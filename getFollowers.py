'''
Obatin the number of followers from serveral accounts
'''

import json
import urllib2
import httplib
import urllib
from linkedin import linkedin
from linkedin import server
from twython import Twython
from pprint import pprint
import sys

from helpers import FileHelper

import webbrowser
import BaseHTTPServer
import urlparse

def get_followers():
	filename = 'data.txt'
	print "Trying to read data from %s" % filename

	data = FileHelper().openReadOnlyJSONFileASObject(filename)

	for client in data['clients']:

		print "Loading account named ... \"%s\"" % client['name']

		for account in client['accounts']:
			fetch_for_all_accounts(account)

		'''
		Linkedin
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

		#pinterest_api_token ="MTQzMTU5NDozODY4ODc1NjE2NDcyNTY3NDU6NjU1MzV8MTQwNDc1OTM3NjoyNTkyMDAwLS1iZDM3NzU2NTVlNWViNTc1MjVhMDdkMzc2MjBjMmFmNQ%3D%3D"
		'''

	print "Have a nice day!"

def fetch_for_all_accounts(accountInfo):

	switchString = {
		'twitter' : get_twitter_followers,
		'youtube' : get_youtube_followers,
		'googleplus' : get_google_followers,
		'facebook' : get_facebook_followers,
		'pinterest' : get_pinterest_followers,
		#'linkedin' : get_linkedin_followers
	}
	
	account = accountInfo.split(':')
	if account and account[1] != '':
		print "acaaaaount --> " + account[1]
		if account[0] in switchString:
			return switchString[account[0]](account)

def get_twitter_followers(account):

	print "invocado twitter"

	if account[0] == 'twitter':
		try:
			twitter_token = "103836433-NhVUnFa94eVEa1YOdZQkl4qV77NiCfVp6888fYvI"
			twitter_token_secret ="qFvHq82TwQPkGK10yc6jMxqztz1tcBlWPVCKIRDe9BVWb"
			twitter_consumer_key = 'iOmJS41zSl21c7h6rhxyK5u9T'
			twitter_consumer_secret = 'FBVT6Azd0oSk9n4sEHDYrgjA8xwCXqmkrYwZvmjBp6sOW0ypSf'

			twitter = Twython(twitter_consumer_key, twitter_consumer_secret, oauth_version=2)
			ACCESS_TOKEN = twitter.obtain_access_token()
			twitter = Twython(twitter_consumer_key, access_token=ACCESS_TOKEN)
			twitter_account = account[1]
			followers = twitter.show_user(screen_name = twitter_account)

			print "Twitter followers of %s : %d" % (twitter_account , followers['followers_count'])

			return ['Twitter', str(twitter_account), str(followers['followers_count'])]
		except:
			return ['twitter' , 'problem found while getting twitter' , 0 ]

def get_youtube_followers(account):

	print "invocado youtube"

	if account[0] == 'youtube':
		try:
			youtube_api = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=%s&key="
			channel_id = account[1]
			youtube_key = "AIzaSyD-e27-f9op5r1POt3bMWisERu-yrl1WBU"
			final_youtube_url = youtube_api % channel_id  + youtube_key
			data = json.load(urllib2.urlopen(final_youtube_url))
			 
			print "Youtube followers of %s :" % channel_id  + str(data['items'][0]['statistics']['subscriberCount'])

			return [str('youtube'), str(channel_id), str(data['items'][0]['statistics']['subscriberCount'])]
		except:
			return [str('youtube'), 'found a prob in youtube', 0]

def get_google_followers(account):

	print "invocado googleplus"

	if account[0] == 'googleplus':
		try:
			googleplusapi = "https://www.googleapis.com/plus/v1/people/%s?key="
			id_googleplus = account[1]
			youtube_key = "AIzaSyD-e27-f9op5r1POt3bMWisERu-yrl1WBU"
			google_plus_final = googleplusapi % id_googleplus + youtube_key
			data = json.load(urllib2.urlopen(google_plus_final))
			print "Google+ followers of " + str(id_googleplus) +":"+ str(data['circledByCount'])

			return [str('google'), str(id_googleplus), str(data['circledByCount'])]
		except:
			return [str('google'), "found a problem in google", 0]

def get_facebook_followers(account):

	print "invocado facebook"
	
	if account[0] == 'facebook':
			try:
				facebook_api = "http://graph.facebook.com/%s"
				facebook_id = account[1]
				facebook_final = facebook_api % facebook_id
				data = json.load(urllib2.urlopen(facebook_final))
				print "Facebook followers of %s" % str(facebook_id) +":"+ str(data['likes'])

				return [str('facebook'), str(facebook_id), str(data['likes'])]
			except:
				return [str('facebook'), 'prob with facebook', 0 ]

def get_pinterest_followers(account):

	print "invocado pinterest"
	
	if account[0] == 'pinterest':
		try:
			pinterest_api_token = "MTQzMTU5NDozODY4ODc1NjE2NDcyNTY3NDU6NjU1MzV8MTQwNDc1OTM3NjoyNTkyMDAwLS1iZDM3NzU2NTVlNWViNTc1MjVhMDdkMzc2MjBjMmFmNQ=="
			pinterest_url = "https://api.pinterest.com/v3/users/%s/?access_token="
			pinterest_user = account[1]
			pinterest_final_url = pinterest_url % pinterest_user + pinterest_api_token
			data = json.load(urllib2.urlopen(pinterest_final_url))
			print "Pinterest followers of %s" % str(pinterest_user) +":"+ str(data['data']['follower_count'])

			return [str('pinterest'), str(pinterest_user), str(data['data']['follower_count'])]
		except:
			return [str('pinterest'), 'found a prob with pinterest', 0]

def get_linkedin_followers(account):

	print "invocado linkedin"
	
	if account[0] == 'linkedin':
		try:
			linkedin_api_key = "77bnwshr9m4k8m"
			linkedin_api_secret = "quxcGwVh5zjK3rLU"

			RETURN_URL = "http://localhost:8000"

			auth = linkedin.LinkedInAuthentication(linkedin_api_key, linkedin_api_secret, RETURN_URL, linkedin.PERMISSIONS.enums.values())

			application = linkedin.LinkedInApplication(authentication=auth)

			# Esto crea un pequenho servidor local para recuperar el codigo de autenticacion
			# antes de que expire el tiempo para obtener el token
			webbrowser.open_new(auth.authorization_url)

			tokenObtenido = _wait_for_user_to_enter_browser(application)

			application = linkedin.LinkedInApplication(token=tokenObtenido)
		
			assert application.authentication and application.authentication.token, 'Application bad built'
			info = application.get_company_updates(1035, params={'count': 2})
			print info
			return ['linkedin', '', 'in testing' ]
		except:
			print "error llamando a linkedin"

def _wait_for_user_to_enter_browser(app):
	class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
		def do_GET(self):
			p = self.path.split('?')
			if len(p) > 1:
				params = urlparse.parse_qs(p[1], True, True)
				app.authentication.authorization_code = params['code'][0]
				app.authentication.get_access_token()

	server_address = ('', 8000)
	httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
	httpd.handle_request()
	return app.authentication.token
