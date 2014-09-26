import urllib2
import json

url = 'https://api.twitch.tv/kraken'
contents = urllib2.urlopen(url)
json_output = json.loads(contents.read())
output = json.dumps(json_output, sort_keys=True, indent=4, separators=(',', ': '))

print output