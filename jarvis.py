#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3
#Already prent in the system no need to install
#Library to detech the user input speech and convert to text
# Already prent in the system no need to install
import datetime
import wikipedia
import pyttsx3
import webbrowser
# Library to detech the user input speech and convert to text
import speech_recognition as sr
import os

"""What SAPI 5?
Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft. Starting with Windows XP, it ships as part of the Windows OS"""
engine = pyttsx3.init('sapi5')
#This line is basically used to find out the voices available in our system usually it will have a male and female voice
voices =engine.getProperty('voices')
#To identify which is the male voice and which is the female voice available in the system O id will give TTS_MS_EN-US_DAVID_11.0 and DAVID
# is a male voice also if we give 1 then it will give ZIRA which is a female voice TTS_MS_EN-US_ZIRA_11.0 and we can choose from that"""
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    #Used to get the current date and time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    elif hour>=12 and hour<=18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am virtual assistant created by Pranav, Please tell me how may i help you')
def takeCommand():
#This takes microphone input from the user and returns the string output
    r=sr.Recognizer() #This is a Recognizer class which basically helps us to identify the audio
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1 #seconds of non speaking audio before a phase is considered complete
        audio = r.listen(source)
    try: #There are chances that the while recognizing audio there can be exeptions so we have to give it inside the try catch
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:, {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please ...")
        return "None"
    return query


"""We mainly use this if __name__ when we have to use a method which is defined somewhere else and while calling this method to somewhere else we have to use this because where the method
 we have defined it there it will have same some definition inside that but if we are just calling this method somewhere else then we don't need these definition to work we need this method to work
   with the arguments which we use to call the method"""
if __name__ == "__main__":
    speak("Pranav is going to be worlds greatest python programmer")
    wishme()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak('Searching Wikipedia')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")





