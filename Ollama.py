from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("LangChain + Ollama (LLaMA 3) Demo")
input_text = st.text_input("Ask your question:")

if not input_text:
    st.info("Please enter a question above to get started!")
else:
    # Ollama LLM
    llm = Ollama(model="llama3")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"question": input_text})
            st.success("Done!")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")

