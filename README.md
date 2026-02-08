# Innovix-Santhiya-
Innovix Hackathon Project – Personalized Career Roadmap Platform with Resume Analysis, Skill Recommendation, and AI-powered Career Guidance.

## Project Overview
This is a career guidance web application designed to help users analyze their resumes, receive personalized feedback, and get a suggested career roadmap. The platform provides:  
- Skills-based career domain suggestions  
- Step-by-step learning roadmap  
- Relevant company recommendations for each career path  
- Resume analysis with market-aligned feedback  
- Adaptive strategies to improve employability  

Developed for **Hackathon 2026** using **Python Flask**, **HTML/CSS/Tailwind**, and **JavaScript**.

---

## Features

### 1. Career Suggestion
- Suggests a relevant career domain based on user skills or interests.
- Displays a roadmap with progress bars for key skills.

### 2. Company Recommendations
- Shows companies hiring for the suggested role.
- Provides “Apply Now” links for each company.

### 3. Resume Analysis
- Extracts text from PDF/DOCX resumes.
- Matches skills against job market requirements.
- Gives a score, proficiency level, and missing skills.
- Suggests adaptive strategies for improvement.

### 4. Responsive UI
- Clean, interactive interface using Tailwind CSS.
- Works across desktops, tablets, and mobile devices.

---

## Tech Stack
- **Backend:** Python Flask  
- **Frontend:** HTML, CSS, Tailwind CSS, JavaScript  
- **Resume Parsing:** PyPDF2 (PDF), python-docx (DOCX)  
- **Version Control:** Git & GitHub  

---
Installation

Follow these steps to run the project locally:

Clone the repository

git clone https://github.com/Santhiya-17/Innovix-Santhiya-.git


Navigate into the project folder

cd Innovix

Create a virtual environment

python -m venv venv


Activate the virtual environment

On Windows:

venv\Scripts\activate


On Linux/Mac:

source venv/bin/activate


Install the required Python packages

pip install -r requirements.txt


Run the Flask application

python app.py


Open the app in your browser
Go to:

http://127.0.0.1:5000/
