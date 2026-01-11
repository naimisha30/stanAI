"""
Lightweight in-memory storage for user memory.

This module handles:
- Structured user profile memory (name, interests, preferences)
- Conversation summary memory

Note:
- This is intentionally in-memory for simplicity.
- Can be easily replaced with a database or Redis in production.
"""

# In-memory store
user_memory: dict[str, dict] = {}


# -------- User profile memory --------

def get_user_profile(user_id: str) -> dict:
    """
    Retrieve stored profile information for a user.
    """
    return user_memory.get(user_id, {})


def update_user_profile(user_id: str, key: str, value: str) -> None:
    """
    Update a single field in the user's profile memory.
    """
    user_memory.setdefault(user_id, {})
    user_memory[user_id][key] = value


# -------- Conversation summary memory --------

def update_summary(user_id: str, summary: str) -> None:
    """
    Store or update a lightweight conversation summary for the user.
    """
    user_memory.setdefault(user_id, {})
    user_memory[user_id]["summary"] = summary


def get_summary(user_id: str) -> str:
    """
    Retrieve the conversation summary for the user, if available.
    """
    return user_memory.get(user_id, {}).get("summary", "")
