import sys
import json

def rate_tweet_sentiment(tweet_line, scores):
        text = json.loads(tweet_line)
        if u'text' in text:
            tweet_msg = json.loads(tweet_line)[u'text']
            encoded_msg = tweet_msg.encode("utf-8")
            sentiment = 0
            for word in encoded_msg.split():
                if word in scores:
                    sentiment += scores[word]
            return sentiment

def main():
    scores = {}
    for line in open(sys.argv[1]):
        term, score  = line.split("\t")
        scores[term] = int(score)

    states = {}
    with open(sys.argv[2]) as tweet_file:
        for line in tweet_file: 
            tweet_line = json.loads(line)
            if 'place' in tweet_line and tweet_line['place'] != None:
                if tweet_line['place']['country_code'] == 'US':
                    score = rate_tweet_sentiment(line, scores)
                    state = tweet_line['place']['full_name'][-2:]
                    if state not in states:
                        states[state] = [score]
                    else:
                        states[state].append(score)
    best = None
    for state in states:
        total_setiment = sum(states[state])/float(len(state))
        if not best or total_setiment > best[1]:
            best = (state, total_setiment)
    print best[0]
        

if __name__ == '__main__':
    main()

