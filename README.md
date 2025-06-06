# LangChain + Ollama + LLaMA 3 Chatbot Demo

This is a lightweight AI assistant demo built using [LangChain](https://github.com/langchain-ai/langchain), [Ollama](https://github.com/ollama/ollama), and [Streamlit](https://streamlit.io/). It uses the locally running LLaMA 3 model served via Ollama to answer user queries in a friendly UI.

---

## 🔧 Features

- Local LLM inference with Ollama (LLaMA 3)
- Prompt templating using LangChain
- User interface built with Streamlit
- Supports easy question answering format

---

## 🚀 How to Run

### 1. Prerequisites
- Python 3.10+
- Ollama installed and model pulled:
  \`\`\`
  ollama pull llama3
  \`\`\`

### 2. Setup
\`\`\`
git clone https://github.com/BhagyeshPatil2004/langchain-ollama-demo.git
cd langchain-ollama-demo
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
\`\`\`

### 3. Run the App
\`\`\`
streamlit run ollama.py
\`\`\`

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure
\`\`\`
├── ollama.py        # Streamlit + LangChain + Ollama integration

├── .env             # Optional environment variables

├── requirements.txt # Required dependencies (Optional)
\`\`\`

---

## 📌 Notes
- Ensure Ollama is running and the \`llama3\` model is downloaded before running the app.
- No OpenAI API is required for this demo, it's 100% local.

---

## 🧑‍💻 Author
[Bhagyesh Patil](https://github.com/BhagyeshPatil2004)

---
