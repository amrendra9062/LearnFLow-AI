from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from utils.pdf_parser import extract_pdf_text
from utils.youtube_parser import get_youtube_transcript
from utils.ai_engine import generate_summary, generate_quiz, chatbot_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # IMPORTANT (not *)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        text = extract_pdf_text(file)
        summary = generate_summary(text)
        quiz = generate_quiz(text)

        return {
            "summary": summary,
            "quiz": quiz
        }
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}

@app.post("/youtube")
async def youtube(url: dict):
    transcript = get_youtube_transcript(url["url"])
    summary = generate_summary(transcript)
    quiz = generate_quiz(transcript)

    return {
        "summary": summary,
        "quiz": quiz
    }

@app.post("/chat")
async def chat(data: dict):
    try:
        question = data.get("question", "")
        context = data.get("context", "")

        if not question:
            return {"answer": "Please ask a question."}

        response = chatbot_response(question, context)

        return {"answer": response}

    except Exception as e:
        print("CHAT ERROR:", e)
        return {"answer": f"Error: {str(e)}"}