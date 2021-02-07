from speech_recog import Recog
from tagger import Tagger
from processor import process

def run():
    print("start")
    listener = Recog()
    tagger =  Tagger()
    sentence = listener.listen()
    # sentence = "make line graph using range from A1 to E4"
    tags = tagger.match_rules(sentence)
    print(tags)
    process(tags)


if __name__ == "__main__":
    run()