# FastAPI MVC - Gemini AI Boilerplate

A clean and scalable FastAPI project following MVC architecture, integrated with Google Gemini AI.

## 🚀 Features
- FastAPI with MVC Pattern (Routers + Controllers)
- Google Gemini AI Integration
- Secure Environment Management (.env)
- Production-Ready Structure

## 📁 Project Structure
fastapi-mvc/
├── controllers/
│   └── query.py
├── routers/
│   └── ai.py
├── main.py
├── .env.example
├── .gitignore
└── requirements.txt

## 🛠️ Installation

1. Clone the repo:
git clone https://github.com/usmanAISystem/fastapi-mvc.git
cd fastapi-mvc

2. Create virtual environment:
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Setup environment:
Rename .env.example to .env
Add your GENAI_API_KEY in .env

5. Run the server:
uvicorn main:app --reload

## 🔗 API Endpoints
- GET / - Welcome message
- POST /ai/query - Gemini AI query

## 👨‍💻 Author
Usman - AI Systems

Built with ❤️ using FastAPI & Gemini