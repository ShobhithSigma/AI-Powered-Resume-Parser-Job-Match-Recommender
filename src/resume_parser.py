# src/resume_parser.py
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_entities(text):
    doc = nlp(text)
    skills = []
    education = []
    experience = []
    
    for ent in doc.ents:
        if ent.label_ == "ORG":
            education.append(ent.text)
        elif ent.label_ == "DATE":
            experience.append(ent.text)
        elif ent.label_ == "PERSON":
            continue
        elif ent.label_ == "GPE":
            continue
        else:
            skills.append(ent.text)
    
    return {
        "skills": list(set(skills)),
        "education": list(set(education)),
        "experience": list(set(experience))
    }
