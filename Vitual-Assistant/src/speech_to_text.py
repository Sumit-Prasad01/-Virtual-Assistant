import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    voice_data = ""  # Initialize voice_data outside the 'with' block
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Optional: Adjusts for ambient noise
        audio = r.listen(source)
    
    try:
        voice_data = r.recognize_google(audio)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError:
        print("There was an error with the request")
    
    return voice_data  # Return the result, even if it's an empty string




# def spech_to_text():
#     r =  sr.Recognizer()
#     with sr.Microphone() as source:
#       audio = r.listen(source) # methord 
#       voice_data = ''
#       try:
#         voice_data = r.recognize_google(audio)
#         return voice_data

#       except sr.UnknownValueError:
#              speak.speak("sorry")
#       except sr.RequestError:
#             speak.speak('No internet connect please turn on you internet')  