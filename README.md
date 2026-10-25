AI Resume Analyzer and Job Recommendation System

 Project Overview

The AI Resume Analyzer and Job Recommendation System is a Python-based web application built using Streamlit. It analyzes uploaded resumes, identifies relevant skills, compares them with job-role requirements, and provides match scores and skill-gap suggestions.

 Features

* Upload resumes in PDF and DOCX formats.
* Extract and clean resume text.
* Detect and categorize technical skills.
* Compare resume skills with multiple job roles.
* Calculate job-role match scores.
* Display matched and missing skills.
* Provide a learning roadmap for missing skills.
* Download a resume analysis report.

Technologies Used

* Python
* Streamlit
* pypdf
* python-docx

 Project Files

* `app.py` — Main Streamlit application.
* `resume_parser.py` — Extracts text from resumes.
* `text_cleaner.py` — Cleans extracted text.
* `skill_extractor.py` — Identifies skills in resumes.
* `job_roles.py` — Contains job roles and required skills.
* `job_matcher.py` — Calculates job-role match scores.

 How to Run the Project

1. Install Python on your computer.

2. Open the project folder in VS Code.

3. Open the terminal in VS Code.

4. Install the required packages using the project's `requirements.txt` file, if available:

   `pip install -r requirements.txt`

5. Run the application:

   `streamlit run app.py`

6. Open the local URL displayed in the terminal.

How to Use

1. Upload a PDF or DOCX resume.
2. Review the extracted skills.
3. View job-role match scores and recommendations.
4. Select a target role to view missing skills.
5. Review the learning roadmap.
6. Download the analysis report.

 Limitations

Match scores are estimates based on the skills detected in the resume. Missing keywords do not necessarily mean that a candidate lacks a skill. The application is intended for career guidance, not automatic hiring or rejection.

 Future Improvements

* Improve skill extraction accuracy.
* Add more job roles and skill datasets.
* Enhance matching using TF-IDF and cosine similarity.
* Add testing and deploy the application online.
