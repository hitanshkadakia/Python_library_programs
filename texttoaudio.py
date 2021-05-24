from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
print("Enter the text which you want to convert to audio:")
Text=input()
sp = gTTS(Text,lang='en',slow=False)
sp.save(audio)
playsound(audio)