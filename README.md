STAN – Conversational Chatbot Backend

This project is a backend chatbot application developed as part of a company assignment.
The objective of this project is to demonstrate backend development skills, AI integration, and clean system design.

The chatbot is named Stan and is designed to behave like a friendly, emotionally aware conversational companion rather than a typical robotic chatbot.

Project Overview

The application is built using FastAPI and integrates with Google Gemini to generate responses.
It exposes a REST API that allows users to send messages and receive replies from the chatbot.

The focus of this project is on:

Backend architecture

Prompt engineering

AI integration

Error handling and reliability

No frontend interface is included, as the goal is to showcase backend functionality.

Features

FastAPI-based REST API

Google Gemini integration for AI-generated responses

System prompt to control chatbot personality and safety behavior

Lightweight user memory (for example, remembering a user’s name)

Emotion-aware fallback responses when the AI service is unavailable

Secure handling of sensitive information using environment variables

Clean and modular project structure

How the Chatbot Works

The chatbot exposes a single main endpoint:

POST /chat


Each request contains:

user_id – used to identify the user and maintain memory

message – the user’s input message

For every request, the backend:

Reads the user message

Retrieves any stored user memory

Builds a prompt using a fixed system prompt and memory context

Sends the prompt to Gemini to generate a response

If the Gemini API is unavailable or quota is exceeded, the system falls back to predefined, emotionally safe responses.
This ensures the application remains stable and responsive at all times.

Memory Design

The chatbot uses a simple in-memory storage mechanism to store user information.
Only information explicitly provided by the user is stored.

Memory is:

Used carefully and transparently

Never assumed or fabricated

Injected into the prompt only when available

This keeps the system easy to understand and extend.

Error Handling and Reliability

All AI calls are wrapped in proper error handling.
If an error occurs while communicating with the Gemini API, the chatbot still responds politely using fallback logic.

This design prevents crashes and improves user experience, reflecting real-world backend best practices.

Project Structure
stanAI/

main.py        
prompts.py   
memory.py      
README.md

.gitignore

__init__.py


Sensitive files such as .env and the virtual environment are excluded from the repository for security reasons.

Setup Instructions

Clone the repository

Create and activate a Python virtual environment

Install required dependencies

Create a .env file and add your Gemini API key

Run the application using Uvicorn

Once the server is running, the chatbot can be tested using Postman or similar API testing tools.

API Usage Example

Request:

{
  "user_id": "u1",
  "message": "My name is Dinesh"
}


Response:

{
  "reply": "Hey Dinesh 🙂 How can I help you today?"
}

Limitations and Future Improvements

User memory is stored in-memory and resets when the server restarts

No frontend interface is included

The project can be extended with database storage, authentication, or a frontend UI

Conclusion

This project demonstrates how a conversational AI backend can be implemented with a clean structure, controlled AI behavior, and reliable error handling.
The emphasis is on clarity, stability, and explainability rather than complexity.
