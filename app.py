from pathlib import Path
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages


show_pages(
        [
            Page("pages/home.py", "🏠 Home"),
            Page("pages/chatbot.py","💬 Forge Chat"),
            Page("pages/musicgen.py","🎙️ Generate Songs")  
        ]
    )
add_page_title()