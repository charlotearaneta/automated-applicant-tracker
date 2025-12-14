import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def screen_candidate(job_description: str, resume: str):
    """
    Sends job + resume to OpenAI and gets a structured evaluation.
    """
    prompt = f"""
You are an experienced HR and recruitment specialist.

You will receive:
1) A job description
2) A candidate's resume

Your task:
- Evaluate how well the candidate fits the role.
- Provide:
  a. Overall match score from 0 to 100
  b. Summary (3–5 sentences)
  c. Key strengths
  d. Skill or experience gaps
  e. Recommended decision: "Strong Fit", "Good Fit", "Needs Development", or "Not a Fit"

Respond in valid JSON with the following keys:
- score
- summary
- strengths
- gaps
- recommendation

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        # we expect a JSON-style answer, but the model still outputs as text
    )

    # Extract text from the response
    result_text = response.output[0].content[0].text

    return result_text

def main():
    job_description = load_text("data/job_description.txt")
    resume = load_text("data/candidate_resume.txt")

    print("🔎 Screening candidate for the role...\n")

    evaluation = screen_candidate(job_description, resume)

    print("📊 Evaluation Result:\n")
    print(evaluation)

if __name__ == "__main__":
    main()

