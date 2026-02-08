from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ---------------- SKILLS DICTIONARY ----------------
SKILLS = {
    "Software Development & Programming": [
        "java", "python", "c", "c++", "javascript", "typescript", "kotlin", "swift",
        "dart", "go", "rust", "sql", "nosql", "shell scripting", "bash", "powershell",
        "oop", "functional programming", "data structures", "algorithms",
        "multithreading", "concurrency", "api development", "microservices",
        "design patterns", "unit testing", "git", "github"
    ],
    "Web Development": [
        "html", "css", "bootstrap", "tailwind", "responsive design", "react", "angular",
        "vue", "node", "express", "next", "webpack", "vite", "pwa", "web security", "seo", "ajax"
    ],
    "Mobile App Development": [
        "android studio", "ios", "swiftui", "flutter", "react native", "cross-platform",
        "mobile ui/ux", "mobile testing", "firebase", "push notifications", "app store", "play store"
    ],
    "AI & Machine Learning": [
        "tensorflow", "pytorch", "scikit-learn", "keras", "opencv", "nlp", "data preprocessing",
        "feature engineering", "model evaluation", "regression", "classification",
        "clustering", "recommendation", "neural networks", "generative ai", "reinforcement learning"
    ],
    "Data & Analytics": [
        "python", "r", "sql", "excel", "power bi", "tableau", "statistics",
        "machine learning", "data visualization", "data cleaning", "data preprocessing"
    ],
    "Cyber Security": [
        "network", "linux", "security", "firewall", "penetration", "ethical hacking",
        "risk assessment", "threat modeling", "vulnerability assessment", "siem"
    ],
    "Design & Creativity": [
        "figma", "adobe xd", "photoshop", "illustrator", "wireframe", "prototype", "ui", "ux"
    ],
    "Management & Business": [
        "requirement", "analysis", "business", "stakeholder", "case study",
        "project management", "scrum", "agile", "kanban"
    ]
}

# ---------------- DOMAIN SUGGESTION ----------------
def suggest_domain(interest, skills):
    interest = interest.lower() if interest else ""
    mapping = {
        "design": "UI/UX Designer",
        "data": "Data Analyst / Data Scientist",
        "security": "Cyber Security Engineer",
        "management": "Product / Business Analyst",
        "development": "Software Developer"
    }
    
    # Check interest
    if interest in mapping:
        return mapping[interest]
    
    # Check skills
    for category, skill_list in SKILLS.items():
        for skill in skills:
            if skill.lower() in [s.lower() for s in skill_list]:
                if category == "Design & Creativity":
                    return "UI/UX Designer"
                elif category == "Software Development & Programming":
                    return "Software Developer"
                elif category == "Cyber Security":
                    return "Cyber Security Engineer"
                elif category in ["Data & Analytics", "AI & Machine Learning"]:
                    return "Data Analyst / Data Scientist"
                elif category == "Management & Business":
                    return "Product / Business Analyst"
    return "Software Developer"

# ---------------- ROADMAP ----------------
def get_roadmap(domain):
    roadmaps = {
        "UI/UX Designer": """
        <ul>
            <li>Learn UI/UX fundamentals</li>
            <li>Master Figma & Wireframing</li>
            <li>Build portfolio projects</li>
        </ul>
        """,
        "Software Developer": """
        <ul>
            <li>Master DSA & Algorithms</li>
            <li>Learn backend development</li>
            <li>Build real-world projects</li>
        </ul>
        """,
        "Cyber Security Engineer": """
        <ul>
            <li>Networking & Linux</li>
            <li>Security fundamentals</li>
            <li>Hands-on labs (TryHackMe)</li>
        </ul>
        """,
        "Data Analyst / Data Scientist": """
        <ul>
            <li>Python & SQL</li>
            <li>Statistics & ML basics</li>
            <li>Data projects</li>
        </ul>
        """,
        "Product / Business Analyst": """
        <ul>
            <li>Requirement analysis</li>
            <li>Business case studies</li>
            <li>Stakeholder communication</li>
        </ul>
        """
    }
    return roadmaps.get(domain, "<p>Roadmap coming soon.</p>")

# ---------------- COMPANY DETAILS ----------------
COMPANY_DETAILS = {
    "Software Developer": [
        {"name": "Amazon", "type": "Product", "description": "Develop scalable applications and microservices in a team environment."},
        {"name": "TCS", "type": "MNC", "description": "Work on enterprise software solutions, client engagement, and Agile projects."},
        {"name": "Swiggy", "type": "Startup", "description": "Build and optimize the core delivery platform with new features."}
    ],
    "UI/UX Designer": [
        {"name": "Google", "type": "Product", "description": "Design user-centric interfaces and prototypes for global products."},
        {"name": "Accenture", "type": "MNC", "description": "Provide UI/UX solutions for enterprise clients."},
        {"name": "Zerodha", "type": "Startup", "description": "Create engaging user experiences for trading platforms."}
    ],
    "Cyber Security Engineer": [
        {"name": "CrowdStrike", "type": "Product", "description": "Develop and implement cybersecurity solutions for global clients."},
        {"name": "Deloitte", "type": "MNC", "description": "Conduct security audits and risk assessments for enterprises."},
        {"name": "QuickHeal", "type": "Startup", "description": "Develop antivirus and threat protection software."}
    ],
    "Data Analyst / Data Scientist": [
        {"name": "Netflix", "type": "Product", "description": "Analyze user data and build recommendation systems."},
        {"name": "Capgemini", "type": "MNC", "description": "Perform data analytics for enterprise solutions."},
        {"name": "Fractal", "type": "Startup", "description": "Work on data-driven AI solutions for clients."}
    ],
    "Product / Business Analyst": [
        {"name": "Uber", "type": "Product", "description": "Define business requirements and improve product workflows."},
        {"name": "BCG", "type": "MNC", "description": "Consult on business strategy and analytics projects."},
        {"name": "Flipkart", "type": "Startup", "description": "Analyze market trends and drive product improvements."}
    ]
}

