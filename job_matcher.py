from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def calculate_similarity(resume_text,job_description):
   documents=(resume_text,job_description)
   Vectorizer=TfidfVectorizer()
   Vectors=Vectorizer.fit_transform(documents)
   similarity=cosine_similarity(Vectors[0:1],Vectors[1:2])[0][0]
   return round(float(similarity)*100,2)
def calculate_match(resume_skills,required_skills):
    resume_set={skill.lower().strip() for skill in resume_skills}
    required_set={skill.lower().strip() for skill in required_skills}
    matched=[
        skill for skill in required_skills
        if skill.lower().strip() in resume_set]
    missing=[
        skill for skill in required_skills
        if skill.lower().strip() not in resume_set]
    if required_skills:
     score=len(matched)/len(required_skills)*100 
    else :
       score=0
    return round (score,2),matched,missing