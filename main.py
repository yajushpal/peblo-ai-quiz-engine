from fastapi import FastAPI, UploadFile
from app.pdf_parser import extract_text_from_pdf, chunk_text
from app.quiz_generator import generate_questions
from app.database import SessionLocal, init_db
from app.models import Question

app = FastAPI()

init_db()


@app.get("/")
def home():
    return {"message": "Peblo AI Quiz Engine Running"}


@app.post("/ingest")
async def ingest_pdf(file: UploadFile):

    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(path)

    chunks = chunk_text(text)

    return {
        "chunks_created": len(chunks),
        "sample_chunks": chunks[:3]
    }


@app.post("/generate-quiz")
def generate_quiz():

    chunk = "A triangle has three sides."

    questions = generate_questions(chunk)

    db = SessionLocal()

    for q in questions:

        question = Question(
            question=q["question"],
            type=q["type"],
            options=q["options"],
            answer=q["answer"],
            difficulty=q["difficulty"],
            source_chunk=chunk
        )

        db.add(question)

    db.commit()

    return questions


@app.get("/quiz")
def get_quiz():

    db = SessionLocal()

    questions = db.query(Question).all()

    result = []

    for q in questions:
        result.append({
            "id": q.id,
            "question": q.question,
            "options": q.options
        })

    return result


@app.post("/submit-answer")
def submit_answer(question_id: int, answer: str):

    db = SessionLocal()

    question = db.query(Question).get(question_id)

    correct = answer == question.answer

    return {
        "correct": correct,
        "difficulty_adjustment": "increase" if correct else "decrease"
    }