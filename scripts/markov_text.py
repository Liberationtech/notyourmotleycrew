from notyourmotleycrew.timelinejs.models import Event
from notyourmotleycrew.timelinejs.models import Filterset

import nltk
import random
import codecs

filterset = Filterset.objects.get(title="ful")
thenteset  = Filterset.objects.get(title="thentetest")

class MarkovModel:
    def __init__(self): 
        self.data = {}
    
    def add_text(self, text):

        tokens = nltk.word_tokenize(text)
        l = len(tokens)
        for i in range(l - 2):
            key = (tokens[i], tokens[i+1])
            value = tokens[i+2]
            
            if key not in self.data:
                self.data[key] = []
            self.data[key].append(value)
    
    def get_random_upper_case(self):
        """
        get a random key but the first word must begin with uppercase letter
        """
        done = False
        while not done:
            pair = random.choice(self.data.keys())
            if (pair[0][0]).isupper():
                result = pair
                done = True
        return result

    def get_sentence(self, n):
        result = u""

        stop = n
        done = 0
        #next_pair = random.choice(self.data.keys())
        next_pair = self.get_random_upper_case()
        result += u"{0}{1}{2}".format(next_pair[0], " " , next_pair[1])
        next_word = "A"
        while not (done > stop  and next_word in [".", "?", "!"]):
            while not next_pair in self.data:

                next_pair = self.get_random_upper_case()
                #next_pair = random.choice(self.data.keys())

            next_word = random.choice(self.data[next_pair])
            next_pair = (next_pair[1], next_word)

            done += 1
            result += u" {0}".format(next_word)
        
        return result

model = MarkovModel()


fn = "/tmp/output.txt"
fh = codecs.open(fn, "w", "utf-8")

def run():
    
    #build the model
    events = Event.objects.filter(filtersets=filterset)

    for event in events:
        model.add_text(event.text_body)
        #print model.data
    
    #for key, value in model.data.items():
        #print key, value
        #print len(value)

    for i in range(1000):
        sentence = model.get_sentence(25)
        fh.write(sentence)
        fh.write("\n\n")
