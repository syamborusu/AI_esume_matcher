import streamlit as st
from utils.extract import extract_text
from utils.compare import calculate_match_score, extract_top_keywords
from utils.report import generate_report

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("📄 AI Resume Matcher & Career Assistant")
st.markdown("Upload a resume and a job description to get a match score, keyword insights, and AI suggestions.")

resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"] )
jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

if resume_file and jd_file:
    with st.spinner("Extracting text..."):
        resume_text = extract_text(resume_file)
        jd_text = extract_text(jd_file)

    score = calculate_match_score(resume_text, jd_text)

    st.metric(label="Match Score", value=f"{score}%")

    st.subheader("Keyword Snapshot")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Resume top keywords**")
        st.write(extract_top_keywords(resume_text, top_n=10))
    with col2:
        st.write("**JD top keywords**")
        st.write(extract_top_keywords(jd_text, top_n=10))

    if st.button("Generate Full Report & Suggestions"):
        with st.spinner("Generating suggestions (may use OpenAI)..."):
            report = generate_report(resume_text, jd_text, score,
                                     top_resume_keywords=extract_top_keywords(resume_text, 10),
                                     top_jd_keywords=extract_top_keywords(jd_text, 10))
        st.subheader("Report")
        st.text(report)

else:
    st.info("Upload both a resume and a job description to start.")

st.markdown("---")
st.markdown("**Notes:**\n- To enable AI suggestions set environment variable `OPENAI_API_KEY`.\n- This is a beginner-friendly starting point; consider adding better NLP models, an ATS keyword matcher, and resume rewriting features.")