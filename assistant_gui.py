import tkinter as tk
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    output.insert(tk.END, "Assistant: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output.insert(tk.END, "Listening...\n")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        output.insert(tk.END, "You: " + command + "\n")
        process_command(command.lower())
    except:
        speak("Sorry, I didn't catch that.")

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.date.today()
        speak("Today's date is " + str(date))

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "exit" in command:
        speak("Goodbye Megha!")
        root.quit()

    else:
        speak("Command not recognized.")

root = tk.Tk()
root.title("Megha Virtual Assistant")
root.geometry("500x400")

output = tk.Text(root)
output.pack(pady=10)

listen_button = tk.Button(root, text="Speak", command=listen)
listen_button.pack(pady=10)

root.mainloop()
