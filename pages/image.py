import streamlit as st
import requests
import base64

# Function to generate image based on prompt
def generate_image(prompt_input):
    invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"

    headers = {
        "Authorization": "Bearer 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",
        "Accept": "application/json",
    }

    payload = {
        "text_prompts": [
            {
                "text": prompt_input,
                "weight": 1
            },
            {
                "text": "",
                "weight": -1
            }
        ],
        "sampler": "K_DPM_2_ANCESTRAL",
        "steps": 25,
        "cfg_scale": 5,
        "seed": 0
    }

    # Re-use connections
    session = requests.Session()

    response = session.post(invoke_url, headers=headers, json=payload)

    response.raise_for_status()
    response_body = response.json()

    # Access the base64 encoded image data from the response
    base64_data = response_body['artifacts'][0]['base64']

    # Decode the base64 data into binary image data
    image_data = base64.b64decode(base64_data)

    # Display the image in Streamlit
    st.image(image_data, width=720, use_column_width=True)


st.title("Stability AI Image Generator")

# Text prompt input
prompt_input = st.text_area("Enter your text prompt:", "underwater world, plants, shells, creatures, high detail, sharp focus, 4k")

# Generate image button
if st.button("Generate Image"):
    if prompt_input.strip() != "":
        with st.spinner("Generating image..."):
            generate_image(prompt_input)
    else:
        st.error("Please enter a text prompt.")

