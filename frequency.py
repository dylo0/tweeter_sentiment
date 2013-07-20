import sys
import json

def main():
    occurencies = {}
    all_words = 0
    for line in open(sys.argv[1]): 
        tweet_line = json.loads(line)
        if 'text' in tweet_line:
            tweet_msg = json.loads(line)['text']
            encoded_msg = tweet_msg.encode("utf-8").split()
            all_words += len(encoded_msg)
            for word in encoded_msg:
                if word in occurencies:
                    occurencies[word] += 1
                else:
                	occurencies[word] = 1
    for k,v in occurencies.items():
        print k, v / float(all_words)


if __name__ == '__main__':
    main()
