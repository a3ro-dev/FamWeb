import streamlit as st
import json

# Set page configuration
st.set_page_config(
    page_title="Fam Assistant",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Enhanced CSS with modern design elements
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        
        :root {
            --primary-color: #3b82f6;
            --primary-light: #60a5fa;
            --secondary-color: #10b981;
            --background-color: #ffffff;
            --surface-color: #f8fafc;
            --text-color: #1e293b;
            --text-light: #64748b;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1);
        }

        .stApp {
            background: var(--background-color);
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        h1, h2, h3, h4, h5, h6, .subheader {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--text-color);
            font-weight: 600;
            letter-spacing: -0.02em;
        }

        .main-header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 700;
            text-align: center;
            margin: 2rem 0;
            animation: fadeIn 1s ease-in;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .card {
            background: var(--surface-color);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: var(--shadow-md);
            margin: 1.5rem 0;
            transition: all 0.3s ease;
            border: 1px solid rgba(0,0,0,0.05);
        }

        .card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 2.5rem 0;
        }

        .feature-item {
            background: var(--surface-color);
            padding: 1.75rem;
            border-radius: 1rem;
            border: 1px solid rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            box-shadow: var(--shadow-sm);
        }

        .feature-item:hover {
            border-color: var(--primary-light);
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }

        .feature-item h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .command-section {
            background: var(--text-color);
            color: white;
            padding: 2.5rem;
            border-radius: 1.25rem;
            margin: 2.5rem 0;
            box-shadow: var(--shadow-lg);
        }

        .section {
            padding: 1.5rem;
            background: var(--surface-color);
            border-radius: 1rem;
            margin: 1.5rem 0;
            box-shadow: var(--shadow-sm);
        }

        .section:hover {
            box-shadow: var(--shadow-md);
        }

        code {
            background: rgba(0,0,0,0.05);
            padding: 0.2em 0.4em;
            border-radius: 0.375rem;
            font-size: 0.875em;
            font-family: 'SF Mono', 'JetBrains Mono', monospace;
        }

        pre {
            background: var(--text-color);
            padding: 1.5rem;
            border-radius: 0.75rem;
            overflow-x: auto;
            box-shadow: var(--shadow-md);
        }

        pre code {
            background: transparent;
            color: #e2e8f0;
            padding: 0;
        }

        .button {
            display: inline-flex;
            align-items: center;
            padding: 0.75rem 1.5rem;
            background: var(--primary-color);
            color: white;
            border-radius: 0.75rem;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-sm);
        }

        .button:hover {
            background: var(--primary-light);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--surface-color);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--primary-light);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--primary-color);
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            .main-header {
                font-size: 2.5rem;
            }
            .feature-grid {
                grid-template-columns: 1fr;
            }
            .section {
                padding: 1rem;
            }
        }

        /* Include a background animation (updated) */
        body:before {
            content: '';
            position: fixed;
            width: 100vw;
            height: 100vh;
            background: radial-gradient(circle, rgba(59,130,246,0.2), transparent 70%);
            animation: floatBG 10s infinite alternate;
            z-index: -1;
        }

        @keyframes floatBG {
            0% {
                transform: scale(1) translate(0, 0);
            }
            100% {
                transform: scale(1.2) translate(-20px, -30px);
            }
        }

        /* Add a glow hover effect to .card and .feature-item */
        .card:hover, .feature-item:hover {
            box-shadow: 0 0 12px rgba(59,130,246,0.3), var(--shadow-lg);
            transform: translateY(-8px);
        }

        /* Add neon glow to main header text */
        .main-header {
            text-shadow: 0 0 6px rgba(59,130,246,0.7), 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Intensify button glow on hover */
        .button:hover {
            box-shadow: 0 0 8px rgba(59,130,246,0.4), var(--shadow-md);
        }
    </style>
""", unsafe_allow_html=True)

# Main header with animation
st.markdown('<h1 class="main-header">FAM Assistant</h1>', unsafe_allow_html=True)

# Introduction card
with st.container():
    st.markdown("""
        <div class="card">
            <h2>🤖 Your Smart Home Companion</h2>
            <p>FAM Assistant is an advanced AI-powered assistant designed for the Raspberry Pi Zero 2W. 
            Combining voice control, gesture recognition, and smart automation to create a seamless home experience.</p>
        </div>
    """, unsafe_allow_html=True)

# Features grid
st.markdown('<h2 style="margin-top: 3rem;">✨ Key Features</h2>', unsafe_allow_html=True)
st.markdown("""
    <div class="feature-grid">
        <div class="feature-item">
            <h3>🎵 Music Control</h3>
            <p>Voice-activated music playback with Spotify integration and local library management</p>
        </div>
        <div class="feature-item">
            <h3>👋 Gesture Control</h3>
            <p>Intuitive gesture recognition using ultrasonic sensors for hands-free operation</p>
        </div>
        <div class="feature-item">
            <h3>🎮 Gaming Hub</h3>
            <p>Host and manage game servers with voice commands and email invitations</p>
        </div>
        <div class="feature-item">
            <h3>📝 Task Management</h3>
            <p>Create and search tasks using natural voice commands</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Table of Contents
st.markdown('<div class="subheader">Table of Contents</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ol>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#usage">Usage</a>
            <ul>
                <li><a href="#voice-commands">Voice Commands</a></li>
                <li><a href="#gesture-controls">Gesture Controls</a></li>
            </ul>
        </li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#development">Development</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#support">Support</a></li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown('<div class="subheader" id="features">Features</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h3>Voice Recognition</h3>
    <ul>
        <li><strong>Wake Word Detection</strong>: Utilizes Porcupine for efficient wake word detection without heavy processing.</li>
        <li><strong>Command Processing</strong>: Recognizes and processes a wide range of voice commands including music control, task management, Bluetooth operations, and more.</li>
        <li><strong>GPT Integration</strong>: Handles unknown commands using GPT-powered responses for seamless interactions.</li>
    </ul>
    <h3>Gesture Control</h3>
    <ul>
        <li><strong>Hand Gesture Detection</strong>: Uses an ultrasonic sensor to detect hand gestures within a specified distance range (2-5cm).</li>
        <li><strong>Debounce Mechanism</strong>: Ensures accurate gesture recognition with debounce protection to prevent false triggers.</li>
        <li><strong>Additional Gestures</strong>: Capable of detecting various gestures like long holds and double taps for enhanced control options.</li>
    </ul>
    <h3>Music Management</h3>
    <ul>
        <li><strong>Playback Control</strong>: Play, pause, resume, and stop music effortlessly.</li>
        <li><strong>Playlist Handling</strong>: Supports shuffle mode and track navigation (next/skip).</li>
        <li><strong>Volume Control</strong>: Adjusts volume levels during different states of operation.</li>
        <li><strong>Music Download</strong>: Facilitates downloading of music tracks via voice commands.</li>
    </ul>
    <h3>Task Management</h3>
    <ul>
        <li><strong>Add Tasks</strong>: Add new tasks through voice input.</li>
        <li><strong>Search Tasks</strong>: Search for existing tasks with fuzzy matching for accuracy.</li>
    </ul>
    <h3>Bluetooth Integration</h3>
    <ul>
        <li><strong>Bluetooth Mode</strong>: Start and stop Bluetooth mode to act as a Bluetooth speaker.</li>
        <li><strong>Device Management</strong>: Handles pairing, connecting, and managing Bluetooth devices seamlessly.</li>
    </ul>
    <h3>News and Information</h3>
    <ul>
        <li><strong>News Updates</strong>: Fetches and reads out the latest news headlines.</li>
        <li><strong>Time and Date</strong>: Reports current time and date upon request.</li>
    </ul>
    <h3>Gaming Hub</h3>
    <ul>
        <li><strong>Game Launching</strong>: Launch and manage favorite games with voice commands.</li>
        <li><strong>Email Invitations</strong>: Sends game session invitations with the device's IP address.</li>
    </ul>
    <h3>Automation</h3>
    <ul>
        <li><strong>System Control</strong>: Execute system commands like shutdown through voice commands.</li>
        <li><strong>Chime Notifications</strong>: Plays chimes to indicate successful command detections and operations.</li>
    </ul>
    <h3>Utility Functions</h3>
    <ul>
        <li><strong>IP Address Retrieval</strong>: Obtains the device's IP address for network-related functionalities.</li>
        <li><strong>Graceful Error Handling</strong>: Ensures the assistant remains stable and responsive during unexpected events.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Installation Section
st.markdown('<div class="subheader" id="installation">Installation</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h3>Prerequisites</h3>
    <ul>
        <li><strong>Hardware</strong>:
            <ul>
                <li>Raspberry Pi Zero 2W</li>
                <li>Ultrasonic Sensor (HC-SR04)</li>
                <li>Microphone</li>
                <li>Speakers</li>
                <li>GPIO Pins: 18 (Trigger), 24 (Echo)</li>
            </ul>
        </li>
        <li><strong>Software</strong>:
            <ul>
                <li>Python 3.x</li>
                <li>Pip (Python package installer)</li>
            </ul>
        </li>
    </ul>
    <h3>Steps</h3>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone https://github.com/a3ro-dev/FAM
cd FAM</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Configuration</strong>:
            <ul>
                <li>Copy the example configuration file:
                    <pre><code>cp conf/secrets.example.yaml conf/secrets.yaml</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Run the Assistant</strong>:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Configuration Section
st.markdown('<div class="subheader" id="configuration">Configuration</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>The configuration file <code>secrets.yaml</code> contains various settings such as API keys, file paths, and other parameters. Ensure all required fields are filled out correctly to enable the assistant's functionalities.</p>
    <h3>Configuration Fields</h3>
    <ul>
        <li><strong>access_key</strong>: Your access key for the Porcupine wake word detection engine.</li>
        <li><strong>keyword_path</strong>: Path to your Porcupine keyword file.</li>
        <li><strong>music_path</strong>: Path to your music directory.</li>
        <li><strong>groq_api_key</strong>: Your Groq API key for specific functionalities.</li>
        <li><strong>openai_api_key</strong>: Your OpenAI API key for GPT integration.</li>
        <li><strong>model_name</strong>: The name of the model you are using.</li>
        <li><strong>utilities</strong>:
            <ul>
                <li><strong>author</strong>: Your name.</li>
                <li><strong>audio_files</strong>:
                    <ul>
                        <li><strong>success</strong>: Path to the success audio file.</li>
                        <li><strong>error</strong>: Path to the error audio file.</li>
                        <li><strong>load</strong>: Path to the load audio file.</li>
                    </ul>
                </li>
                <li><strong>model_path</strong>: Path to your model file.</li>
                <li><strong>weather_api_key</strong>: Your API key for fetching weather information.</li>
                <li><strong>news_api_key</strong>: Your API key for fetching news updates.</li>
                <li><strong>email</strong>:
                    <ul>
                        <li><strong>sender_email</strong>: Your email address used for sending emails.</li>
                        <li><strong>sender_password</strong>: Your email account password.</li>
                        <li><strong>smtp_server</strong>: SMTP server address for your email provider.</li>
                        <li><strong>smtp_port</strong>: SMTP server port (commonly 587 for TLS).</li>
                    </ul>
                </li>
                <li><strong>image_path</strong>: Path to your image file.</li>
            </ul>
        </li>
        <li><strong>music_search</strong>:
            <ul>
                <li><strong>output_path</strong>: Path to the output directory for music search results.</li>
            </ul>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Usage Section
st.markdown('<div class="subheader" id="usage">Usage</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h3>Starting the Assistant</h3>
    <p>Launch the assistant using the command mentioned above. The assistant will start listening for the wake word to activate.</p>
    <h3 id="voice-commands">Voice Commands</h3>
    <h4>System Control</h4>
    <ul>
        <li><strong>Shutdown</strong>: "Shutdown"</li>
    </ul>
    <h4>Music Control</h4>
    <ul>
        <li><strong>Play Music</strong>: "Play music"</li>
        <li><strong>Pause Music</strong>: "Pause music"</li>
        <li><strong>Resume Music</strong>: "Resume music"</li>
        <li><strong>Stop Music</strong>: "Stop music"</li>
        <li><strong>Next Song</strong>: "Next song" or "Skip"</li>
        <li><strong>Seek Forward</strong>: "Seek forward"</li>
    </ul>
    <h4>Task Management</h4>
    <ul>
        <li><strong>Add Task</strong>: "Add task" or "Add a new task"</li>
        <li><strong>Search Task</strong>: "Search task"</li>
    </ul>
    <h4>Information</h4>
    <ul>
        <li><strong>Time Inquiry</strong>: "What time is it?" or "What’s the time?" or "Time"</li>
        <li><strong>Date Inquiry</strong>: "What’s the date?" or "Current date" or "Date"</li>
    </ul>
    <h4>News</h4>
    <ul>
        <li><strong>Get News</strong>: "News"</li>
    </ul>
    <h4>Bluetooth [Not Yet Deployed]</h4>
    <ul>
        <li><strong>Start Bluetooth Mode</strong>: "Start Bluetooth mode", "Enable Bluetooth mode", or "Bluetooth speaker mode"</li>
        <li><strong>Stop Bluetooth Mode</strong>: "Stop Bluetooth mode", "Disable Bluetooth mode", or "Exit Bluetooth speaker mode"</li>
    </ul>
    <h4>Gaming</h4>
    <ul>
        <li><strong>Play Game</strong>: "Play game" or "Start game"</li>
        <li><strong>Stop Game</strong>: "Stop game" or "End game"</li>
    </ul>
    <h4>Greetings</h4>
    <ul>
        <li><strong>Greet</strong>: "Hi", "Hello", or "Hey"</li>
        <li><strong>How Are You</strong>: "How are you?"</li>
    </ul>
    <h4>Automation</h4>
    <ul>
        <li><strong>Start My Day</strong>: "Start my day" or "Good morning"</li>
    </ul>
    <h3 id="gesture-controls">Gesture Controls</h3>
    <ul>
        <li><strong>Activate Voice Input</strong>: Hold your hand 2-5cm from the ultrasonic sensor to activate voice input.</li>
        <li><strong>Additional Gestures</strong>:
            <ul>
                <li><strong>Long Hold</strong>: Maintain hand position for a prolonged period to trigger specific actions.</li>
                <li><strong>Double Tap</strong>: Perform quick gestures to execute shortcut commands.</li>
            </ul>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Project Structure Section
st.markdown('<div class="subheader" id="project-structure">Project Structure</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <pre><code>FamAssistant/
├── main.py                      # Main assistant implementation
├── _fam_assistant.py            # Core assistant logic
├── libs/
│   ├── bluetooth_manager.py     # Bluetooth functionality
│   ├── clock.py                 # Time and task management
│   ├── games.py                 # Games management
│   ├── gpt.py                   # GPT integration
│   ├── music.py                 # Music player implementation
│   ├── raspotify_wrapper.py     # Spotify Connect Manager
│   ├── music_search.py          # Music search and download
│   └── utilities.py             # Utility functions
├── assets/
│   └── tts_audio_files/         # Text-to-speech audio files
├── conf/
│   ├── config.example.yaml      # Example configuration file
│   └── config.yaml              # User configuration file
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies</code></pre>
</div>
""", unsafe_allow_html=True)

# Development Section
st.markdown('<div class="subheader" id="development">Development</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h3>Language</h3>
    <p>Python 3.x</p>
    <h3>Concurrency</h3>
    <ul>
        <li>Utilizes <code>ThreadPoolExecutor</code> for handling I/O-bound tasks like command processing and gesture detection.</li>
        <li>Employs <code>ProcessPoolExecutor</code> to leverage all four cores of the Raspberry Pi Zero 2W for CPU-bound operations, ensuring efficient performance and avoiding deadlocks.</li>
    </ul>
    <h3>Logging</h3>
    <p>Implements structured logging for monitoring and debugging purposes.</p>
    <h3>GPIO Management</h3>
    <p>Manages GPIO pins for ultrasonic sensor-based gesture detection with proper setup and cleanup to prevent hardware issues.</p>
    <h3>Error Handling</h3>
    <p>Incorporates comprehensive error handling to maintain assistant stability and reliability.</p>
    <h3>Key Improvements for Multi-Core Utilization</h3>
    <ul>
        <li><strong>ThreadPoolExecutor and ProcessPoolExecutor</strong>:
            <ul>
                <li>Added <code>ThreadPoolExecutor</code> for I/O-bound tasks.</li>
                <li>Added <code>ProcessPoolExecutor</code> for CPU-bound tasks to utilize all four cores effectively.</li>
            </ul>
        </li>
        <li><strong>Gesture Detection</strong>:
            <ul>
                <li>Runs gesture detection in a separate thread to prevent blocking the main process.</li>
            </ul>
        </li>
        <li><strong>Command Processing</strong>:
            <ul>
                <li>Handles command processing concurrently using executors to distribute the workload across multiple cores.</li>
            </ul>
        </li>
        <li><strong>Avoiding Deadlocks</strong>:
            <ul>
                <li>Ensures thread-safe operations with proper locking mechanisms.</li>
                <li>Separates I/O and CPU-bound tasks to different executors to prevent resource contention.</li>
            </ul>
        </li>
    </ul>
    <h3>Concurrency Model</h3>
    <p>Fam Assistant employs a hybrid concurrency model to maximize CPU utilization and maintain responsiveness:</
</div>
""", unsafe_allow_html=True)

# License Section
st.markdown('<div class="subheader" id="license">License</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>This work is licensed under a <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/" target="_blank">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.</p>
    <img src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" alt="Creative Commons License" style="margin-top: 1rem;">
</div>
""", unsafe_allow_html=True)

# Support Section
st.markdown('<div class="subheader" id="support">Support</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>For any questions or issues, reach out at <a href="mailto:akshatsingh14372@outlook.com">akshatsingh14372@outlook.com</a></p>
    <p>Developer: <a href="https://github.com/a3ro-dev" target="_blank">a3ro-dev</a></p>
    <div class="contact" style="margin-top: 2rem;">
        <a href="https://github.com/a3ro-dev" target="_blank" class="button">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                 alt="GitHub" 
                 style="width: 24px; height: 24px; vertical-align: middle; margin-right: 8px;">
            Visit GitHub Profile
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

