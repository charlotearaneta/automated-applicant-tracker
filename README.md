# 🎯 Automated Applicant Tracker 

A lightweight HR Tech system that automatically screens candidates, scores résumés, updates applicant statuses, and generates structured evaluations using AI.

This project combines my **HR background** with **Python automation** and **AI résumé screening**, creating a practical tool that helps recruiters streamline candidate screening and improve hiring decisions.

---

## 🌟 Overview

The Automated Applicant Tracker processes applicants in bulk using:

- A **CSV file** containing applicant details  
- **Role specific job descriptions**  
- Individual **résumé files**  
- An **AI-powered résumé evaluation engine**

The system automatically:

✔ Evaluates candidates using AI  
✔ Generates match scores (0–100)  
✔ Highlights strengths & skill gaps  
✔ Gives a hiring recommendation  
✔ Updates each candidate’s status  
✔ Produces structured output (CSV + JSON)

This transforms manual applicant tracking into a simple, repeatable, automated workflow.


---

## 📂 Project Structure

```text

automated-applicant-tracker/
│
├─ data/
│   ├─ applicants.csv
│   ├─ job_it_support.txt
│   ├─ resumes/
│   │   ├─ resume_james.txt
│   │   ├─ resume_emily.txt
│
├─ src/
│   ├─ screen_candidate.py      # AI résumé screening engine
│   ├─ track_applicants.py      # Main automation script
│
├─ results/
│   ├─ applicant_results.json   # Saved evaluations
│
├─ requirements.txt
├─ README.md
└─ case-study.md

```

---


## 🚀 Features

### ✔ Bulk Applicant Processing  
Processes an entire applicant list with one command.

### ✔ Automated AI Summary  
Generates structured evaluation output including:  
- Match score  
- Summary  
- Strengths  
- Gaps  
- Recommendation  

### ✔ Status Updates  
Automatic status assignment based on score thresholds:  
- **Shortlisted**  
- **Screened**  
- **Rejected**  

### ✔ CSV + JSON Output  
Updated applicant data is saved for easy reporting and analysis.

### ✔ Modular & Extendable  
You can plug this into:  
- ClickUp  
- Notion  
- Google Sheets  
- ATS systems  

---


## 🧠 How It Works

### **1. Load applicants**  
Reads the `applicants.csv` file, including:  
- Name  
- Email  
- Role applied for  
- Resume file  
- Status  

### **2. Match to job description**  
Loads the correct job description based on `job_id`.

### **3. AI Screening Engine**  
Uses OpenAI GPT models to evaluate the candidate résumé.

### **4. Update Applicant Status**  
Example logic:  
- Score ≥ 80 → **Shortlisted**  
- Score 60–79 → **Screened**  
- Score < 60 → **Rejected**  

### **5. Save Outputs**  
Stores results into:  
- `results/applicant_results.json`  
- Updated CSV  


---



## 📥 Input Example (applicants.csv)

```csv
name,email,job_id,resume_file,status
James Walker,james.walker@email.com,IT_SUPPORT,resume_james_walker.txt,New
Emily Thompson,emily.thompson@email.com,IT_SUPPORT,resume_emily_thompson.txt,New

```

## 📤 Output Example (AI Evaluation JSON)

```json
{
  "name": "James Walker",
  "job_id": "IT_SUPPORT",
  "score": 82,
  "summary": "James demonstrates a strong technical foundation with relevant troubleshooting experience and customer support skills. His background aligns well with the core requirements of an IT Support role, and he shows clear potential for growth in a professional IT environment.",
  "strengths": [
    "Google IT Support Professional Certificate",
    "Hands-on IT troubleshooting experience",
    "Strong customer service and communication skills",
    "Basic networking knowledge"
  ],
  "gaps": [
    "Limited exposure to enterprise-level IT systems",
    "No direct experience with ticketing platforms"
  ],
  "recommendation": "Good Fit",
  "status": "Shortlisted"
}

```


---


## 🛠 Tech Stack

- **Python**  
- **OpenAI GPT Models**  
- **Pandas** (optional for CSV processing)  
- **python-dotenv** for environment variables  
- **JSON / CSV** for data tracking  


---

## ⚙️ Setup Instructions

## 1. Clone the repository

```bash

git clone https://github.com/charlotearaneta/automated-applicant-tracker.git
cd automated-applicant-tracker

```

## 2. Install dependencies

```bash

pip install -r requirements.txt

```

## 3. Add your API key

Create a .env file:

```env

OPENAI_API_KEY=your_key_here

```

## 4. Run the tracker

```bash

python src/track_applicants.py

```

---

## 🖼 Demo


- Applicant CSV sample  
- Résumé file example  
- Terminal output  
- AI evaluation JSON  
- Final ranked list  

---

## 🗺 Roadmap

### **Phase 1 — MVP**  
- AI résumé evaluation  
- Bulk applicant screening  
- CSV + JSON output  
- Automated status updates  

---

### **Phase 2 — Enhancements**  
- Streamlit UI (web-based tool)  
- PDF résumé parsing  
- Export results to Google Sheets  
- Weighted scoring metrics  

---

### **Phase 3 — ATS-Level Features**  
- Multiple job pipelines  
- Ranking dashboard  
- Candidate history tracking  
- Hiring team collaboration features  

---

### **Phase 4 — Integrations**  
- ClickUp task creation  
- Notion database sync  
- Email notifications  
- API-based ATS compatibility  

---

## 🎯 What I Learned

Building this system taught me:

✔ How to scale AI résumé screening for multiple applicants  
✔ How to automate recruitment workflows using Python  
✔ How to implement decision rules and business logic programmatically  
✔ How to design structured AI outputs using prompt engineering  
✔ How to create modular HR-Tech systems that can integrate with ATS tools  

---

## 🌍 Long Term Vision

To evolve this into a full **AI-powered Applicant Tracking System (ATS)** with:

- Interactive dashboards  
- Automated shortlisting  
- HR workflow automations  
- Candidate scoring history  
- Job pipeline visualizations  

My goal is to make hiring **faster, fairer, and more data-driven**.

---


## 📬 Contact
👩‍💻 Created by: **Charlote Araneta**

🔗 LinkedIn: https://www.linkedin.com/in/charlotearaneta

🌐 Portfolio: https://charlotearaneta.github.io



---

