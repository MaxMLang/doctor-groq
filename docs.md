# Doctor Groq Chatbot Code Documentation

This document provides a detailed overview of the key components, functions, and logic used in the **Doctor Groq** chatbot application. It covers the initialization, badge system, content safety checks, and interaction handling.

---

## Table of Contents
1. [Code Overview](#code-overview)
2. [Function Documentation](#function-documentation)
   - [check_and_award_badges](#check_and_award_badges)
   - [check_content_safety](#check_content_safety)
3. [Badge System](#badge-system)
4. [User Interface and Styling](#user-interface-and-styling)

---

## Code Overview

The **Doctor Groq** application is a Streamlit-based chatbot for children, enhanced with Groq’s Llama Guard API for content safety. The chatbot allows children to interact with Doctor Groq and earn badges for various educational interactions and time spent.

The main components of the code include:
- Badge progression and display system for achievements.
- A content safety check for user inputs and chatbot responses.
- Custom styling to make the UI engaging and user-friendly.

## Function Documentation

### `check_and_award_badges`

```python
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
```

This function manages the badge progression system by checking current interaction counts or cumulative time spent. If a user reaches a badge threshold, it updates the badge to “earned” and displays a success message in the sidebar.

### `check_content_safety`

```python
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
```

This function uses the Llama Guard content moderation model to assess if a given text input is safe for children. If unsafe content is detected, it returns `False` along with a hazard code.

---

## Badge System

The application includes a set of interactive badges to motivate children to explore more. The badge system is managed through a dictionary in `st.session_state`, where each badge has:
- A `description`
- A `count` or `time_spent` (for tracking progress)
- A `threshold` for earning the badge
- An `earned` status, updated once the badge is awarded

Badges included:
- **Explorer**: Ask 5 questions
- **Question Champion**: Answer 10 educational questions
- **Learning Streak**: Spend 10 minutes with Doctor Groq
- **Fun Seeker**: Engage in 3 fun quizzes
- **Knowledge Keeper**: Reach 15 interactions

---

## User Interface and Styling

The interface uses Streamlit’s markdown and CSS styling to create a user-friendly experience. Key styling elements:
- Custom `st.markdown` styling for buttons, chat input, and badge progression.
- SVG badge display, using `powered_by_groq.svg` positioned at the bottom of the interface.
- **Custom badges** in the sidebar, allowing kids to view their progress through interactive visuals.

The UI design choices were made to keep the application visually appealing and engaging for young users, focusing on vibrant colors, rounded borders, and clear callouts for achievements and messages.

