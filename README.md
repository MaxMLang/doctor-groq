# Doctor Groq - Kid-Friendly Learning Chatbot

<img src="powered_by_groq.svg" style="width: 300px; height: auto;">


## Overview

**Doctor Groq** is a safe, kid-friendly educational chatbot designed to provide children with a secure platform to explore educational topics. Leveraging **Llama Guard 3 8B** powered by Groq for robust content filtering, Doctor Groq ensures that interactions remain age-appropriate, allowing young users to learn and discover the world with guidance they can trust. 

This chatbot is created for the **Groq Bounty** competition, showcasing the capabilities of Groq’s Llama Guard in providing safe, AI-powered education.

### Demo

![Doctor Groq Chatbot Screenshot](./demo.gif)

## Why This Project Matters

Education is one of the most impactful sectors for the adoption of AI. AI-powered educational tools can offer personalized and accessible learning experiences, breaking down complex concepts in ways that are easy for children to understand. However, when designing AI applications for young audiences, **safety becomes paramount**.

Children are especially vulnerable to exposure to harmful or inappropriate content. Doctor Groq aims to bridge the gap between AI-driven educational resources and the need for strict content moderation. By integrating **Llama Guard 3 8B** for real-time content safety checks, Doctor Groq provides a safe environment for children to explore educational content. This project highlights how AI can contribute positively to education while safeguarding young users from inappropriate or harmful material.

## Features

- **Content Filtering**: All input and output are processed by **Llama Guard 3 8B** to ensure safety. Any unsafe content is flagged with a specific hazard code, so users are always aware of potentially risky content.
- **Friendly Conversational AI**: A kid-friendly conversational model (llama-3.1-70b-versatile) generates responses that are both educational and easy for children to understand.
- **Engaging and Safe UI**: Designed with a colorful and welcoming interface that is easy to navigate, tailored specifically for young learners.
- **Powered by Groq Badge**: Displays a "Powered by Groq" badge on the UI, showcasing the underlying technology.

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


## Technology Stack

- **Backend**: Groq API using Llama Guard 3 8B for content filtering and safety checks.
- **Frontend**: Streamlit for an interactive and user-friendly interface.
- **Deployment**: Deployable to any platform that supports Python and Streamlit, such as Heroku or Vercel.




