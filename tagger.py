import spacy
from spacy.matcher import Matcher

graph_pattern = [{"POS": "NOUN"}, {"LOWER": "graph"}]
cell_pattern = [{"LOWER": "cell"}, {"POS": "NOUN"}]
class Tagger():
    def __init__(self):
        self.sp = spacy.load("en_core_web_md")
        self.matcher = Matcher(self.sp.vocab)


    def match_rules(self, sentence):
        self.matcher.add("GraphType", [graph_pattern])
        self.matcher.add("CellType", [cell_pattern])
        sen = self.sp(sentence)
        matches = self.matcher(sen)
        print_pos(sen)
        for match_id, start, end in matches:
            string_id = self.sp.vocab.strings[match_id]  # Get string representation
            span = sen[start:end]  # The matched span
            print(match_id, string_id, start, end, span.text)
    

    def tag_pos(self, sentence):
        sen = self.sp(sentence)
        print_pos(sen) 


def print_pos(tokens):
    for word in tokens:
        print(f"{word.text:{12}} {word.pos_}")