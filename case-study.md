# 🧩 Case Study: Automated Applicant Tracker 
## Case Study  
### *A Human-Centered HR-Tech Innovation for Faster, Fairer, and Data-Driven Hiring*

---

## 1. Executive Summary

The **Automated Applicant Tracker** is an AI-powered HR automation tool designed to modernize the recruitment screening process. It evaluates candidate résumés, assigns match scores, generates structured competency insights, and updates applicant statuses automatically.

As an HR professional transitioning into tech, I designed this project to demonstrate how **AI, workflow automation, and human-centered HR practices** can be combined to create scalable, objective, and efficient hiring systems.

By processing applicants in bulk using Python and OpenAI models, the tracker significantly reduces manual workload while improving consistency and fairness in candidate evaluation.

---

## 2. Problem Statement

Traditional résumé screening is one of the most time-consuming and inconsistent parts of recruitment. HR teams face challenges such as:

- High volume of applicants  
- Manual and repetitive screening tasks  
- Human fatigue and bias  
- Lack of structured evaluation frameworks  
- Slow time-to-shortlist  
- Inconsistent decision-making across recruiters  

Small teams and early-stage companies often struggle even more due to limited hiring infrastructure and resources.

There is a clear opportunity to **automate first-round screening**, reduce administrative work, and enable recruiters to focus on higher-value human interactions.

---

## 3. Objective

To develop a lightweight, scalable system that:

- Automates résumé evaluation using AI  
- Assigns objective match scores  
- Identifies strengths and skills gaps  
- Updates applicant statuses automatically  
- Produces structured output for reporting  
- Standardizes the first-round screening process  

The goal is not to replace HR professionals, but to **augment** their decision-making and help them allocate their time more strategically.

---

## 4. Solution Overview

The Automated Applicant Tracker is a modular HR-Tech tool that uses:

- CSV-based applicant pipeline  
- Role-specific job descriptions  
- Résumé text files  
- AI résumé screening engine  
- Business logic for decision-making  
- Automated status updates  

By leveraging Python and OpenAI GPT models, the system converts unstructured résumé data into structured screening insights.

The tracker performs:

- Bulk applicant screening  
- Score-based ranking  
- Automated pipeline updates  
- JSON + CSV reporting  

This ensures every applicant is reviewed **consistently, fairly, and at scale**.

---

## 5. Technical Approach

### a. AI Résumé Screener Engine  
The evaluation logic uses an LLM to produce:
- Match score  
- Summary  
- Strengths  
- Gaps  
- Hiring recommendation  

### b. Business Logic Layer  
Scores are mapped to status updates:
- **≥ 80 — Shortlisted**  
- **60–79 — Screened**  
- **< 60 — Rejected**  

### c. Data Processing Layer  
A CSV file (`applicants.csv`) acts as the central pipeline.

### d. Output Layer  
The system exports:
- `results/applicant_results.json`  
- Updated CSV with statuses and scores  

### e. Modularity  
The architecture allows future integration with:
- ClickUp  
- Notion  
- HRIS tools  
- Streamlit dashboards  

---

## 6. Impact and Results

The Automated Applicant Tracker delivers measurable improvements in recruitment workflow efficiency:

### ⏱ 1. Time Savings  
Bulk automation reduces first-round screening time from hours to minutes.

### 🎯 2. Consistency and Fairness  
Each applicant is evaluated using the same structured criteria, reducing subjective bias.

### 📊 3. Data-Driven Decisions  
Score-based ranking improves quality-of-hire and visibility into role fit.

### ⚙️ 4. Scalability  
The system can process **10 or 1,000 applicants** with equal efficiency.

### 🧠 5. Strategic Value for HR Teams  
HR professionals can focus on interviews, culture fit, and high-touch interactions rather than administrative screening.

---

## 7. Key Learnings

Building this system taught me:

### ✔ How to scale AI résumé screening for multiple applicants  
Understanding how to design batch workflows and structured outputs.

### ✔ The importance of translating HR logic into algorithms  
Business rules (e.g., scoring thresholds) had to be operationalized carefully.

### ✔ Best practices in prompt engineering  
Clear JSON specifications increased reliability and consistency.

### ✔ How to design modular HR-Tech systems  
Separating data, screening logic, and business rules ensures maintainability.

### ✔ How automation can enhance—not replace—human HR judgment  
The tool supports recruiters by handling repetitive tasks, allowing them to focus on human interaction and strategic decision-making.

---