def get_companies(domain):
    return COMPANY_DETAILS.get(domain, [])

# ---------------- RESUME EXTRACTION ----------------
def extract_text(path, ext):
    text = ""
    if ext == "pdf":
        reader = PdfReader(path)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif ext == "docx":
        doc = Document(path)
        for para in doc.paragraphs:
            text += para.text
    return text.lower()

# ---------------- JOB MARKET WEIGHTS ----------------
JOB_MARKET_WEIGHTS = {
    "UI/UX Designer": {"figma": 0.30, "ux": 0.25, "prototype": 0.20, "wireframe": 0.15, "ui": 0.10},
    "Software Developer": {"dsa": 0.30, "algorithm": 0.25, "python": 0.20, "java": 0.15, "git": 0.10},
    "Cyber Security Engineer": {"network": 0.30, "linux": 0.25, "security": 0.20, "firewall": 0.15, "penetration": 0.10},
    "Data Analyst / Data Scientist": {"python": 0.30, "sql": 0.25, "statistics": 0.20, "machine learning": 0.15, "data": 0.10},
    "Product / Business Analyst": {"requirement": 0.30, "analysis": 0.25, "business": 0.20, "stakeholder": 0.15, "case study": 0.10}
}

# ---------------- RESUME ANALYSIS ----------------
def analyze_resume(text, role):
    role_skills = list(JOB_MARKET_WEIGHTS.get(role, {}).keys())
    matched = [s for s in role_skills if s in text]
    missing = [s for s in role_skills if s not in text]

    if not matched:
        return [], 0, "Beginner", missing, ["⚠️ Focus on foundational skills for this role"]

    weights = JOB_MARKET_WEIGHTS.get(role, {})
    score = int(sum(weights[s] for s in matched if s in weights) * 100)

    if score >= 80:
        level = "Ready for Interview"
    elif score >= 50:
        level = "Intermediate"
    else:
        level = "Beginner"

    feedback = []
    if missing:
        feedback.append("⚠️ Focus on high-demand market skills")
    else:
        feedback.append("✅ Strong skill alignment with current job market")

    return matched, score, level, missing, feedback

# ---------------- PRIORITIZE SKILLS ----------------
def prioritize_skills(role, missing_skills):
    weights = JOB_MARKET_WEIGHTS.get(role, {})
    ranked = sorted(missing_skills, key=lambda skill: weights.get(skill, 0), reverse=True)
    return ranked

# ---------------- CAREER OUTCOME ----------------
def career_outcome(role, level):
    outcomes = {
        "Beginner": {"category": "Internships & Entry-Level", "strategy": "Build fundamentals & projects"},
        "Intermediate": {"category": "Service & Mid-size Companies", "strategy": "Upskill and apply for full-time roles"},
        "Ready for Interview": {"category": "Product Companies & MNCs", "strategy": "Mock interviews & referrals"}
    }
    return outcomes.get(level, {})

# ---------------- ADAPTIVE STRATEGY ----------------
def adaptive_strategy(level, interview_feedback, project_feedback):
    strategy = {"reduce_focus": [], "increase_focus": [], "actions": []}

    if interview_feedback == "poor_communication":
        strategy["increase_focus"].append("Explain projects clearly")
        strategy["actions"].append("Practice mock interviews")
        strategy["actions"].append("Revise project storytelling")

    if interview_feedback == "weak_concepts":
        strategy["increase_focus"].append("Core fundamentals")
        strategy["actions"].append("Revise theory before coding")

    if project_feedback == "weak_projects":
        strategy["increase_focus"].append("Hands-on projects")
        strategy["actions"].append("Refine existing projects")
        strategy["actions"].append("Add real-world use cases")

    if level == "Ready for Interview":
        strategy["reduce_focus"].append("New skill acquisition")
        strategy["actions"].append("Focus on interviews & referrals")

    return strategy

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/career")
def career():
    return render_template("career.html", skills=SKILLS)

@app.route("/analyze", methods=["POST"])
def analyze():
    domain = suggest_domain(
        request.form.get("interest"),
        request.form.getlist("skills")
    )
    return render_template(
        "result.html",
        domain=domain,
        roadmap=get_roadmap(domain),
        companies=get_companies(domain)
    )

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/review_resume", methods=["POST"])
def review_resume():
    role = request.form.get("target_role")
    file = request.files.get("resume_file")

    ext = file.filename.split(".")[-1]
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    text = extract_text(path, ext)

    matched, score, level, missing, feedback = analyze_resume(text, role)
    priority_skills = prioritize_skills(role, missing)
    outcome = career_outcome(role, level)

    interview_feedback = "poor_communication" if score < 70 else "good"
    project_feedback = "weak_projects" if len(priority_skills) > 3 else "good"

    adaptive_plan = adaptive_strategy(level, interview_feedback, project_feedback)

    return render_template(
        "resume_result.html",
        role=role,
        feedback=feedback,
        score=score,
        level=level,
        priority_skills=priority_skills,
        outcome=outcome,
        adaptive_plan=adaptive_plan
    )

if __name__ == "__main__":
    app.run(debug=True)








