"""Module for handling interactions with the Gemini model."""

from google import genai
from google.genai.types import GenerateContentConfig, Type, Part, Schema
from .config import MODEL_NAME, TEMPERATURE, MAX_TOKENS
import json

def initialize_client(api_key: str):
    """Initialize the Gemini model with configuration settings."""
    if not api_key:
        raise ValueError("API key is required to generate recipes")
    client = genai.Client(api_key=api_key)
    return client

def generate_recipe(ingredients: str, api_key: str) -> dict:
    """
    Generate recipe suggestions based on provided ingredients.
    
    Args:
        ingredients (str): Comma-separated list of ingredients
        api_key (str): Gemini API key for authentication
    
    Returns:
        dict: Dictionary containing recipe details including:
            - title: Recipe title
            - ingredients: List of required ingredients
            - instructions: Step-by-step cooking instructions
            - cooking_time: Estimated cooking time
    """
    client = initialize_client(api_key)

    system_prompt = (
        "You are a world-class culinary AI assistant. Your task is to generate one "
        "creative and easy-to-follow recipe based on the user's available ingredients "
        "and preferred cuisine. You must return the response as a single, valid JSON object, "
        "strictly following the provided schema. Do not include any text outside the JSON block."
    )

    schema = Schema(
        type=Type.OBJECT,
        properties={
            "title": Schema(type=Type.STRING, description="A creative and funny name for the dish."),
            "prep_time": Schema(type=Type.STRING, description="The time required to get things ready for the dish."),
            "cook_time": Schema(type=Type.STRING, description="The time required to actually cook the dish."),
            "ingredients": Schema(type=Type.ARRAY, items=Schema(type=Type.STRING), description="A list of ingredients with quantities required for the dish."),
            "calories": Schema(type=Type.STRING, description="The calorific value of the dish in terms of kcals and no other text. (eg. 800 kcals)"),
            "instructions": Schema(type=Type.ARRAY, items=Schema(type=Type.STRING), description="A concise, numbered, Step-by-step instructions to prepare the dish.(use glyphicons as necessary)"),
            "yputube_link": Schema(type=Type.STRING, description="A URL link to a YouTube video demonstrating the preparation of the dish. (if available)"),
        },
        required=["title", "ingredients", "instructions"],
    )

    # Define the user prompt
    user_prompt = (
        f"Generate a recipe using these ingredients: {ingredients}. "
        f"If necessary, assume common pantry staples "
        f"(salt, pepper, oil, water)."
    )

    config = GenerateContentConfig(
        system_instruction=system_prompt,
        response_schema=schema,
        response_mime_type='application/json'
    )
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_prompt,
        config=config,
        # temperature=TEMPERATURE,
        # max_output_tokens=MAX_TOKENS
    )
    
    return json.loads(response.text)  # This will return the JSON-formatted recipe
