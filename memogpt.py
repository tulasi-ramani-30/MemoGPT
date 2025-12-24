import json
import os
from google import genai
import streamlit as st

st.title("MemoGPT🤖")
client = genai.Client(
    api_key="..............."
)
path = "history.json"

if os.path.exists(path):
    with open(path, "r") as file:
        history = json.load(file)
else:
    history = []

def answer_query(question, history):
    conversation = ""
    for entry in history:
        conversation += f"User: {entry['question']}\n"
        conversation += f"AI: {entry['answer']}\n"

    conversation += f"User: {question}\nAI:"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=conversation
    )

    return response.text

user_input = st.text_area("Ask MemoGPT: ")
ai_response = answer_query(user_input, history)
if st.button("Enter"):
    with st.spinner("Processing... ⏳"):
        st.write(f"\nAI: {ai_response}")
    

history.append({
    "question": user_input,
    "answer": ai_response
})

with open(path, "w") as file:
    json.dump(history, file, indent=4)



