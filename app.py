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
st.markdown(
    "<h1 style='color: #000000; font-family: Arial, sans-serif;'>Doctor Groq - Kid-Friendly Learning Chatbot</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<p style='font-size: 1.1em; font-family: Arial, sans-serif; color: #555;'>Hello! I am Doctor Groq, your friendly assistant here to help kids learn about the world in a safe and fun way!</p>",
    unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize badge progression system in session state
if "badges" not in st.session_state:
    st.session_state.badges = {
        "Explorer": {"description": "Ask 5 questions", "count": 0, "threshold": 5, "earned": False},
        "Question Champion": {"description": "Answer 10 educational questions", "count": 0, "threshold": 10,
                              "earned": False},
        "Learning Streak": {"description": "Spend 10 minutes with Doctor Groq", "time_spent": 0, "threshold": 10,
                            "earned": False},
        "Fun Seeker": {"description": "Engage in 3 fun quizzes", "count": 0, "threshold": 3, "earned": False},
        "Knowledge Keeper": {"description": "Reach 15 interactions", "count": 0, "threshold": 15, "earned": False},
    }


def check_and_award_badges():
    """
    Checks the progression of each badge based on current interaction counts,
    time spent, or specific thresholds. If any badge threshold is met,
    it updates the badge status to 'earned' and displays a success message.

    For badges such as 'Explorer' and 'Question Champion', it checks counts.
    For 'Learning Streak', it checks cumulative time spent with the assistant.

    Side effects:
        - Updates badge statuses in `st.session_state`.
        - Displays badge achievements in the sidebar if thresholds are met.
    """
    for badge, details in st.session_state.badges.items():
        if badge in ["Explorer", "Question Champion", "Fun Seeker", "Knowledge Keeper"]:
            if details["count"] >= details["threshold"] and not details["earned"]:
                st.session_state.badges[badge]["earned"] = True
                st.sidebar.success(f"🎉 You've earned the '{badge}' badge!")
        elif badge == "Learning Streak":
            if details["time_spent"] >= details["threshold"] and not details["earned"]:
                st.session_state.badges[badge]["earned"] = True
                st.sidebar.success(f"⏰ You've earned the '{badge}' badge!")


# Display a checkbox to control sidebar visibility
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

st.sidebar.checkbox("Show Badge Progression", value=st.session_state.show_sidebar, key="show_sidebar")

# Display badges in the sidebar if checkbox is selected
if st.session_state.show_sidebar:
    st.sidebar.header("🏅 Badge Progression")
    for badge, details in st.session_state.badges.items():
        st.sidebar.markdown(f"**{badge}**: {details['description']}")
        if details["earned"]:
            st.sidebar.markdown("Status: ✅ Earned!")
        else:
            progress = details["count"] if badge != "Learning Streak" else details["time_spent"]
            st.sidebar.markdown(f"Status: ⏳ In Progress ({progress} / {details['threshold']})")

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


def check_content_safety(text):
    """
    Verifies if the provided text is safe using the Llama Guard content moderation model.
    It checks for various hazard categories and flags any unsafe content based on category codes.

    Parameters:
        text (str): The user input text that needs to be checked for safety.

    Returns:
        tuple (bool, str): Returns a tuple where the first element is a boolean
        indicating whether the content is safe, and the second element is the
        hazard code (if any) or `None`.

    Side effects:
        - Displays error message in Streamlit app if content check fails.
    """
    try:
        completion = client.chat.completions.create(
            model=st.session_state.get("safety_model", "llama-guard-3-8b"),
            messages=[{"role": "user", "content": text}],
            max_tokens=10,
            temperature=0.0,
        )
        assistant_message = completion.choices[0].message.content.lower()
        for code, category in hazard_categories.items():
            if code.lower() in assistant_message:
                return False, code
        return True, None
    except Exception as e:
        st.error(f"Error in content safety check: {e}")
        return True, None


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input("Ask Doctor Groq anything fun or educational!")

if prompt:
    system_prompt = "You are Doctor Groq, a kid-friendly, educational assistant. Please answer in a way that is safe, friendly, and easy for children to understand. Your responses should be educational and fun!"
    is_safe, hazard_code = check_content_safety(prompt)
    if not is_safe:
        warning_message = f"🚨 Warning: Unsafe content detected. Hazard: {hazard_code} - {hazard_categories[hazard_code]}"
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": warning_message})
        st.write(warning_message)
    else:
        st.session_state.badges["Explorer"]["count"] += 1
        st.session_state.badges["Question Champion"]["count"] += 1
        st.session_state.badges["Knowledge Keeper"]["count"] += 1
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🦖"):
            st.markdown(prompt)
        with st.chat_message("assistant", avatar="🤖"):
            try:
                completion = client.chat.completions.create(
                    model=st.session_state.get("conversational_model", "llama-3.1-70b-versatile"),
                    messages=[{"role": "system", "content": system_prompt}, *st.session_state.messages]
                )
                response_content = completion.choices[0].message.content
                is_safe, hazard_code = check_content_safety(response_content)
                if not is_safe:
                    response_content = f"🚨 Warning: Unsafe content. Hazard: {hazard_code} - {hazard_categories[hazard_code]}"
                st.markdown(response_content)
                st.session_state.messages.append({"role": "assistant", "content": response_content})
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Simulate time spent for Learning Streak badge
st.session_state.badges["Learning Streak"]["time_spent"] += 1

# Check for badge achievements after interaction
check_and_award_badges()

# Style customization
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
