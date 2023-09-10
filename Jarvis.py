import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morining")
    elif hour >=12 and hour <18:
        speak("Good aftrnoon")
    else:
        speak("Good evning")
          
    speak("i am jarvish sir, tell me how i can do for you?")

    
def takecommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print("recogniging")        
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("say that again please.......")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('savaliyakishan1823@gmail.com', 'Google@1823')
    server.sendmail('savaliyakisan@gmail.com', to, content)
    server.close()
          
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
         # Logic for executing task based on query
        if 'wikipedia' in  query:
            speak('searching wikipedia.......')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            print(result)
            speak(result) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open chrom' in query:
            chrompath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrompath)
        elif 'play music' in query:
            music_dir = 'C:\\Users\\admin\\.idlerc'  
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'good boy' in query:
            speak("raju is good boy")
        elif 'how are you raju' in query:
            speak("how are you raju one thousan time")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif 'open resso' in  query:
            ressopath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Resso\\Resso.exe"
            os.startfile(ressopath)
        elif 'open vlc' in query:
            vlcpath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcpath)
        elif 'open pycharm' in query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\pycharm64.exe"
            os.startfile(pycharmpath)
        elif 'how are you' in query:
            speak("i am fine sir")
            speak("how about you")
        elif 'what is news' in query:
            newspath = "https://www.youtube.com/watch?v=WWTcZyVasUI&ab_channel=RepublicBharat"
            os.startfile(newspath)
        elif "play lofi" in query:
            lofipath = "https://www.youtube.com/watch?v=pT1iNnDGJbM&t=405s&ab_channel=AestheticLo-fiMagic"
            os.startfile(lofipath)
        elif 'email to' in query:
            try:
                speak("What i say?")
                content = takecommand()
                to = "rajnasit81405@gmail.com"
                sendemail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir i can't send this email")
                
        
