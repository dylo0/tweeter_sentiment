import sys
import json
import math

def main():
    scores = {}
    for line in open(sys.argv[1]):
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in open(sys.argv[2]): 
        tweet_line = json.loads(line)
        if 'text' in tweet_line:
            tweet_msg = json.loads(line)['text']
            encoded_msg = tweet_msg.encode("utf-8").split()
            sent_factor = 0
            for word in encoded_msg:
                if word in scores:
                    sent_factor += scores[word] ** 3
                else:
                	scores[word] = 0
            #na podstawie wspolczynnika tweeta dodaje do wszystkich wyrazow wspolczynnik, pierwsza czesc - cubic root
            diff = math.pow(abs(sent_factor),1.0/3) * (1,-1)[sent_factor<0] / float(len(encoded_msg))
            
            for word in encoded_msg:
            	scores[word] += diff
            	print word, str(scores[word])

if __name__ == '__main__':
    main()
