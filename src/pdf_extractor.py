from pypdf import PdfReader
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/"data"
path=sorted(DATA_DIR.rglob("*.pdf"))
pages=[]
for p in path:
    reader=PdfReader(p)
    for page_number,page in enumerate(reader.pages,start=1):
      text=page.extract_text()
      pages.append({
        "source":p.name,
        "page":page_number,
        "text":text
    })   