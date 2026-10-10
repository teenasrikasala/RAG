import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from chunker import chunks
model=SentenceTransformer('all-MiniLM-L6-v2')
texts=[chunk['text'] for chunk in chunks]
chunk_embeddings=model.encode(texts,normalize_embeddings=True)
chunk_embedding_faiss_compaitable=np.asarray(chunk_embeddings,dtype='float32')
diemensions=chunk_embedding_faiss_compaitable.shape[1]
index=faiss.IndexFlatIP(diemensions)
index.add(chunk_embedding_faiss_compaitable)
print("total no.of queries:",index.ntotal)
q=input("\nany queriesss about company policies:")
print(q)
q_embeddings=model.encode([q],normalize_embeddings=True)
q_embedding_faiss_compaitable=np.asarray(q_embeddings,dtype='float32')
k=min(3,len(chunks))
scores,indices=index.search(q_embedding_faiss_compaitable,k)
for rank,(scores,idx) in enumerate(zip(scores[0],indices[0]),start=1):
    chunk=chunks[int(idx)]
    print(f"Rank:{rank}")
    print("chunk_id:",chunk['chunk_id'])
    print("page:",chunk['page'])
    print("similarity score:",round(float(scores),4))
    print("text:",chunk['text'])

