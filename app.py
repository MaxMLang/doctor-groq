import streamlit as st
from groq import Client
from dotenv import load_dotenv
import os
# Display the SVG badge below everything
with open("powered_by_groq.svg", "r") as svg_file:
    svg_content = svg_file.read()
st.markdown(
    f"""
    <div style="text-align: right; margin-top: 20px;">
        <div style="width: 150px; height: auto;">{svg_content}</div>
    </div>
    """,
    unsafe_allow_html=True
)
# Load environment variables from .env file
load_dotenv()

# Set up the Groq client using the API key from secrets or environment
client = Client(api_key=os.getenv("GROQ_API_KEY"))

# Title and Introduction
st.markdown("<h1 style='color: #000000; font-family: Arial, sans-serif;'>Doctor Groq - Kid-Friendly Learning Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1em; font-family: Arial, sans-serif; color: #555;'>Hello! I am Doctor Groq, your friendly assistant here to help kids learn about the world in a safe and fun way!</p>", unsafe_allow_html=True)

# Set a default conversational model and safety model
if "conversational_model" not in st.session_state:
    st.session_state["conversational_model"] = "llama-3.1-70b-versatile"  # Conversational model
if "safety_model" not in st.session_state:
    st.session_state["safety_model"] = "llama-guard-3-8b"  # Content safety checker model

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hazard categories dictionary
hazard_categories = {
    "S1": "Violent Crimes",
    "S2": "Non-Violent Crimes",
    "S3": "Sex-Related Crimes",
    "S4": "Child Sexual Exploitation",
    "S5": "Defamation",
    "S6": "Specialized Advice",
    "S7": "Privacy",
    "S8": "Intellectual Property",
    "S9": "Indiscriminate Weapons",
    "S10": "Hate",
    "S11": "Suicide & Self-Harm",
    "S12": "Sexual Content",
    "S13": "Elections",
    "S14": "Code Interpreter Abuse"
}

# Function to check content safety using Llama Guard
def check_content_safety(text):
    try:
        # Use Llama Guard to check for unsafe content
        completion = client.chat.completions.create(
            model=st.session_state["safety_model"],
            messages=[{"role": "user", "content": text}],
            max_tokens=10,
            temperature=0.0,
        )

        # Extract response and look for a hazard code
        assistant_message = completion.choices[0].message.content.lower()
        for code, category in hazard_categories.items():
            if code.lower() in assistant_message:
                return False, code  # Unsafe content detected with hazard code
        return True, None  # No hazard detected

    except Exception as e:
        st.error(f"Error in content safety check: {e}")
        return True, None  # Return safe if there's an error

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input with a colorful and friendly placeholder
prompt = st.chat_input("Ask Doctor Groq anything fun or educational!")

if prompt:
    # Add kid-friendly guidance to the system prompt
    system_prompt = "You are Doctor Groq, a kid-friendly, educational assistant. Please answer in a way that is safe, friendly, and easy for children to understand. Your responses should be educational and fun!"

    # Check user input for safety
    is_safe, hazard_code = check_content_safety(prompt)
    if not is_safe:
        # Display a warning message if input is unsafe
        warning_message = f"🚨 Warning: Unsafe content detected in input. Hazard: {hazard_code} - {hazard_categories[hazard_code]}"
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": warning_message})
        st.write(warning_message)
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🦖"):
            st.markdown(prompt)

        # Call conversational model for assistant response
        with st.chat_message("assistant", avatar="🤖"):
            try:
                # Generate response with the conversational model
                completion = client.chat.completions.create(
                    model=st.session_state["conversational_model"],
                    messages=[
                        {"role": "system", "content": system_prompt},  # Add system prompt
                        *st.session_state.messages  # Unpack the existing messages
                    ],
                )
                response_content = completion.choices[0].message.content

                # Check assistant's response for safety
                is_safe, hazard_code = check_content_safety(response_content)
                if not is_safe:
                    # Display warning if response is unsafe
                    response_content = f"🚨 Warning: Unsafe content detected in response. Hazard: {hazard_code} - {hazard_categories[hazard_code]}"

                st.markdown(response_content)  # Display the assistant's response
                # Append the assistant's response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response_content})

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Style customization to make the UI more kid-friendly
st.markdown(
    """
    <style>
    .stChatInput > div {
        border-radius: 10px;
        background-color: #e3f2fd;
    }
    .stChatInput textarea {
        border: 2px solid #64b5f6;
        font-size: 1.1em;
        font-family: Arial, sans-serif;
    }
    .stMarkdownContainer > div {
        font-size: 1em;
        font-family: 'Comic Sans MS', sans-serif;
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid #e0e0e0;
    }
    .stMarkdownContainer h2 {
        color: #42a5f5;
        font-size: 1.4em;
        font-family: 'Comic Sans MS', sans-serif;
    }
    .stButton > button {
        background-color: #81c784;
        color: white;
        font-size: 1em;
        padding: 10px 20px;
        border-radius: 12px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


