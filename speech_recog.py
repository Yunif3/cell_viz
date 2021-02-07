import speech_recognition as sr

class Recog():
    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    # def await_trigger(self):
    
    def listen(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            word = self.r.recognize_google(audio)
            return word