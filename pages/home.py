import streamlit as st
st.set_page_config(page_title="Homepage", page_icon="🏠")
with open("designing.css") as source_des:
    st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
# Set the page title and icon


# Display the main title of your homepage
st.title("Welcome to My Project!")

# Add a brief introduction or description of your project
st.write("""
         This is an amazing project that leverages the power of Streamlit to create interactive web applications 
         with ease. Below are some of the standout features of our project:
         """)

# List the features of your project
st.markdown("""
            - **Feature 1**: Description of feature 1.
            - **Feature 2**: Description of feature 2.
            - **Feature 3**: Description of feature 3.
            - **Feature 4**: Description of feature 4.
            """)

