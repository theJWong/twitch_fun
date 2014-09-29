import urllib2
import json

class PyTwitch(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.base_url = 'https://api.twitch.tv/kraken'

    def get_channel(self, name):
        try:
            url = self.base_url + '/channels/' + name
            contents = urllib2.urlopen(url)
            return json.loads(contents.read())
        except urllib2.HTTPError, err:
            if err.code == 404:
                raise Exception("Invalid channel name")
            else:
                raise Exception("Error: " + err)

#url = 'https://api.twitch.tv/kraken'
url = 'https://api.twitch.tv/kraken/channels/asdfasdfasdf23142435'
contents = urllib2.urlopen(url)
json_output = json.loads(contents.read())
output = json.dumps(json_output, sort_keys=True, indent=4, separators=(',', ': '))

print output