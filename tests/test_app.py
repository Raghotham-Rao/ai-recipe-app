import streamlit as st
from src.app import main

def test_main():
    """Test the main entry point of the Streamlit application."""
    # Run the main function
    main()

    # Check if the title is displayed
    assert st.session_state.get('title') == "Your App Title"

def test_sidebar():
    """Test the sidebar functionality."""
    from src.components.sidebar import render_sidebar

    # Render the sidebar
    render_sidebar()

    # Check if sidebar elements are present
    assert 'Home' in st.sidebar.text_area('Navigation')