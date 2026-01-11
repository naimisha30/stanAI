STAN – Emotion-Aware Conversational Chatbot Backend

Project Overview
This project is a backend conversational chatbot named STAN, developed using FastAPI and integrated with Google Gemini LLM.
The goal of the project is to demonstrate how a modern chatbot system can be built with clean backend architecture, prompt engineering, basic long-term memory, emotion-aware interaction, and graceful error handling.
The focus of this assignment is not on UI or deployment, but on backend design, AI integration, and system reliability, which are important in real-world applications.

Problem Statement
Traditional chatbots often respond in a robotic way, forget previous user information, or fail completely when an external AI service is unavailable.
This project aims to solve these issues by:
Creating a chatbot that can converse naturally
Remember basic user-provided information
spond empathetically to emotions
Continue working even when the AI API quota is exhausted
System Architecture
The system is designed in a modular and simple architecture with the following components:
FastAPI Backend
Handles HTTP requests and responses using REST APIs.
Prompt System
Defines the chatbot’s personality, tone, safety rules, and behavior.
Memory Module
Stores lightweight user memory such as name and conversation context.
LLM Integration (Gemini)
Generates intelligent responses when the API is available.
Fallback Logic
Ensures the chatbot responds meaningfully even if the AI API fails.
File Structure Explanation

main.py
This is the core file of the project. It defines:
The /chat API endpoint
Request validation using Pydantic
Memory extraction logic
Prompt construction
Gemini API call
Emotion-based fallback responses

prompts.py
Contains the system prompt that defines:
Chatbot identity (Stan)
Personality and tone
Safety and honesty rules
Memory usage behavior
This ensures consistent, human-like responses across all interactions.

memory.py
Manages simple in-memory storage for:
User profile information (example: name)
Conversation context
Only information explicitly shared by the user is stored to avoid hallucination and privacy issues.

.env.example
Shows how environment variables are configured without exposing sensitive API keys.
Chat Flow Explanation
The user sends a message to the /chat endpoint.
The backend checks if the message contains memory-related information (e.g., “my name is…”).
If found, the information is stored in memory.
Stored memory is injected into the prompt for personalization.
The prompt is sent to the Gemini LLM to generate a response.
If the LLM API fails (quota or error), the system switches to a smart fallback mechanism.

Emotion Handling Design
To improve interaction quality, the chatbot includes basic emotion detection when the AI API is unavailab
The system prioritizes emotions over greetings, for example:
“hello i am sad” → empathetic response
“i am stressed about exams” → supportive response
“i am happy today” → positive reinforcement

This approach is:
Lightweight
Explainable
Reliable for a student-level system

Error Handling & Reliability
All calls to the Gemini API are wrapped in a try-except block.
If the API quota is exceeded or an error occurs:
The backend does not crash
A meaningful response is still returned
The user experience remains smooth
This demonstrates graceful degradation, which is a real-world backend best practice.
Security Considerations
API keys are stored using environment variables
.env files are excluded from version control
A .env.example file is provided for configuration guidance
This ensures secure handling of sensitive credentials.

Limitations
Memory is stored in-memory and resets on server restart
No frontend UI is implemented
No database integration (intentional for simplicity)
These limitations were chosen deliberately to keep the project focused, clean, and easy to evaluate.

Future Enhancements
The system can be extended by:
Adding a database for persistent memory
Implementing user authentication
Adding a frontend interface
Enhancing emotion detection with ML models

Conclusion
This project demonstrates:
Backend API development using FastAPI
Integration of a large language model
Prompt engineering for controlled behavior

Basic memory handling

Emotion-aware interaction

Robust error handling and fallback logic

Overall, the project reflects practical system design thinking, suitable for academic evaluation and real-world backend development scenarios.
