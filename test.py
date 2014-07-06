
'''
Proudly made by JLPV
Program that get followers
Facebook
Twitter
Google+
Pinterest
Linkedin
Youtube


Linkedin requires
$ pip install python-linkedin
$ pip install requests
$ pip install requests_oauthlib
'''

import json
import urllib2
import httplib
import urllib
from linkedin import linkedin


print "Just a little try"
'''
twitter_api = "https://api.twitter.com/1.1/users/show.json?screen_name="
name_twitter= "rsarver"
twitter_token = "iOmJS41zSl21c7h6rhxyK5u9T"
twitter_token_secret ="FBVT6Azd0oSk9n4sEHDYrgjA8xwCXqmkrYwZvmjBp6sOW0ypSf"

params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
	"Accept": "text/plain"}
conn = httplib.HTTPConnection(twitter_api)
conn.request("POST", "", params, headers)
'''
#data = json.load(urllib2.urlopen(""))

print "Youtube Channel Followers Test"
youtube_api = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=%s&key="
#channel_id = "UCjKOqskq9R0LUTzA-Lj6Wmg"
channel_id = "UCuNY3eeP2gACgmorxbpxwuQ"
youtube_key = "AIzaSyD-e27-f9op5r1POt3bMWisERu-yrl1WBU"
final_youtube_url = youtube_api % channel_id  + youtube_key
data = json.load(urllib2.urlopen(final_youtube_url))
#decoded = json.loads(data)
 
print data['items'][0]['statistics']['subscriberCount']

# Google Plus
print "Google Plus Followers Test"
googleplusapi = "https://www.googleapis.com/plus/v1/people/%s?key="
id_googleplus = "113551191017950459231"
google_plus_final = googleplusapi % id_googleplus + youtube_key
data = json.load(urllib2.urlopen(google_plus_final))
print json.dumps(data['circledByCount'])

#Facebook
print "Facebook FOllowers Test"
facebook_api = "http://graph.facebook.com/%s"
facebook_id = "portal.baquia"
facebook_final = facebook_api % facebook_id
data = json.load(urllib2.urlopen(facebook_final))
print json.dumps(data['likes'])


'''Linkedin



API Key:

77bnwshr9m4k8m
Secret Key:

quxcGwVh5zjK3rLU
OAuth User Token:

89d8c97c-a47b-49c3-8303-9ba267d53d9e
OAuth User Secret:

5af9fab1-91ad-40f2-865f-9ed0c2f3f961


'''

linkedin_api_key = "77bnwshr9m4k8m"
linkedin_api_secret = "quxcGwVh5zjK3rLU"
RETURN_URL = 'http://localhost:8000'
authentication = linkedin.LinkedInAuthentication(linkedin_api_key, linkedin_api_secret, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)