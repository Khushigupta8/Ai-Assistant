import texttospeech
import speechtotext
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data or "what's your name" in user_data:
        texttospeech.texttospeech("My name is Assistant.")
        return "My name is Assistant."
    
    elif "who are you" in user_data:
        texttospeech.texttospeech("I am Khushi's Virtual Assistant.")
        return "I am Khushi's Virtual Assistant."
    
    elif "how old are you" in user_data:
        texttospeech.texttospeech("I am just a few months old.")
        return "I am just a few months old."

    elif "hello" in user_data or "hey" in user_data:
        texttospeech.texttospeech("Hello, How can I help you?")
        return "Hello, How can I help you?"

    elif "good morning" in user_data:
        texttospeech.texttospeech("Good morning, How are you?")
        return "Good morning, How are you?"

    elif "who created you" in user_data or "who is your creator" in user_data:
        texttospeech.texttospeech("I was created by Khushi.")
        return "I was created by Khushi."

    elif "thank you" in user_data:
        texttospeech.texttospeech("You're welcome!")
        return "You're welcome!"

    elif "time now" in user_data or "what time is it" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} hour : {current_time.minute} minute"
        texttospeech.texttospeech(Time)
        return Time
    elif "date today" in user_data or "what is the date today" in user_data:
        current_date = datetime.datetime.now().date()
        Date = f"Today's date is {current_date}."
        texttospeech.texttospeech(Date)
        return Date
    
    elif "shutdown" in user_data:
        texttospeech.texttospeech("Ok, have a nice day")
        return "Ok, have a nice day"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        texttospeech.texttospeech("Sure, playing music.")
        return "Sure, playing music."

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        texttospeech.texttospeech("Sure, opening YouTube.")
        return "Sure, opening YouTube."

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        texttospeech.texttospeech("Sure, opening Google.")
        return "Sure, opening Google."

    elif "weather" in user_data:
        ans = weather.weather()
        texttospeech.texttospeech(ans)
        return ans

    elif "what can you do for me" in user_data:
        response = "I can assist you with various tasks such as providing information, playing music, and more."
        texttospeech.texttospeech(response)
        return response

    else:
        texttospeech.texttospeech("Sorry, I am not allowed to do this.")
        return "Sorry, I am not allowed to do this."
