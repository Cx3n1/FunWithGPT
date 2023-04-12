import openai

def getTextFromAudio(file) -> str:
    openedFile = open(file, 'rb')
    transcribe = openai.Audio.transcribe("whisper-1", openedFile)
    return transcribe.text

