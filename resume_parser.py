from pypdf import PdfReader
from docx import Document
def extract_text(file):
    if file.name.lower().endswith (".pdf"):
      reader=PdfReader(file)
      text=""
      for page in reader.pages:
       page_text=page.extract_text()
       if page_text:
        text+=page_text +"\n"
       return text 
    elif file.name.lower().endswith/ ".docx":
       document=Document(file)
       text=""
       for paragraph in document.paragraphs:
        text+= paragraph.text +"/n"
       return text
    return ""   
       
