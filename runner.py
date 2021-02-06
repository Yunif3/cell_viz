from speech_recog import Recog
from tagger import Tagger

def run():
    print("start")
    listener = Recog()
    tagger =  Tagger()
    # sentence = listener.listen()
    sentence = "get range from D5 to D6 and cell A4 and cell A5"
    print(tagger.match_rules(sentence))


if __name__ == "__main__":
    run()