from speech_recog import Recog
from tagger import Tagger
from processor import process

def run():
    print("start")
    listener = Recog()
    tagger =  Tagger()
    print("done setting up")
    while True:
        try:
            sentence = listener.listen()
            # sentence = "make line graph using range from A1 to E4"
            tags = tagger.match_rules(sentence)
            print(tags)
            process(tags)
        except KeyboardInterrupt:
            break
        except Exception as e:
            continue


if __name__ == "__main__":
    run()