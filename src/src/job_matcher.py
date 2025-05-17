# src/job_matcher.py
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_jobs(csv_path):
    return pd.read_csv(csv_path)

def recommend_jobs(resume_text, jobs_df, top_n=5):
    job_texts = jobs_df['description'].tolist()
    job_embeddings = model.encode(job_texts, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    
    similarities = util.cos_sim(resume_embedding, job_embeddings)[0]
    top_matches = similarities.topk(k=top_n)
    
    matched_jobs = []
    for idx in top_matches[1]:
        matched_jobs.append(jobs_df.iloc[int(idx)])
    
    return pd.DataFrame(matched_jobs)
