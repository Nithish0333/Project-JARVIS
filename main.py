import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
from openai import OpenAI

# =========================
# SET YOUR API KEY HERE
# =========================
client = OpenAI(api_key="YOUR_API_KEY")

# =========================
# TEXT TO SPEECH
# =========================
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# =========================
# SPEECH RECOGNITION
# =========================
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# =========================
# AI RESPONSE
# =========================
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Error connecting to AI."

# =========================
# MAIN ASSISTANT LOGIC
# =========================
def run_assistant():
    speak("Hello! I am your AI assistant. How can I help you?")

    while True:
        command = listen()

        if command == "":
            continue

        # EXIT
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        # TIME
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        # GOOGLE SEARCH
        elif "search" in command:
            speak("Searching on Google")
            webbrowser.open(f"https://www.google.com/search?q={command}")

        # OPEN YOUTUBE
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # OPEN NOTEPAD (Windows)
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # DEFAULT → ASK AI
        else:
            response = ask_ai(command)
            speak(response)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    run_assistant()
