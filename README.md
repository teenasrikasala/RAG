# College Policy RAG Chatbot

This is a RAG-based chatbot that answers questions about college policies using PDF documents. I built this project to understand how document search and Large Language Models (LLMs) work together.

The chatbot searches for relevant information in the policy documents and uses Llama 3 to generate an answer based on the retrieved content.

## Features

- Ask questions about college policies in normal language.
- Read and process policy PDFs.
- Split document text into smaller chunks.
- Find relevant information using semantic search.
- Generate answers using Llama 3.
- Return a fallback response when relevant information is not found.
- Simple web interface to interact with the chatbot.

## Technologies Used

- Python
- Flask
- HTML, CSS and JavaScript
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS for vector search
- Ollama with Llama 3
- PyPDF for extracting text from PDFs

## How It Works

1. The chatbot extracts text from the policy PDFs.
2. The text is divided into smaller chunks.
3. Sentence Transformers converts the chunks into embeddings.
4. FAISS searches for chunks relevant to the user's question.
5. The retrieved information is passed to Llama 3.
6. Llama 3 generates an answer using the provided context.
7. If the retrieved information is not relevant enough, the chatbot returns a fallback response.

## Project Structure

```text
RAG/
├── app.py
├── requirements.txt
├── README.md
├── data/
├── src/
├── templates/
└── static/
```

- `app.py` – Runs the Flask application.
- `data/` – Contains the college policy PDF files.
- `src/` – Contains the code for PDF extraction, chunking, embeddings, retrieval and LLM integration.
- `templates/` – Contains the HTML page.
- `static/` – Contains the CSS and JavaScript files.
- `requirements.txt` – Lists the Python dependencies.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/teenasrikasala/RAG.git
cd RAG
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Download Ollama from https://ollama.com/download.

Download the Llama 3 model:

```bash
ollama pull llama3
```

Make sure Ollama is running on your computer.

### 5. Start the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Current Status

The project runs locally using Flask and Ollama. It uses the policy PDFs as its knowledge source and FAISS for retrieving relevant information.

## Future Improvements

- Improve answer accuracy and retrieval quality.
- Show document names and page numbers with answers.
- Test more questions, including questions outside the policy documents.
- Improve the chatbot's ability to say "I don't know" when the documents don't contain the answer.
- Explore deployment options for making the chatbot available online.

## Author

**Teenasri Kasala**

GitHub: https://github.com/teenasrikasala

LinkedIn: https://www.linkedin.com/in/teena-sri-kasala-62973532b/
