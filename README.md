# Doctor Groq - Kid-Friendly Learning Chatbot

<img src="powered_by_groq.svg" style="width: 300px; height: auto;">

## Overview

**Doctor Groq** is a safe, kid-friendly educational chatbot designed to provide children with a secure platform to explore educational topics. Leveraging **Llama Guard 3 8B** powered by Groq for robust content filtering, Doctor Groq ensures that interactions remain age-appropriate, allowing young users to learn and discover the world with guidance they can trust.

This chatbot is created for the **Groq Bounty** competition, showcasing the capabilities of Groq’s Llama Guard in providing safe, AI-powered education.

## Just Want the Easy Way? Meet Pytector for Groq API

For the purposes of this demo and to showcase the new Groq API capabilities directly, the current GroqMail implementation uses the API in its **raw form**. However, as the author of **Pytector**, I’ve developed a streamlined package that also integrates seamlessly with the Groq API. **Pytector** offers a production-grade solution for efficiently accessing Groq’s powerful features with minimal setup, designed to scale with larger applications.

<div align="center">
    <a href="https://github.com/MaxMLang/pytector">
        <img src="https://github.com/MaxMLang/assets/blob/main/pytector-logo.png?raw=true" alt="Pytector Logo" width="100" height="100">
    </a>
</div>

**Benefits of Pytector:**
- **Security-Focused API Calls**: Offers a streamlined approach to Groq API integration, designed with a focus on prompt injection detection.
- **Error Handling and Logging**: Built-in error handling to ensure stable and reliable API communication.
- **Scalability for Production**: Developed with a focus on streamlined, scalable implementations suitable for high-demand environments.

For more details and to use Pytector in your projects, visit the [Pytector GitHub repository](https://github.com/MaxMLang/pytector).

### Demo

![Doctor Groq Chatbot Screenshot](./demo.gif)

## Why This Project Matters

Education is one of the most impactful sectors for AI adoption. AI-powered educational tools can offer personalized and accessible learning experiences, simplifying complex concepts in ways that are easy for children to understand. However, when designing AI applications for young audiences, **safety becomes paramount**.

Children are especially vulnerable to exposure to harmful or inappropriate content. Doctor Groq aims to bridge the gap between AI-driven educational resources and the need for strict content moderation. By integrating **Llama Guard 3 8B** for real-time content safety checks, Doctor Groq provides a safe environment for children to explore educational content. This project highlights how AI can contribute positively to education while safeguarding young users from inappropriate or harmful material.

## Features

- **Content Filtering**: Every input and output is processed by **Llama Guard 3 8B** to ensure safety. If unsafe content is detected, it’s flagged with a hazard code, making it easy to identify potentially risky material.
- **Friendly Conversational AI**: A kid-friendly conversational model (llama-3.1-70b-versatile) generates responses that are both educational and easy for children to understand.
- **Engaging and Safe UI**: Designed with a colorful and welcoming interface tailored for young learners, making it easy for them to navigate.
- **Badge System**: Encourages children to engage with educational content by awarding badges based on interaction milestones (details below).
- **Powered by Groq Badge**: Displays a "Powered by Groq" badge in the UI, showcasing the underlying technology.

---

## Badge System

The badge system in Doctor Groq is designed to make learning both fun and rewarding. As children interact with Doctor Groq, they earn badges based on their engagement, encouraging consistent learning and exploration. The badges include:

- **Explorer**: Awarded for asking 5 questions, promoting curiosity.
- **Question Champion**: Given after 10 educational questions, encouraging deeper exploration.
- **Learning Streak**: Earned by spending 10 minutes with Doctor Groq, fostering prolonged engagement.
- **Fun Seeker**: Granted after engaging in 3 fun quizzes, adding an element of play.
- **Knowledge Keeper**: Awarded after reaching 15 interactions, rewarding consistent participation.

Each badge tracks a specific metric (e.g., time spent, number of questions asked) and updates progress dynamically. When a threshold is reached, a success message appears, notifying the child of their new achievement.

For more details on the code implementation of the badge system, refer to the [docs.md](docs.md) file.

---

## How to Run the App

### Prerequisites

- Python 3.7 or higher
- Required packages: `Streamlit`, `groq`, `dotenv`

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/doctor-groq.git
   cd doctor-groq
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory with your Groq API key.
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser and navigate to `http://localhost:8501`.

### Using the App

1. **Ask a Question**: Enter an educational question or topic in the chat.
2. **Content Safety Check**: Doctor Groq, powered by Llama Guard 3 8B, checks both user inputs and responses for content safety.
3. **Educational and Fun Responses**: Doctor Groq provides age-appropriate, friendly responses.
4. **Content Warnings**: Unsafe content is flagged with a hazard code (e.g., S1, S2) to inform users.

---

## Technology Stack

- **Backend**: Groq API using Llama Guard 3 8B for content filtering and safety checks.
- **Frontend**: Streamlit for an interactive and user-friendly interface.
- **Deployment**: Deployable to any platform that supports Python and Streamlit, such as Heroku or Vercel.

---

## Additional Documentation

For an in-depth look at each function, including the `check_and_award_badges` and `check_content_safety` functions, refer to [docs.md](docs.md). This document contains detailed explanations for each function, their parameters, and return values, as well as an overview of the badge system and UI styling.


