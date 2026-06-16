<div align="center">

# 📄 CV Optimizer — AI Resume Reviewer Bot

### Drag. Drop. Get Hired. — Instant ATS Score, Keyword Gaps & Rewrite Suggestions Powered by Gemini AI

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)](https://resume-reviewer-bot.netlify.app)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI%20Powered-4285F4?style=for-the-badge&logo=google&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![ATS](https://img.shields.io/badge/ATS-Optimized-8A2BE2?style=for-the-badge&logo=checkmarx&logoColor=white)]()

<br/>

> *"Upload your resume, paste the job description — get an honest ATS match score, missing keywords, formatting fixes, and high-impact rewrite suggestions in seconds."*

</div>

---

## 🎯 What Is This?

**CV Optimizer** is an AI-powered resume reviewer that gives job seekers **brutally honest, actionable feedback** on their resume — the same way a professional recruiter or ATS system would evaluate it.

Most people apply for jobs with resumes that never even reach a human — they get rejected by **ATS (Applicant Tracking Systems)** before anyone reads them. This tool fixes that.

Just drag & drop your PDF resume, paste the job description you're targeting, and get:
- An **ATS match score** (0–100%)
- **Missing keywords** the job description requires but your resume lacks
- **Formatting & structure fixes** that ATS systems penalise
- **High-impact rewrite suggestions** for specific bullet points

> ✅ **No login. No signup. No data stored. Just upload and get results.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📂 **Drag & Drop Upload** | Simple PDF drag-and-drop interface — no form filling |
| 🎯 **ATS Match Score** | Percentage score showing how well your resume matches the job description |
| 🔍 **Missing Keyword Detection** | Identifies important keywords from the JD that are absent in your resume |
| 🛠️ **Formatting & Structure Fixes** | Flags ATS-unfriendly formatting like tables, columns, images, fancy fonts |
| ✍️ **High-Impact Rewrite Suggestions** | Specific bullet point rewrites to make your experience sound stronger |
| ⚡ **Instant Analysis** | Results in seconds — powered by Gemini AI |
| 🔒 **Privacy First** | No resume data is stored or sent to any database |

---

## 🏗️ Architecture & Tech Stack

```
┌──────────────────────────────────────────────────────────────┐
│                    Browser Frontend                          │
│         (Drag & Drop PDF Upload + Results UI)                │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│                   PDF Text Extractor                         │
│            (Reads resume content client-side)                │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│                   Gemini AI (LLM Core)                       │
│     ATS Scoring + Keyword Analysis + Rewrite Generation      │
└───┬───────────────┬────────────────────┬─────────────────────┘
    │               │                    │
┌───▼────┐   ┌──────▼──────┐   ┌────────▼──────────┐
│  ATS   │   │  Keyword    │   │   Rewrite &        │
│  Score │   │  Gap Finder │   │   Structure Fixes  │
│ Engine │   │             │   │   Recommender      │
└────────┘   └─────────────┘   └───────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│                  Results Dashboard                           │
│     Score + Missing Keywords + Fixes + Rewrites              │
└──────────────────────────────────────────────────────────────┘
```

### 🛠️ Technologies Used

- **Frontend:** HTML, CSS, Vanilla JavaScript
- **AI Engine:** Google Gemini AI (LLM)
- **PDF Parsing:** Client-side PDF text extraction
- **Deployment:** Netlify
- **Storage:** None — fully stateless, privacy-first

---

## 💬 How It Works — Step by Step

```
Step 1 — Upload Resume
  └── Drag & drop your PDF resume onto the upload area

Step 2 — Paste Job Description
  └── Copy-paste the job description you are applying for

Step 3 — Click "Analyze"
  └── Gemini AI reads both documents and compares them

Step 4 — Get Your Results
  ├── 🎯 ATS Match Score:         78%
  ├── ❌ Missing Keywords:         "React", "CI/CD", "Agile", "REST APIs"
  ├── 🛠️ Formatting Fixes:        "Remove tables — ATS can't read them"
  │                               "Use standard section headers"
  └── ✍️ Rewrite Suggestions:
        Before: "Worked on website features"
        After:  "Engineered 3 customer-facing React features,
                 reducing page load time by 40%"
```

---

## 🧠 How the AI Works

**1. PDF Parsing**
The resume PDF is read client-side in the browser and its raw text is extracted — no file upload to any server.

**2. Dual-Document Analysis**
Gemini AI receives both the resume text and the job description together, and is prompted to act as a senior recruiter + ATS system evaluating the match.

**3. ATS Scoring**
The model calculates a match percentage based on keyword overlap, relevant experience alignment, and role-specific terminology presence.

**4. Keyword Gap Detection**
Important terms from the job description that are missing from the resume are identified — these are exactly what ATS filters screen for.

**5. Structured Feedback Generation**
Rather than generic advice, the model generates specific, actionable rewrites for actual bullet points in the user's resume — making it easy to act on the feedback immediately.

---

## 📁 Project Structure

```
resume-reviewer-bot/
│
├── index.html           # Full app — UI, PDF parsing, Gemini API calls & results
└── README.md            # Project documentation
```

> 💡 Built as a lightweight single-file app deployed on Netlify — no backend, no database, no build step required.

---

## 🎯 Skills Demonstrated

This project showcases the following for potential employers:

- ✅ **LLM Integration** — Gemini AI API for intelligent document analysis
- ✅ **Prompt Engineering** — Crafting prompts that make an LLM behave like an ATS + recruiter
- ✅ **Client-Side PDF Parsing** — Extracting and processing PDF text in the browser
- ✅ **Dual-Document Reasoning** — Comparing two documents (resume vs JD) and extracting insights
- ✅ **Privacy-First Architecture** — Zero data storage, fully client-side processing
- ✅ **Clean UI/UX** — Drag-and-drop interface, structured results display
- ✅ **Frontend Deployment** — Live production app on Netlify

---

## 🌍 Why This Matters

Over **75% of resumes** are rejected by ATS systems before a human ever reads them — not because the candidate is unqualified, but because their resume isn't optimised for the specific job.

This tool gives every job seeker access to the same quality of resume feedback that was previously only available from expensive career coaches or recruitment consultants — **completely free, in seconds**.

---

## 🔮 Future Roadmap

- [ ] Support for DOCX resume uploads
- [ ] LinkedIn profile URL analysis
- [ ] Role-specific resume templates after analysis
- [ ] Cover letter generator based on resume + JD
- [ ] Side-by-side before/after resume view
- [ ] Multiple JD comparison (find the best-fit job)

---

## 🚀 My Other Projects

| Project | Description | Live Demo |
|---|---|---|
| ✈️ **AI Travel Agent** | AI trip planner — live flight & train prices, weather, budget-aware itineraries | [![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://travelagent-bqtmr6s69hxtqk8oxibuqj.streamlit.app/) |
| 🌾 **Agriculture AI Assistant** | AI bot for Indian farmers — mandi prices, disease detection, schemes, RAG | [![Live Demo](https://img.shields.io/badge/Live%20Demo-HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/spaces/suszi-2/AGRICULTURE_BOT) |

---

## 🙋‍♂️ About the Developer

Built with ❤️ by **[SHAKSHI SONI]**

I build practical AI tools that solve everyday problems. This project demonstrates my ability to combine LLM prompt engineering, client-side PDF processing, and clean UI design into a privacy-first, zero-backend production app.

📫 **Connect with me:**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Profile-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/suszi-2)

---

<div align="center">

**⭐ Star this repo if it helped you land interviews — it means a lot!**

*Built to give every job seeker a fair shot at getting past the ATS filter.*

</div>
