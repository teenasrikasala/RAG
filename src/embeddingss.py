from sentence_transformers import SentenceTransformer
from chunker import chunks
model=SentenceTransformer('all-MiniLM-L6-v2')
texts=[]
for chunk in chunks:
    texts.append(chunk['text'])
embeddings=model.encode(texts)    
for i,embeddings in enumerate(embeddings):
    print(chunks[i]['chunk_id'])
    print('vector length:',len(embeddings))
    print(embeddings)
    print('-'*50)