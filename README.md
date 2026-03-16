# peblo-ai-quiz-engine

# Peblo AI Backend Engineer Challenge

## Overview
This project implements a mini content ingestion and adaptive quiz generation engine.

The system ingests educational PDFs, extracts content, generates quiz questions, and exposes APIs to retrieve quizzes and submit student answers.

---

## System Architecture

PDF Input  
↓  
Text Extraction (pdfplumber)  
↓  
Content Chunking  
↓  
Quiz Generation  
↓  
SQLite Database  
↓  
FastAPI Backend APIs  
↓  
Adaptive Difficulty Logic

---

## Tech Stack

Backend: FastAPI  
Language: Python  
Database: SQLite  
PDF Processing: pdfplumber  

---

## Project Structure
 app/
main.py
pdf_parser.py
quiz_generator.py
models.py
database.py

README.md
requirements.txt
.env.example


---

## API Endpoints

POST /ingest  
Upload a PDF and extract chunks.

POST /generate-quiz  
Generate quiz questions.

GET /quiz  
Retrieve stored quiz questions.

POST /submit-answer  
Submit a student answer.

---

## Adaptive Difficulty Logic

Correct answer → increase difficulty  
Incorrect answer → decrease difficulty
