SKILLS={"programming":['python','java','c','c++','c#','javascript'],
'databases':['sql','my sql','moongdb','postgresql'],
'machine_learning':['machine learning','scikit-learn','tensorflow','pytotrch'],
'data':['pandas','numpy','excel','power bi'],
'web':['html','css','javascript','react','fastapi'],
'ai_nlp':['deep learning','nlp','llm','rag','transformers'],
'tools':['git','github','docker','opencv','yolo']}
def extract_skills(text):
    text=text.lower()
    skill_categories={"programming":['python','java','c'],
                      'databases':['sql','my sql','moongdb','postgresql'],
                      'machine_learning':['machine learning','scikit-learn','tensorflow','pytotrch'],
                      'data':['pandas','numpy','excel','power bi'],
                      'web':['html','css','javascript','react','fastapi'],
                      'ai_nlp':['deep learning','nlp','llm','rag','transformers'],
                      'tools':['git','github','docker','opencv','yolo']}
    found_skills={}
    for category,skill_list in skill_categories.items():
        matched=[
            skill for skill in skill_list
            if skill in text
        ]            
        found_skills[category]=matched
    return found_skills    