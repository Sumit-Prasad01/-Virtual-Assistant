import datetime
import text_to_speech
import speech_to_text
import webbrowser
import weather
import os

def Action(data) :   
  
    user_data = data.lower()

    if "what is your name" in   user_data :
      text_to_speech.text_to_speech("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in user_data  or "hye" in user_data  or "hay" in user_data: 
        text_to_speech.text_to_speech("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  user_data :
            text_to_speech.text_to_speech("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in user_data or "thank" in user_data:
           text_to_speech.text_to_speech("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in user_data:
           text_to_speech.text_to_speech("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in user_data:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          text_to_speech.text_to_speech(Time)
          return str(Time) 

    elif "shutdown" in user_data or "quit" in user_data:
            text_to_speech.text_to_speech("ok sir")
            return "ok sir"  

    elif "play music" in user_data or "song" in user_data:
        webbrowser.open("https://open.spotify.com/")   
        text_to_speech.text_to_speech("Spotify is now ready for you, enjoy your music")                   
        return "Spotify is now ready for you, enjoy your music"


    elif 'open google' in user_data or 'google'  in user_data:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech("google open")  
        return "google open"

    elif 'open youtube' in user_data or "open youtube" in  user_data:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech("YouTube open") 
        return "YouTube open"    
    
    elif 'weather'  in user_data :
       ans   = weather.Weather()
       text_to_speech.text_to_speech(ans) 
       return ans

    elif 'music from my laptop' in user_data:
        url = 'C:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.text_to_speech("songs playing...")
        return "songs playing..." 

    else :
        text_to_speech.text_to_speech( "i'm able to understand!")
        return "i'm able to understand!"       
