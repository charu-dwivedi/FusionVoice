# NOTE: this requires PyAudio because it uses the Microphone class
from gtts import gTTS
import speech_recognition as sr
import os
import time
import pyglet
import pyaudio
import wave

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

def speech_play_test(voice_output):
     audio_file = "/Users/charu/Projects/FusionVoice/LangProcess/test.mp3"
     tts = gTTS(text=voice_output, lang="en")
     tts.save(audio_file)
     '''sound = pyglet.media.load(audio_file)
     sound.play()
     '''
     
     pygame.mixer.init()
     pygame.mixer.music.load(audio_file)
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
         continue
     pygame.mixer.music.stop()
     pygame.mixer.music.load("test2.mp3")
     

def audio_file_remove():
     audio_file = "test.mp3"
     os.remove(audio_file)
     #Cannot remove audio file, have to remove it when entire application close

def speechrec():
    playWav('/Users/charu/Projects/FusionVoice/LangProcess/ask.wav')
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    try:
        banana = r.recognize_google(audio, language = "en-us", show_all=False)   # recognize speech using Google Speech Recognition
        playWav('/Users/charu/Projects/FusionVoice/LangProcess/understood.wav')
        return banana
    except:                            # speech is unintelligible
        errormess = "Could not understand audio, please try again"
        speech_play_test(errormess)

def playWav(wavename):
    chunk = 1024
    f = wave.open(wavename, "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
    #read data  
    data = f.readframes(chunk)  

    #paly stream  
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  
    


