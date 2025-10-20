"""Configuration settings for the GenAI model."""

import os

# API configurations
try:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
except:
    GEMINI_API_KEY = None

# Model configurations
MODEL_NAME = "gemini-2.5-flash-lite"  # Using Gemini Pro model
TEMPERATURE = 0.7  # Controls randomness in generation
MAX_TOKENS = 1024  # Maximum length of generated response
