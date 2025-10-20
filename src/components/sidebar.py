import streamlit as st

def render_sidebar():
    """Render the sidebar with API key configuration."""
    with st.sidebar:
        st.title("Recipe App")
        st.markdown("---")
        
        # API Key input section
        api_key = st.text_input(
            "Enter your Gemini API Key",
            type="password",
            help="Get your API key from Google AI Studio (https://makersuite.google.com/app/apikey)",
            key="gemini_api_key"
        )
        
        if not api_key:
            st.warning("⚠️ Please enter your Gemini API key to generate recipes")
        else:
            st.success("✅ API key set successfully!")
        
        st.markdown("---")
        st.markdown("""
            ### How to get an API Key:
            1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
            2. Sign in with your Google account
            3. Click 'Create API Key'
            4. Copy and paste the key here
        """)
    
    return api_key
