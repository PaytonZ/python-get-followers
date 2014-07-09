'''
Proudly made by JLPV and DST to FM
Script that get followers from:
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

Twitter requires
$ pip install twython

Pinterest Token should be renewed after 1 http://month/
https://www.pinterest.com/oauth/?consumer_id=1431594&response_type=token

Versions
---------------
v0.1 -- 07/07/2014 - Working All Networks except Linkedin"
v0.2 -- 07/07/2014 - File data.txt inserting data in json format
'''

import sys

import getFollowers
import accountManager

print "=========================================================="
print "Python Script for getting Followers in Social Networks"
print "The Script is given AS IS, dont blame the dev if it doesn't work"
print "If you're not agree , close this script immediately"
print "v0.3 -- 09/07/2014 - Menu and account manager"
print "=========================================================="

print '*****SOCIAL NETWORK MANAGER*****'
print ''
print '1 - Get followers from existing accounts'
print '2 - Open account manager'
print '3 - To exit from social network manager'
print ''

def get_followers():
	getFollowers.get_followers()

def account_manager():
	accountManager.menu()

switch = {
	1 : get_followers,
	2 : account_manager,
	3 : quit
}

selection = raw_input("Insert an option: ")

if selection:
	
	num = int(selection)
	switch[num]()
