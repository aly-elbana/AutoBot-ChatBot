"""
Configuration module for the AI ChatBot application.
"""
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Configuration
def get_llm():
    """Initialize and return the LLM instance."""
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Model that supports images (multimodal)
        google_api_key=GEMINI_API_KEY,
        temperature=0.5
    )
