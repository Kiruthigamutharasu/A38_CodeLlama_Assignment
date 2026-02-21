# PART 2 — TASK 4
# Streamlit Code Assistant using CodeLlama + Ollama

import streamlit as st
import ollama

# ---- Model Call ----
def ask_codellama(prompt):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# ---- UI ----
st.title("💻 AI Coding Assistant (CodeLlama + Ollama)")

task = st.selectbox(
    "Select Task",
    ["Generate Code", "Explain Code", "Debug Code", "Optimize Code"]
)

user_input = st.text_area("Enter your code or prompt")

if st.button("Run Assistant"):

    if task == "Generate Code":
        prompt = f"Generate Python code for:\n{user_input}"

    elif task == "Explain Code":
        prompt = f"Explain this code clearly:\n{user_input}"

    elif task == "Debug Code":
        prompt = f"Fix bugs and give corrected code:\n{user_input}"

    elif task == "Optimize Code":
        prompt = f"Optimize this code:\n{user_input}"

    output = ask_codellama(prompt)

    st.subheader("CodeLlama Output")
    st.code(output, language="python")