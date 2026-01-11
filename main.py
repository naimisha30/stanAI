from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from google import genai  # Gemini SDK

from prompts import SYSTEM_PROMPT
from memory import get_user_profile, update_user_profile

# --------------------------------------------------
# App & config
# --------------------------------------------------

load_dotenv()

app = FastAPI(title="STAN Chatbot")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# --------------------------------------------------
# Request model
# --------------------------------------------------

class ChatRequest(BaseModel):
    user_id: str
    message: str


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def health():
    return {"status": "STAN is alive"}


# --------------------------------------------------
# Chat endpoint
# --------------------------------------------------

@app.post("/chat")
def chat(req: ChatRequest):
    user_id = req.user_id
    message = req.message.strip()
    lowered = message.lower()

    # -------------------------
    # Get memory
    # -------------------------
    profile = get_user_profile(user_id)

    # -------------------------
    # Memory extraction
    # -------------------------
    if "my name is" in lowered:
        name = lowered.split("my name is")[-1].strip()
        update_user_profile(user_id, "name", name)

    # -------------------------
    # Build memory context
    # -------------------------
    memory_context = ""
    if "name" in profile:
        memory_context = f"The user's name is {profile['name']}."

    # -------------------------
    # Prompt
    # -------------------------
    prompt = f"""
{SYSTEM_PROMPT}

Memory:
{memory_context}

User says:
{message}
"""

    # -------------------------
    # Try Gemini (LLM)
    # -------------------------
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        reply = response.text.strip()

    # -------------------------
    # Smart emotion-based fallback
    # -------------------------
    except Exception as e:
        print("Gemini error:", e)

    # Emotion-first handling
    if any(word in lowered for word in ["sad", "lonely", "down", "upset"]):
        reply = (
            "I’m really sorry you’re feeling this way 💙 "
            "I’m here with you. Want to talk about what’s making you feel sad?"
        )

    elif any(word in lowered for word in ["stress", "anxious", "worried", "pressure"]):
        reply = (
            "That sounds overwhelming 😔 "
            "Take a moment — I’m listening. What’s been stressing you out?"
        )

    elif any(word in lowered for word in ["happy", "excited", "good", "great"]):
        reply = "That’s nice to hear 😊 What made you feel that way?"

    elif any(word in lowered for word in ["hi", "hello", "hey"]):
        reply = "Hey! 😊 I’m glad you reached out. What’s on your mind?"

    elif "how are you" in lowered:
        reply = "I’m doing okay 🙂 Thanks for asking. How are you feeling today?"

    else:
        reply = "I’m listening 🙂 Tell me a little more."

        

    return {"reply": reply}
