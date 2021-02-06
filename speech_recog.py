import speech_recognition as sr

class Recog():
    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.r.adjust_for_ambient_noise(self.mic)

    # def await_trigger(self):
    
    def listen(self):
        print("listening now")
        audio = self.r.listen(self.mic)
        word = self.r.recognize_google(audio)
        return word