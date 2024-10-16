import streamlit as st
import json

# Set page configuration
st.set_page_config(
    page_title="Fam Assistant",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Arial', sans-serif;
    }
    .header {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        color: #1E90FF;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #4682B4;
        margin-top: 30px;
    }
    .section {
        padding: 20px;
        font-size: 18px;
        line-height: 1.6;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 20px;
    }
    .growth-graph {
        text-align: center;
        margin-top: 30px;
    }
    .growth-step {
        font-size: 18px;
        margin-bottom: 15px;
    }
    .contact {
        font-size: 18px;
        color: #007bff;
        text-align: center;
        margin-top: 20px;
    }
    a {
        color: #007bff;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown('<div class="header">Fam Assistant</div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <p>Fam Assistant is an innovative, voice-activated assistant tailored for Raspberry Pi and soon launching for other platforms [Web, Android, Windows, Linux (DESKTOP)]. It supports various functionalities, including music playback, task management, weather updates, and even launching games. This project aims to provide users with an all-encompassing personal assistant experience, packaged in a lightweight solution.</p>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown('<div class="subheader">Key Features</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><strong>Voice Recognition</strong>: Process voice commands using Google Speech Recognition.</li>
        <li><strong>Music Player</strong>: Control your music—play, pause, resume, or stop it effortlessly.</li>
        <li><strong>Task Management</strong>: Add and search for tasks directly through voice input.</li>
        <li><strong>Games Hub</strong>: Launch and manage your favorite games.</li>
        <li><strong>News and Weather</strong>: Stay updated with the latest news and weather reports.</li>
        <li><strong>Automation</strong>: Perform automated tasks like sending emails or managing downloads.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Challenges and Failures
st.markdown('<div class="subheader">Challenges and Failures</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p><strong>RGB Lighting and Camera Module:</strong> Initially, I added ambient RGB lights and a camera for image capture functionality. While the lights were meant to provide a soothing atmosphere during voice interactions, they caused unexpected hardware malfunctions and instability in the assistant’s core functionalities. After multiple attempts at troubleshooting, both the RGB lights and the camera features were permanently removed from the system to ensure stability.</p>
</div>
""", unsafe_allow_html=True)

# Growth Graph with achievements
st.markdown('<div class="subheader">Project Growth</div>', unsafe_allow_html=True)
st.markdown('<div class="growth-graph">', unsafe_allow_html=True)

st.markdown('<div class="growth-step">✔️ Initial Development: Core functionality implemented</div>', unsafe_allow_html=True)
st.markdown('<div class="growth-step">✔️ Integration of Music Playback and Voice Commands</div>', unsafe_allow_html=True)
st.markdown('<div class="growth-step">✔️ Introduction of Weather and News Features</div>', unsafe_allow_html=True)
st.markdown('<div class="growth-step">✔️ Task Management Added</div>', unsafe_allow_html=True)
st.markdown('<div class="growth-step">✔️ Camera and RGB Lights Integrated (Removed Later)</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Projected to turn open source
st.markdown('<div class="subheader">What’s Next?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>I am working towards making Fam Assistant open-source in the near future! At present, it remains closed-source, but the goal is to release it for public collaboration once the system reaches a more mature stage.</p>
</div>
""", unsafe_allow_html=True)

# Closing Remarks
st.markdown('<div class="contact">Contact: For any questions or issues, reach out at <a href="mailto:akshatsingh14372@outlook.com">akshatsingh14372@outlook.com</a>.</div>', unsafe_allow_html=True)
st.markdown('<div class="contact">Developer: <a href="https://github.com/a3ro-dev">a3ro-dev</a></div>', unsafe_allow_html=True)