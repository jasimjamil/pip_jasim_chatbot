import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set your Hugging Face API token here
HUGGINGFACE_API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/dalle-mini/dalle-mega"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_image(prompt):
    """
    Generate an image from Hugging Face API using the given prompt.
    Args:
        prompt (str): A text description of the image to generate.
    Returns:
        Image: The generated image as a PIL Image object.
    """
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    elif response.status_code == 400:
        st.error("Bad Request: The prompt may be invalid. Please refine your description.")
        st.stop()
    elif response.status_code == 401:
        st.error("Unauthorized: Check your Hugging Face API token.")
        st.stop()
    elif response.status_code == 429:
        st.error("Rate Limit Exceeded: Too many requests. Try again later.")
        st.stop()
    else:
        st.error(f"Error {response.status_code}: Unable to generate image. Please try again.")
        st.stop()

# Streamlit Frontend Configuration
st.set_page_config(page_title="DALL-E Professional Image Generator", page_icon="\U0001F4BB", layout="centered")
st.title(":art: Professional DALL-E Image Generator")
st.write("### Create Professional and Unique Images with AI")

# Sidebar for Instructions
with st.sidebar:
    st.header("How to Use")
    st.write("1. Enter a detailed description of the professional image.")
    st.write("2. Click 'Generate Image' to create a stunning image.")
    st.write("3. View, download, or share your AI-generated masterpiece.")
    st.markdown("---")
    st.write("**Example Prompts:**")
    st.code("A professional workspace with sunlight coming through large windows.")
    st.code("An artistic painting of a futuristic city skyline at sunset.")
    st.code("A nature-inspired calm and peaceful environment with trees and water.")

# Main Section
st.markdown("#### Enter Your Image Description Below")
prompt_input = st.text_area("Image Description:", placeholder="e.g., A professional abstract painting of an office environment")

# Generate Button
if st.button("Generate Professional Image"):
    if prompt_input.strip():
        st.info("Generating your professional image, please wait...")
        with st.spinner("Processing..."):
            image = generate_image(prompt_input)
            st.image(image, caption="Generated Professional Image", use_column_width=True)
            st.success("Image generation complete!")
    else:
        st.warning("Please enter a description to generate the image.")

# Footer Section
st.markdown("---")
st.markdown(
    "**:art: Created by Muhammad Jasim | Powered by DALL-E & Streamlit**"
)
st.markdown(
    "*This tool generates stunning professional images without specific laptop or Dell restrictions.*"
)
