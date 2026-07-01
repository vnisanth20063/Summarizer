import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
##------------------GETTING API_KEY-----------------------------
Api_key=os.getenv("GROQ_API_KEY")

##-------------------SETTING SESSION STATE TO NONE---------------
if "answer" not in st.session_state:
    st.session_state.answer=" "
if "ans" not in st.session_state:
    st.session_state.ans=" "

##--------------------VALIDATION OF API KEY-----------------------
if Api_key is None:
    st.error("API_KEY MISSING")
    st.stop()

@st.cache_resource
def load_llm():
  return ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.4,
    api_key=Api_key)

llm=load_llm()


tab1,tab2=st.tabs(["Summarizer","Integrated AI"])


#Tab 2 function which pass values to prompt and invoke llm
def get_input(f,mark):
  prompt= f""" You are an expert Anna University academic answer generator.

Your task is to generate high-quality exam answers from the given input document/file content.

The answer must be created based on:
- Question asked
- Mark allocation
- Content available in the uploaded document
- Anna University exam writing style


Instructions:

1. Analyze the uploaded document/file carefully.
2. Extract only relevant information related to the question.
3. Generate the answer according to the given mark requirement.

Mark-based answer length:

2 Marks:
- Give a short definition or direct answer
- Include 2-3 important points

5 Marks:
- Give an introduction
- Explain key concepts
- Provide 4-5 important points
- Add examples if needed

10 Marks:
- Provide a detailed explanation
- Include introduction
- Use multiple headings and subheadings
- Explain concepts step-by-step
- Add examples, diagrams (if applicable), advantages/disadvantages .end with tips

13/15 Marks:
- Write a complete university-level answer
- Include:
  1. Title
  2. Introduction
  3. Definition
  4. Detailed explanation
  5. Working/Architecture/Process (if applicable)
  6. Key points
  7. Advantages
  8. Applications
  9. Conclusion


Answer formatting rules:

Use this structure:

# Title

## Introduction

(brief overview)

## Definition / Meaning

(explain the concept)

## Main Explanation

Use:

### Heading 1
- Point-wise explanation

### Heading 2
- Detailed explanation

### Heading 3
- Important concepts


## Key Points

- Important exam points
- Technical terms
- Keywords expected in university evaluation


## Advantages / Applications
(if applicable)

## Conclusion

(summary)


Important rules:

- Do not give a simple summary.
- Write in an elaborate exam-answer style.
- Use clear headings and subheadings.
- Highlight important keywords.
- Maintain technical accuracy.
- Do not add irrelevant information.
- If information is missing, clearly mention it.
- Make the answer suitable for Anna University evaluation.

Input:

file:
{f}


Marks:
{mark}





Generate the final answer."""
  response=llm.invoke(prompt)
  return response.content



def questions(summary,questi_on):
    prompt=f"""You are an intelligent AI assistant.

You are given a generated explanation/summary from a document.

Your task:
- Answer the user's question using only the provided content.
- Explain the answer clearly and in detail.
- If the question requires more explanation, provide examples.
- Keep the answer structured with proper titles, headings, and bullet points when needed.
- Do not give unrelated information.
- If the answer is not available in the provided content, clearly say that it is not mentioned.

Generated Content:
{summary}

User Question:
{questi_on}

Provide the final answer:"""
    response=llm.invoke(prompt)
    return response.content


#Tab1 inputs
with tab1:
    f=st.file_uploader(
        "Upload your file")

    mark=st.number_input(
        "Enter the mark",min_value=0,max_value=100)

    button=st.button("Generate Answer")

    if button:
        with st.spinner("Sumarizing......."):
            a=get_input(f,mark)
            st.markdown(a)
            st.session_state.answer=a
if st.session_state:
 st.markdown(st.session_state.answer)

#tab 2
with tab2:

    questi_on=st.text_input("Ask your questions")
    button=st.button("Generate")
    if button:
        with st.spinner("Generating answer...."):
            if st.session_state:
              b=questions(st.session_state,questi_on)
              st.markdown(b)
              st.session_state.ans=b
    
    