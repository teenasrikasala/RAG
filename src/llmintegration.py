import requests
from src.faiss_search import retrieve
def ans_que(question):
    results=retrieve(question)
    if not results:
        return f"I could not find relevant answer to your question"
    if results[0]["similarity_score"]<0.35:
        print()
        return f"I could not find relevant answer to your question"
    context="\n\n".join(f"page {item["page"]}:\n{item["text"]}" for item in results)
    prompt=f"""
           you are a question answer assisstance
           Rules to be followed
           1.only use the document to retrieve answers
           2.don't use information out of document
           3. keep the answer clear and relevant to the question asked
           4.don't end answer with broken sentence,complete the answer in full sentence
           5.no need to mention the source ,page number or chunk id in the answer
         
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
        return answer    
    except requests.exceptions.RequestException as error:
        return f"ollama is not responding: {error}"    
if __name__=="__main__":
    while True:
        q=input("ask question or Q to quit:")
        if q.lower()=='q':
            break
        if q:
           ans_que(q)        