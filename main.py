import os
import wave
import openai
from whisperStuff import getTextFromAudio
from gptPrompt import gpt3
from gptPrompt import gpt3_5
import pyaudio
import keyboard


openai.api_key = os.getenv("OPENAI_API_KEY")

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

audioStream = p.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)

textmem = ''

frames = []
while(True):
    while(keyboard.is_pressed('a')):
        data = audioStream.read(CHUNK)
        frames.append(data)

    if(len(frames) != 0):
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        openedFile = open("output.wav", 'rb')
        transcribe = openai.Audio.transcribe("whisper-1", openedFile)
        userask = (f"user:{transcribe.text}")
        print(f"{userask}")
        textmem += userask
        frames.clear()
        textmem += "GPT:"
        answer = gpt3_5(textmem)
        print(f"GPT:{answer}")
        textmem += answer

    if keyboard.is_pressed('q'):
        break

print("recording stopped")
audioStream.stop_stream()
audioStream.close()
p.terminate()


# with audioStream as mic:
#     text = mic.read(CHUNK)
#     text = text.lower()

# recognizer = speech_recognition.Recognizer()
#
# while True:
#     try:
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = recognizer.listen(mic)
#
#             text = recognizer.recognize_google(audio)
#             text = text.lower()
#
#             print(text)
#         pass
#     except:
#         continue









