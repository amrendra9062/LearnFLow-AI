 LearnFlow AI

An intelligent AI-powered learning assistant that transforms any content into structured knowledge, interactive quizzes, and personalized learning experiences.

 Overview

LearnFlow AI allows users to upload or link content (PDFs, videos, etc.), automatically extracts meaningful information, generates summaries, creates quizzes, and provides a chatbot for deeper understanding.

It delivers a complete end-to-end learning workflow:

Content → Understanding → Practice → Exploration

Features
Multi-Content Input
Upload PDFs
Add YouTube links
(Extensible to audio/images)
Smart Content Understanding
Structured summaries
Key concepts extraction
Clean, readable notes
Interactive Quiz Generation
Auto-generated MCQs
Answers with explanations
Helps reinforce learning
AI Chatbot
Ask questions about the content
Get explanations with context
Explore topics in depth
Unified Learning Experience
Everything in one place
Simple and intuitive UI
Real-world usability
Tech Stack
Frontend
React.js
Axios
CSS (custom styling)
Backend
FastAPI
Python
AI Engine
Google Gemini API (Gemini 2.5 Flash)
Content Processing
PyPDF (PDF parsing)
YouTube Transcript API
Project Structure
hackathon/
│
├── backend/
│   ├── main.py
│   ├── utils/
│   │   ├── ai_engine.py
│   │   ├── pdf_parser.py
│   │   ├── youtube_parser.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Upload.js
│   │   │   ├── Summary.js
│   │   │   ├── Quiz.js
│   │   │   ├── Chatbot.js
Setup Instructions
Clone the repository
git clone <your-repo-url>
cd hackathon
Backend Setup
cd backend

python3.11 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn google-generativeai pypdf youtube-transcript-api python-multipart
Set API Key
export GOOGLE_API_KEY="your_gemini_api_key"
Run Backend
uvicorn main:app --reload

Backend runs on:

http://localhost:8000
Frontend Setup
cd frontend

npm install
npm start

Frontend runs on:

http://localhost:3000
How to Use
Open the web app
Upload a PDF OR enter a YouTube link
View:
Summary
Quiz
Use chatbot to ask questions
Learn interactively LearnFlow AI

