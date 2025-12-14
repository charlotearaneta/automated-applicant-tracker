# src/track_applicants.py

import csv
import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

from dotenv import load_dotenv
from openai import OpenAI


# ----------------------------
# CONFIG
# ----------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")  # You can override via .env if you want

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RESUMES_DIR = DATA_DIR / "resumes"
RESULTS_DIR = PROJECT_ROOT / "results"

APPLICANTS_CSV = DATA_DIR / "applicants.csv"
UPDATED_CSV = DATA_DIR / "applicants_updated.csv"
RESULTS_JSON = RESULTS_DIR / "applicant_results.json"

# Map job_id -> job description file
JOB_FILES = {
    "IT_SUPPORT": DATA_DIR / "job_it_support.txt",
    # Add more later:
    # "HR_ASSISTANT": DATA_DIR / "job_hr_assistant.txt",
}


# Status thresholds
SHORTLIST_THRESHOLD = 80
SCREENED_THRESHOLD = 60


# ----------------------------
# HELPERS
# ----------------------------

def read_text(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")
    return file_path.read_text(encoding="utf-8").strip()


def safe_int(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def decide_status(score: int) -> str:
    if score >= SHORTLIST_THRESHOLD:
        return "Shortlisted"
    if score >= SCREENED_THRESHOLD:
        return "Screened"
    return "Rejected"


def build_prompt(job_description: str, resume: str) -> str:
    return f"""
You are an experienced recruiter. Evaluate the candidate's resume against the job description.

Return ONLY valid JSON with exactly these keys:
- score (integer 0-100)
- summary (string, 2-4 sentences)
- strengths (array of strings)
- gaps (array of strings)
- recommendation (string: "Strong Fit" | "Good Fit" | "Needs Development" | "Not a Fit")

Be professional, structured, and avoid sensitive demographic assumptions (age, gender, race, religion, etc.).
Focus on skills, experience, evidence, and role alignment.

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume}
""".strip()


def extract_text_from_response(resp) -> str:
    """
    Tries to safely extract the model's text output from the OpenAI Responses API object.
    """
    try:
        return resp.output[0].content[0].text.strip()
    except Exception:
        # Fallback (rare)
        return str(resp).strip()


def parse_json_or_fallback(raw: str) -> Dict[str, Any]:
    """
    Attempts to parse JSON. If the model returns extra text, try to locate JSON block.
    """
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Try to salvage JSON by finding first { and last }
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            candidate = raw[start:end + 1]
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                pass

    return {
        "score": None,
        "summary": "Could not parse model output as JSON.",
        "strengths": [],
        "gaps": [],
        "recommendation": "Needs Development",
        "raw_output": raw
    }


def evaluate_candidate(client: OpenAI, job_description: str, resume: str) -> Dict[str, Any]:
    prompt = build_prompt(job_description, resume)

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    raw_text = extract_text_from_response(response)
    data = parse_json_or_fallback(raw_text)

    # Normalize types
    score = safe_int(data.get("score"))
    data["score"] = score

    # Ensure list types
    if not isinstance(data.get("strengths"), list):
        data["strengths"] = []
    if not isinstance(data.get("gaps"), list):
        data["gaps"] = []

    # Ensure recommendation is string
    if not isinstance(data.get("recommendation"), str):
        data["recommendation"] = "Needs Development"

    return data


# ----------------------------
# MAIN WORKFLOW
# ----------------------------

def load_applicants(csv_path: Path) -> List[Dict[str, str]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing applicants file: {csv_path}")

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    required_cols = {"name", "email", "job_id", "resume_file", "status"}
    if not required_cols.issubset(set(reader.fieldnames or [])):
        raise ValueError(f"applicants.csv must contain columns: {sorted(required_cols)}")

    return rows


def save_updated_csv(rows: List[Dict[str, Any]], output_path: Path) -> None:
    if not rows:
        return

    fieldnames = list(rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_results_json(results: List[Dict[str, Any]], output_path: Path) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def main():
    if not OPENAI_API_KEY:
        raise RuntimeError("Missing OPENAI_API_KEY. Add it to your .env file.")

    client = OpenAI(api_key=OPENAI_API_KEY)

    applicants = load_applicants(APPLICANTS_CSV)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    all_results: List[Dict[str, Any]] = []
    updated_rows: List[Dict[str, Any]] = []

    print(f"🔎 Loaded {len(applicants)} applicant(s).")

    for row in applicants:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip()
        job_id = row.get("job_id", "").strip()
        resume_file = row.get("resume_file", "").strip()
        status = row.get("status", "").strip()

        print(f"\n🧾 Applicant: {name} | Job: {job_id} | Current status: {status}")

        # Only process "New" applicants (change if you want)
        if status.lower() != "new":
            print("↪ Skipping (not New).")
            updated_rows.append(row)
            continue

        job_path = JOB_FILES.get(job_id)
        if not job_path:
            print(f"⚠ Unknown job_id: {job_id}. Add it to JOB_FILES. Skipping.")
            updated_rows.append(row)
            continue

        resume_path = RESUMES_DIR / resume_file

        try:
            job_description = read_text(job_path)
            resume_text = read_text(resume_path)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            updated_rows.append(row)
            continue

        evaluation = evaluate_candidate(client, job_description, resume_text)

        score = evaluation.get("score")
        if score is None:
            final_status = "Screened"  # safe default
        else:
            final_status = decide_status(score)

        result_record = {
            "name": name,
            "email": email,
            "job_id": job_id,
            "score": score,
            "summary": evaluation.get("summary", ""),
            "strengths": evaluation.get("strengths", []),
            "gaps": evaluation.get("gaps", []),
            "recommendation": evaluation.get("recommendation", ""),
            "status": final_status,
        }

        all_results.append(result_record)

        # Add columns to CSV row
        updated_row = dict(row)
        updated_row["score"] = "" if score is None else score
        updated_row["recommendation"] = result_record["recommendation"]
        updated_row["updated_status"] = final_status
        updated_row["summary"] = result_record["summary"]
        updated_rows.append(updated_row)

        print(f"✅ Result: score={score} → {final_status} ({result_record['recommendation']})")

    # Save outputs
    save_results_json(all_results, RESULTS_JSON)
    save_updated_csv(updated_rows, UPDATED_CSV)

    print("\n📦 Outputs saved:")
    print(f" - JSON: {RESULTS_JSON}")
    print(f" - CSV : {UPDATED_CSV}")


if __name__ == "__main__":
    main()

