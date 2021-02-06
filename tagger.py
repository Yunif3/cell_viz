import spacy
from spacy.matcher import Matcher
import json
import collections

class Tagger():
    def __init__(self):
        self.sp = spacy.load("en_core_web_md")
        self.matcher = Matcher(self.sp.vocab)
        # add the patterns to extract
        with open("patterns.json", "r") as f:
            pattern_dict = json.load(f)
            for pattern_type, pattern in pattern_dict.items():
                self.matcher.add(pattern_type, pattern)


    def match_rules(self, sentence):
        sen = self.sp(sentence)
        matches = self.matcher(sen)
        tags = collections.defaultdict(list)
        print_pos(sen)
        for match_id, start, end in matches:
            pattern_type = self.sp.vocab.strings[match_id]  # Get string representation
            span = sen[start:end]  # The matched span
            tags[pattern_type].append(span.text)
            print(match_id, pattern_type, start, end, span.text)
        return tags


def print_pos(tokens):
    for word in tokens:
        print(f"{word.text:{12}} {word.pos_}")