#part1: Taking user voice and convert it to text form.
#part2: Process the text and give some results.
#part3: Convert results (text) into voice.

# From part2:
# To convert text into speek.
import pyttsx3
# part1:
# Step1: Go to google search for speechRecognition python and copy its pip function then execute the library in Terminal.
import speech_recognition as sr

# To search a song from and sing from youtube.
import pywhatkit as kit

# For grasping information from we are using wikipedia libarary.
import wikipedia

# Note data and time library is not require it will assign defautly when we install python.
from datetime import datetime

# To leasten jokes for chill out.
import  pyjokes

#creating a function for repeation of engine code
def speek(answer):
    engine = pyttsx3.init()
    # converting male voice into female voice
    voices = engine.getProperty('voices')
    engine.setProperty(('voice', voices[1].id))
    engine.say(answer)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print('speak something')
    audio = r.listen(source)
#Note: This programme requires pyAudio.

# part2:
# To convert sentence into audio use library text to seech
try:
    print(r.recognizer_google(audio))
    question = r.recognizer_google(audio)
    if 'Alexa' in question:
        question.replace('Alexa','')
        print(question)
        if 'what are you doing' in question:
            print('I am waiting for your question')
            speek('I am waiting for your question')

        elif 'how are you' in quesstion:
            print('i am good, what about you?')
            speek('i am good, what about you?')
        elif 'play' in question:
            question = question.replace('play','')
            pywhatkit.playonyt(question)
        elif 'who is' in question:
            question = question.replace('who is','')
            print(wikipedia.summary(question,1))
            speek(wikipedia.summary(question,1))
        elif 'time' in question:
            datetime.today().time().strftime('%I:%M:%P')
            print(time)
            speek(time)
        elif: 'joke' in question:
            pyjocks.get_joke(
            print(joke)
                speek(joke)
            )

    else:
        print('you are not talking with me please carry on')
except sr.UnknownValueError:
    print("sorry, i can't process your request")
    speek("sorry, i can't process your request")


