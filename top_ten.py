import sys
import json


def main():
    tags = {}
    with open(sys.argv[1]) as tweet_file:
        for line in tweet_file: 
            tweet_line = json.loads(line)
            if 'entities' in tweet_line and tweet_line['entities']['hashtags'] != []:
                for tag in tweet_line['entities']['hashtags']:
                    key = tag['text']
                    if key not in tags:
                        tags[key] = 1
                    else:
                        tags[key] += 1
    sorted_tags = sorted(tags.items(), key = lambda num: num[1], reverse = True )
    for i in range(10):
        print sorted_tags[i][0], float(sorted_tags[i][1])


if __name__ == '__main__':
    main()

