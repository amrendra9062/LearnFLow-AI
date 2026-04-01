import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Gemini 2.5 Flash model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_summary(text):
    prompt = f"""
Summarize the following content into:
- Key points
- Important concepts
- Short structured notes

Content:
{text[:3000]}
"""

    response = model.generate_content(prompt)
    return response.text if response.text else "No summary generated."


def generate_quiz(text):
    prompt = f"""
Create 5 MCQ questions from the content below.

Each question must include:
- Question
- 4 options (A, B, C, D)
- Correct answer
- Explanation

Content:
{text[:3000]}
"""

    response = model.generate_content(prompt)
    return response.text if response.text else "No quiz generated."


def chatbot_response(question, context):
    prompt = f"""
You are a helpful AI tutor.

Context:
{context}

User Question:
{question}

Give a clear, simple explanation with examples.
"""

    response = model.generate_content(prompt)
    return response.text if response.text else "No response generated."