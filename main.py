import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am Jarvis. Please tell me how may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('stssharin@gmail.com', '01797392776')
    server.sendmail('stssharin@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search for' in query:
            search_term = take_command().split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')

        elif 'search on youtube' in query:
            search_term = take_command().split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'go to youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'go to google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'go to stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, the time is {strTime}")

        elif 'open sublime' in query:
            codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)

        elif 'bye' in query:
            speak("going offline")
            break
        elif 'exit' in query:
            speak("going offline")
            break
        elif 'good bye' in query:
            speak("going offline")
            break
        elif 'tata' in query:
            speak("going offline")
            break


    # About Jarvis
        elif 'who are you' in query:
            speak("I am Jarvis")
        elif 'what can you do' in query:
            speak('I can tell the time, I can search in wikipedia, google and youtube')

        elif 'how are you' in query:
            speak('I am doing fine. Thank you for asking')

    # Sending mail
        elif 'email to sharin' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "saraban15-9660@diu.edu.bd"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I could not send this email at this time.")

        elif 'email to farhan' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "khandokar15-9731@diu.edu.bd"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I could not send this email at this time.")

        elif 'email to zuba' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "jobayer15-9641@diu.edu.bd"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I could not send this email at this time.")
        elif 'email to sir' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "toukirul.cse0300.c@diu.edu.bd"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I could not send this email at this time.")


