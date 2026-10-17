import requests
from faiss_search import retrieve
def ans_que(question):
    results=retrieve(question)
    if not results:
        print("answer regarding to your question is not exist")
        return
    if results[0]["similarity_score"]<0.35:
        print("I could not find relevant answer to your question")
        return
    context="\n\n".join(f"page {item["page"]}:\n{item["text"]}" for item in results)
    prompt=f"""
           you are a question answer assisstance
           Rules to be followed
           1.only use the document to retrieve answers
           2.don't use information out of document
           3.If the answer is missing then reply like this
           "I could not find relevant answer to your question"
           DOCUMENT_CONTEXT:
           {context}
           QUESTION:
           {question}
           """
    try:
        response=requests.post("http://localhost:11434/api/generate",
            json={
               "model":"llama3",
                "prompt":prompt,
                "stream":False,
                           },timeout=180)   
        response.raise_for_status()
        answer=response.json()["response"]
        print(answer)
        for item in results:
            print(f"page:{item["page"]}") 
            print(f"chunk:{item["chunk_id"]}")
            print(f"similarity score:{item["similarity_score"]:.4f}")
    except requests.exceptions.RequestException as error:
        print("ollama is not responding:",error)    
if __name__=="__main__":
    while True:
        q=input("ask question or Q to quit:")
        if q.lower()=='q':
            break
        if q:
           ans_que(q)        