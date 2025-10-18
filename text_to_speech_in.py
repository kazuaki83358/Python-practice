import pyttsx3
def text_to_speech(text, output_file):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')       # get available voices
    engine.setProperty('voice', voices[1].id)   # select female voice
    engine.setProperty('rate', 160)             # speed of speech
    engine.setProperty('volume', 0.9)           # volume level between 0 and 1

    engine.say(text)

    engine.save_to_file(text, output_file)
    engine.runAndWait()

    print(f"Audio saved successfully as '{output_file}'")

with open("try.txt", "r") as file:
    txt = file.read().strip() 

text_to_speech(
    txt,
    "speech_output.mp3"
)