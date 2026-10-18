import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from src.chunker import chunks
model=SentenceTransformer('all-MiniLM-L6-v2')
texts=[chunk['text'] for chunk in chunks]
chunk_embeddings=model.encode(texts,normalize_embeddings=True)
chunk_embedding_faiss_compaitable=np.asarray(chunk_embeddings,dtype='float32')
diemensions=chunk_embedding_faiss_compaitable.shape[1]
index=faiss.IndexFlatIP(diemensions)
index.add(chunk_embedding_faiss_compaitable)
print("total no.of queries:",index.ntotal)
def retrieve(q,k=3):
      q_embeddings=model.encode([q],normalize_embeddings=True)
      q_embedding_faiss_compaitable=np.asarray(q_embeddings,dtype='float32')
      k=min(3,len(chunks))
      scores,indices=index.search(q_embedding_faiss_compaitable,k)
      results=[]
      for score,idx in zip(scores[0],indices[0]):
            chunk=chunks[int(idx)]
            results.append({
          "source":chunk["source"],       
          "chunk_id":chunk["chunk_id"],
          "source":chunk["source"],       
          "page":chunk["page"],
          "similarity_score":round(float(score),4),
          "text":chunk["text"]
             })
      return results

if __name__=="__main__":
    while True:    
          q=input("\nany queriesss about company policies or Q for quit:")
          if q.lower()=="q":
               break
          result=retrieve(q)
         
