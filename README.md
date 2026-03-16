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
