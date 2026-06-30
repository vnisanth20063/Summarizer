# 🎓 Anna University AI Answer Generator & Integrated AI Assistant

An AI-powered academic assistant built using **Streamlit, LangChain, and Groq LLM** that generates high-quality university exam answers from uploaded documents/images and provides an integrated AI assistant for asking questions based on the generated content.

This project uses **Prompt Engineering** to create answers according to **Anna University exam writing style** with proper structure, headings, technical points, advantages, applications, and conclusions.

---

# 🚀 Features

## 📄 AI Document Answer Generator

- Upload academic documents/files
- Analyze the uploaded content using AI
- Generate answers based on document information
- Creates structured university-level answers
- Avoids irrelevant information

---

# 🎯 Mark-Based Answer Generation

The AI automatically changes the answer format based on the mark requirement.

## 2 Marks

Generates:

- Short definition
- Direct answer
- Important points
- Technical keywords

---

## 5 Marks

Generates:

- Introduction
- Explanation of concepts
- Important points
- Examples (if required)

---

## 10 Marks

Generates:

- Detailed explanation
- Multiple headings
- Step-by-step explanation
- Advantages and disadvantages
- Applications

---

## 13/15 Marks

Generates a complete university exam answer:

Structure:

1. Title
2. Introduction
3. Definition / Meaning
4. Detailed Explanation
5. Working / Architecture / Process
6. Key Points
7. Advantages
8. Applications
9. Conclusion

---

# 🤖 Integrated AI Assistant

After generating an answer, users can interact with the AI.

Capabilities:

- Ask questions from generated content
- Get detailed explanations
- Provides structured answers
- Uses previous generated content as context
- Avoids unrelated answers

---


---

# 🛠️ Technologies Used

## Programming Language

- Python

## Frontend

- Streamlit

## AI Framework

- LangChain

## Large Language Model

- Groq API
- Llama 3.1 8B Instant

## Environment Management

- Python-dotenv

---

# step 1:📂 Project Structure
│
├── app.py
│
├── .env
│
├── requirements.txt
│
├── .gitignore
│
└── README.md


## Step 2: Install Required Packages
pip install -r requirements.txt

## Step 3: Create Environment File
.env

Add your Groq API key:

GROQ_API_KEY=your_api_key_here


## Step 4: Run Application

Execute:

streamlit run app.py