import streamlit as st
from components.sidebar import render_sidebar
from genai.model import generate_recipe

def main():
    # Get API key from sidebar
    api_key = render_sidebar()
    
    st.title("Recipe App")
    st.write("""
        Welcome to the Recipe App! This application helps you discover delicious recipes based on the ingredients you have.
        
        To get started:
        1. Enter your Gemini API key in the sidebar (Get it from Google AI Studio - https://makersuite.google.com/app/apikey)
        2. Enter your available ingredients in the text input field below
        3. Let the app suggest a perfect recipe for you!
        
        The app will analyze your ingredients and provide you with a detailed recipe including preparation time, 
        cooking instructions, and even a video demonstration when available.
    """)
    
    # Add text input for ingredients
    ingredients = st.text_input(
        "Enter your ingredients",
        placeholder="Example: chicken, rice, tomatoes, onions (comma separated)",
        disabled=not api_key
    )
    
    # Generate and display recipe when ingredients are provided
    if ingredients:
        st.markdown("---")
        with st.spinner("Generating your recipe..."):
            try:
                recipe = generate_recipe(ingredients, api_key)
                
                # Display recipe in a nice format
                st.header(f'🍽️ {recipe["title"]}')
                
                # Display prep time, cook time, and calories in columns
                col1, col2, col3 = st.columns(3)
                if "prep_time" in recipe:
                    col1.metric("⏲️ Prep Time", recipe["prep_time"])
                if "cook_time" in recipe:
                    col2.metric("🍳 Cook Time", recipe["cook_time"])
                if "calories" in recipe:
                    col3.metric("🔥 Calories", recipe["calories"])
                
                # Display image if available
                if "image_url" in recipe and recipe["image_url"]:
                    st.image(recipe["image_url"], caption="Recipe Image")
                
                # Display ingredients in an expandable section
                with st.expander("📝 Ingredients", expanded=True):
                    for ingredient in recipe["ingredients"]:
                        st.write(f"• {ingredient}")
                
                # Display instructions in a numbered list
                st.subheader("👩‍🍳 Cooking Instructions")
                for i, step in enumerate(recipe["instructions"], 1):
                    st.write(f"{step}")
                
                # Display YouTube video if available
                if "youtube_url" in recipe and recipe["youtube_url"]:
                    st.markdown("---")
                    st.subheader("📺 Watch How to Make It")
                    st.video(recipe["youtube_url"])
                
            except Exception as e:
                st.error(f"Sorry, there was an error generating your recipe. Please try again.{e}")

if __name__ == "__main__":
    main()