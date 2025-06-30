Clara – Personal Voice Assistant

Clara is a simple Python-based voice assistant that can greet users, tell the current time and date, open websites, and perform basic internet searches using voice commands.

Objective

To build a beginner-friendly personal voice assistant that interacts with the user through voice, performs searches, and gives real-time information like time and date.

Features

-Listens to your voice commands

- Responds with voice (TTS)

-Tells the current time

-Tells today's date

-Searches Google using keywords (when "internet" or "web" is mentioned)

-Opens websites like Google and YouTube.

-Can be exited with "bye", "exit", or "tata".

Tools & Libraries Used

-speech_recognition – for capturing and recognizing speech

-pyttsx3 – for text-to-speech functionality

-webbrowser – to open websites

-datetime – for time and date functions.

-pyaudio – required for voice input via microphone.

How It Works

-Clara greets the user based on the current time.

-It continuously listens for your voice commands.

-Based on the keywords spoken, it can:

-Search the web ("internet", "web", "search")

-Open Google or YouTube

-Say the current time or date.

-Exit if you say "bye", "exit", or "tata".

Sample Interaction

Clara: Good Afternoon!

Clara: I'm Clara - your personal voice assistant. How can I help you today?

You: What is the time?

Clara: The current time is 15:30:10

You: Search internet Python programming

Clara: Searching the Internet....
(opens Google search for Python programming)

You: Bye

Clara: Bye! See you later.

Outcome

-Voice interaction with Python using speech recognition and synthesis.

-Great project for beginners exploring voice interfaces and automation.






