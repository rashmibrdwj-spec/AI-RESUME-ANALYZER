import streamlit as st
from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_roles import JOB_ROLES
from job_matcher import calculate_match
from job_matcher import calculate_similarity
st.title ('AI RESUME ANALYZER')
st.write('UPLOAD YOUR RESUME TO BEGIN ANALYSIS')
uploaded_file=st.file_uploader('UPLOAD YOUR RESUME',
type=['pdf','docx'])
if uploaded_file is not None:
    st.success('RESUME UPLOADED SUCCESSFULLY:')
    st.write('FILE NAME:',uploaded_file.name)
    resume_text=extract_text(uploaded_file)
    cleaned_text=clean_text(resume_text)
    skills=extract_skills (cleaned_text)
    st.subheader("CLEANED RESUME TEXT")
    st.text(cleaned_text)
    st.subheader('EXTRACTED RESUME TEXT')
    st.text(resume_text)
    st.write('FILE SIZE:',uploaded_file.size,"bytes")    
    st.subheader('Skills Found')
    for category, skill_list in skills.items():
        if skill_list:
         st.write(
                 category.replace("_","").title(),
                 ';',
                 ','.join(skill_list))
    st.subheader('Job Role Recommendaton')
    resume_skills=[skill
            for skill_list in skills.values()
                for skill in skill_list]    
    st.subheader ('Resume Summary')
    col1,col2=st.columns(2)
    col1.metric('Skills Detected',len(resume_skills))
    col2.metric('Job Rules Analyzed',len(JOB_ROLES))     
    results=[]
    for role,required_skills in JOB_ROLES.items():
                   score,matched,missing=calculate_match(resume_skills,required_skills)
    results.append((role,score,matched,missing))             
    results.sort(key=lambda item:item[1],reverse=True)
    for role,score,matched,missing in results:
                      st.write(f'** {role}-{score} % match**')
                      st.progress(score/100)
                      st.write('Matched skills',','.join(matched) or'None')
                      st.write('Missing Skills',','.join(missing) or'None')
                      st.divider()       
    st.subheader('Skill Gap Analysis')
    target_role=st.selectbox('choose your target job role',
    list(JOB_ROLES.keys())
    )
    resume_skills=[
         skill.lower().strip()
         for skill_list in skills.values()
         for skill in skill_list]
    st.write('DEBUG-DETECTED SKILLS',resume_skills)
    required_skills=JOB_ROLES[target_role]      
    matched_skills=[
    skill for skill in required_skills
    if skill.lower().strip() in resume_skills]     
    missing_skills=[
    skill for skill in required_skills
    if skill.lower().strip() not in resume_skills]
    total_skills=len(required_skills)
    match_percentage=(round(len(matched_skills)/total_skills*100,2)
    if total_skills > 0 else 0)
    st.subheader('JOB MATCH RESULT')
    st.metric("MATCH PERCENTAGE",f'{match_percentage}%')
    st.write('Target Role',target_role)
    st.write(
         'Skills You Have',
         ','.join(matched_skills)or'None found')
    st.write(
         'Skills to Learn',
         ','.join(missing_skills)or 'None identified')
    st.subheader('LEARNNG ROADMAP')
    if missing_skills:
                for skill in missing_skills:
                  st.write(f"learn{skill}")
    else:
          st.success('YOU HAVE ALL THE LISTED SKILLS FOR THIS ROLE')              
    st.subheader('Download Analysis Report')
    report=f"""
    AI RESUME ANALYZER REPORT
    Resume:{uploaded_file.name}
    Target_Job_Role:{target_role}
    Skills Found:
    {','.join(resume_skills) or 'None found'}
    skills Matched  for Target Role:
    {','.join(matched_skills) or 'None found'}
    skills to learn:
    {','.join(missing_skills) or 'None identified'}    
     """
    st.download_button(
         label='Download Report',
         data=report,
         file_name='resume_analysis_report.txt',mime='text/plain')


                                   
                                                             

