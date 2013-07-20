import urllib
import json

def getTweetData():
	for i in range(1,11):
		response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(i))
		for element in json.load(response)[u'results']:
			tweet = element[u'text']
			encoded_string = tweet.encode('utf-8')
			print encoded_string
			print ''

if __name__ == "__main__":
	getTweetData()
