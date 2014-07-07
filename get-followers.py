
'''
Proudly made by JLPV to FM
Program that get followers
Facebook
Twitter
Google+
Pinterest
Linkedin
Youtube


Linkedin requires
https://github.com/ozgur/python-linkedin
$ pip install python-linkedin
$ pip install requests
$ pip install requests_oauthlib

from twython import Twython
https://github.com/bear/python-twitter

'''

import json
import urllib2
import httplib
import urllib
from linkedin import linkedin
from twython import Twython


print "=========================================================="
print "Python Script for getting Followers in Social Networks"
print "The Script is given AS IS, dont blame the dev if it dont work"
print "If you're not agree , close this script inmediatly"
print "=========================================================="



twitter_token = "103836433-NhVUnFa94eVEa1YOdZQkl4qV77NiCfVp6888fYvI"
twitter_token_secret ="qFvHq82TwQPkGK10yc6jMxqztz1tcBlWPVCKIRDe9BVWb"
twitter_consumer_key = 'iOmJS41zSl21c7h6rhxyK5u9T'
twitter_consumer_secret = 'FBVT6Azd0oSk9n4sEHDYrgjA8xwCXqmkrYwZvmjBp6sOW0ypSf'


twitter = Twython(twitter_consumer_key, twitter_consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(twitter_consumer_key, access_token=ACCESS_TOKEN)
followers = twitter.show_user(screen_name = 'katyperry')

print "Twitter followers? %d" % followers['followers_count']


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




linkedin_api_key = "77bnwshr9m4k8m"
linkedin_api_secret = "quxcGwVh5zjK3rLU"
RETURN_URL = 'http://localhost:8000'
authentication = linkedin.LinkedInAuthentication(linkedin_api_key, linkedin_api_secret, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)
authentication.authorization_code = raw_input("Insert here the auth token: ")
token = authentication.get_access_token()
application = linkedin.LinkedInApplication(token='AQTPEQE-tb9zYCFwqDK9KAt8oboIPL4A9cGip9LYNxltYXwDFJVCnreE6rJ_GQRxHPXPj4d0dUcR4PqSRjsgudOeZfyPBV9De11Hr1M2bK0YILV-it')
application.get_company_updates(1035, params={'count': 2})
'''
#pinterest_api_token ="MTQzMTU5NDozODY4ODc1NjE2NDcyNTY3NDU6NjU1MzV8MTQwNDc1OTM3NjoyNTkyMDAwLS1iZDM3NzU2NTVlNWViNTc1MjVhMDdkMzc2MjBjMmFmNQ%3D%3D"
pinterest_api_token = "MTQzMTU5NDozODY4ODc1NjE2NDcyNTY3NDU6NjU1MzV8MTQwNDc1OTM3NjoyNTkyMDAwLS1iZDM3NzU2NTVlNWViNTc1MjVhMDdkMzc2MjBjMmFmNQ=="
pinterest_url = "https://api.pinterest.com/v3/users/%s/?access_token="
pinterest_user = "baquia"
pinterest_final_url = pinterest_url % pinterest_user + pinterest_api_token
data = json.load(urllib2.urlopen(pinterest_final_url))
print json.dumps(data['data']['follower_count'])


