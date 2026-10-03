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
for page in pages:
    print(f"\npage:{page['page']}:")
    print(page["text"])    
print(type(pages))
print(type(pages[0]))    