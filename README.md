# Resume Matcher (Beginner-Friendly AI Project)

This project helps compare a **resume** against a **job description**, highlighting matches, gaps, and suggestions for improvement. It’s built with **Streamlit** for the frontend and basic **NLP techniques** for comparison.

---

## 🚀 Features
- Upload Resume (.pdf or .docx)
- Upload Job Description (.pdf, .docx, or text)
- Compare and score similarity
- Highlight strengths and gaps
- AI-powered suggestions (if OpenAI API is enabled)
- Generate a simple report

---

## 📂 Project Structure
resume_matcher/
├── app.py                 # Main Streamlit app
├── utils/
│   ├── __init__.py        # Makes utils a Python package
│   ├── extract.py          # Text extraction logic
│   ├── compare.py          # Matching + scoring logic
│   └── report.py           # Report generation logic
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
├── .gitignore             # Ignore cache/env files
└── .vscode/               # VS Code config (optional)
    └── settings.json      # Extra paths for Pylance