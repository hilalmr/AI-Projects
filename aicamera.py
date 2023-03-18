import random
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

# Initialize Text-to-speech engine
engine = pyttsx3.init()

# Greetings list
greetings = ["hello", "hi", "hey there", "hey"]

# Goodbye list
goodbyes = ["bye", "goodbye", "see you later", "take care"]

# Openings list
openings = ["can you", "what can you", "what do you", "what are you", "who are you", "how do you"]

# Knowledge base
knowledge_base = {
    "what is your name": "My name is AI, how can I assist you today?",
    "what time is it": datetime.datetime.now().strftime("It's %I:%M %p"),
    "open Google": webbrowser.open("https://www.google.com"),
    "open YouTube": webbrowser.open("https://www.youtube.com")
}

# Function to handle text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle speech-to-text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry, could not recognize what you said.")
            return ""

# Function to handle the AI logic
def AI(text):
    text = text.lower()
    if text in greetings:
        speak(random.choice(greetings))
    elif text in goodbyes:
        speak(random.choice(goodbyes))
        exit()
    elif any(word in text for word in openings):
        speak("I am an AI, and I can do a lot of things. What would you like me to do?")
    elif text in knowledge_base:
        speak(knowledge_base[text])
    else:
        speak("I'm sorry, I don't understand. Can you please repeat that?")

# Main function to handle the loop
def main():
    while True:
        text = listen()
        AI(text)

# Run the main function
if __name__ == "__main__":
    main()
