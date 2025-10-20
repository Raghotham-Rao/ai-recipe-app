"""Initialize the genai package."""

from .model import generate_recipe
from .config import GEMINI_API_KEY

__all__ = ['generate_recipe', 'GEMINI_API_KEY']
