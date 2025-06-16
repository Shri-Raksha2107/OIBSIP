#Clara-The Personal Voice Assistant.It can do the basic help like- Greeting the user,tells time,date and also searches the internet for user asked queries.
import speech_recognition as sr
import pyttsx3 as sx3
import webbrowser
import datetime
import pyaudio
#Creating a function to convert text to audio
def voice(text): #creating a function called voice and parameter as text.
    print("Clara:",text)
    try:
        engine=sx3.init()#Initiates text-to-audio engine.
        engine.say(text)#Queues the engines
        engine.runAndWait()#Makes the queue speak.
    except:
        print("Sorry! Couldn't process audio.")#Incase of an error, this message is thrown.
def greet():#This function(greet) is created to wish the user.
    time=int(datetime.datetime.now().hour)
    if time<12:
        voice("Good Morning!")
    elif time<18:
        voice("Good Afternoon!")
    else:
        voice("Good Evening!")
    voice("I'm Clara-your personal voice assistant.How can I help you today?.If you want to search from web do mention internet.")
def user_voice():#This function(user_voice) is used to get user's voice query and turn it into text.
    recog=sr.Recognizer()#This recognises the user's audio/input.
    with sr.Microphone() as source:#Accessing the microphone to get the user's audio or query.
        voice("Listening...")
        recog.adjust_for_ambient_noise(source)#This is used to amplify any external noise in user's audio to improve the quality of the audio.
        audio=recog.listen(source)
    try:
        voice("Understanding...")
        cm=recog.recognize_google(audio)#This google function helps to convert the audio to text.
        print("You said:", cm)
        return cm.lower()
    except sr.UnknownValueError:#Incase, if the audio couldn't be processed than this part runs.
        voice("Sorry, Couldn't understand your query.")
        return "None"
    except sr.RequestError:#Incase, if there is any error in Google services than this part runs.
        voice("Sorry, there was a problem with the Google service.")
        return "None"
def web():#This function(web) is used to search the internet incase the user wants something from the internet.
    question=user_voice()
    if "internet" in question or "web" in question:
        voice("Searching the Internet....")
        question= question.replace("search", "").replace("internet", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={question}")
    elif "open youtube" in question:
        voice("Opening Youtube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in question:
        voice("Opening Google.")
        webbrowser.open("https://www.google.com")
    else:
        voice("Sorry! Couldn't understand your query.")
def time_date():#This function(time_date) is used to get current time and date from the system when the user asks for it. 
    t_d=user_voice()
    if "time" in t_d:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        voice(f"The current time is {strTime}")
    elif "date" in t_d:
        today = datetime.date.today()
        formatted_date = today.strftime("%d/%m/%Y")
        voice("Today's date:", formatted_date)
    else:
        voice("Sorry! Couldn't understand.")
def exit_():#This function runs when the user wants to exit from the voice assistant.
    from_voice=user_voice()
    if "exit" in from_voice or "bye" in from_voice or "tata" in from_voice:
        voice("Bye! See you later.")
    else:
        voice("Sorry! Couldn't understand your query.")
def run_clara():
    greet()
    while True:
        s=user_voice()
        if "internet" in s or "web" in s or "youtube" in s or "google" in s:
            web()
        elif "time" in s or "date" in s:
            time_date()
        elif "exit" in s or "bye" in s or "tata" in s:
            exit_()
            break
        else:
            voice("Sorry! Couldn't understand your query.")    
if __name__ == "__main__":
    run_clara() 



    
        



