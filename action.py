import texttospeech
import speechtotext
import datetime
import webbrowser
import weather
def Action(data):
 user_data=data.lower()

 if "what is your name" in user_data:
    texttospeech.texttospeech("My name is Assistant.")
    return "My name is Assistant."

 elif "hello" in user_data or "hey" in user_data:
    texttospeech.texttospeech("Hello, How can I help you?")
    return "Hello, How can I help you?"
    
 elif "good morning" in user_data:
    texttospeech.texttospeech("Good morning, How are you?")
    return "Good morning, How are you?"

 elif "time now" in user_data:
    current_time=datetime.datetime.now()
    Time=(str)(current_time)+"hour:",(str)(current_time.minute)+"minute"
    texttospeech.texttospeech(Time)
    return Time

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
    ans=weather.weather()
    texttospeech.texttospeech(ans)
    return ans

 else:
    texttospeech.texttospeech("Sorry, I am not allowed to do this.")
    return "Sorry, I am not allowed to do this."