# app/streamlit_app.py
import streamlit as st
from src.resume_parser import extract_text_from_pdf, extract_entities
from src.job_matcher import load_jobs, recommend_jobs

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("📄 AI Resume Matcher & Job Recommender")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with open("resumes/temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    text = extract_text_from_pdf("resumes/temp_resume.pdf")
    entities = extract_entities(text)

    st.subheader("🧠 Extracted Resume Data:")
    st.json(entities)

    jobs_df = load_jobs("data/jobs_dataset.csv")
    recommended_jobs = recommend_jobs(text, jobs_df)

    st.subheader("✅ Recommended Jobs")
    st.dataframe(recommended_jobs[["title", "company", "location"]])
