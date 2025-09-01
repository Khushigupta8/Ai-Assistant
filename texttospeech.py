import pyttsx3

def texttospeech(text):
    engine = pyttsx3.init()
    
    # Rate slow/fast (70 tumne rakha hai, thoda aur bada sakti ho)
    engine.setProperty('rate', 150)
    
    # Voice list get karna
    voices = engine.getProperty('voices')
    
    # Usually index 1 female hota hai
    engine.setProperty('voice', voices[1].id)
    
    # Speak
    engine.say(text)
    engine.runAndWait()

# Test
texttospeech("Hi world, I am speaking in a female voice.")
