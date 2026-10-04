from pypdf import PdfReader
path="data\\leave_policy.pdf"
reader=PdfReader(path)
pages=[]
for page_number,page in enumerate(reader.pages,start=1):
    text=page.extract_text()
    pages.append({
        "page":page_number,
        "text":text
    })   