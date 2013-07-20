import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores = {}
    for line in open(sys.argv[1]):
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in open(sys.argv[2]): 
        text = json.loads(line)
        if u'text' in text:
            tweet_msg = json.loads(line)[u'text']
            encoded_msg = tweet_msg.encode("utf-8")
            sentiment = 0
            for word in encoded_msg.split():
                if word in scores:
                    sentiment += scores[word]
            print sentiment
      
if __name__ == '__main__':
    main()



# afinnfile = open("AFINN-111.txt")
# scores = {} # initialize an empty dictionary
# for line in afinnfile:
#   term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
#   scores[term] = int(score)  # Convert the score to an integer.

# print scores.items() # Print every (term, score) pair in the dictionary
# print scores['protest']