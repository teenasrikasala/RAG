from pdf_extractor import pages
chunk_size=500
chunks=[]
for page in pages:
    text=page['text']
    page_number=page['page']
    chunk_number=1
    for start in range(0,len(text),chunk_size):
        chunk_text=text[start:start+chunk_size]
        chunks.append({
             'text':chunk_text,
             'page':page_number,
             'chunk_id':f'page{page_number}_chunk{chunk_number}'
        })
        chunk_number+=1   