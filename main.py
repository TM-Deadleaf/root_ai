import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    '''
    root greets u every time according to the hour of the day
    '''
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("i am root sir,please command me as u wish!")


def takeCommand():
    '''
    take the commands from your microphone
    '''
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User Said:{}\n".format(query))
    except Exception as e:
        print("Say that again!!!!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
    if "wikipedia" in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open youtube " in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "play music" in query:
        music = "name of the directory of the  music"
        songs = os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music, songs))
    elif "the time " in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("the time is :{}".format(strtime))
    elif "open pycharm" in query:
        code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
        os.startfile(cdoe_path)
    elif "send email" in query:
        """
        this query string sends email to required user
        """
        try:
            speak("what should i speak??")
            content = takeCommand()
            sendEmail(to, content)
            to = "the email you wish to send to"
            speak("Email has been sent")
        except Exception as e:
            speak("Sorry my friend harry bhai. I am not able to send this email")
