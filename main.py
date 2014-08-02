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
v0.8 -- 10/07/2014 - GUI with listeners (MainGUI.py)
v0.9 -- 11/07/2014 - GUI more funcionality (load clients in a list) (MainGUI.py)
v0.10 -- 11/07/2014 - Helper for file management
v0.11 -- 11/07/2014 - Loadin followers on tableView (MainGUI.py)
v0.12 -- 11/07/2014 - Refactor methods on getFollowers module
v0.13 -- 12/07/2014 - helpers methods to write a file
v0.14 -- 12/07/2014 - linkedin working
v0.15 -- 16/07/2014 - account management full working
'''

import sys

import getFollowers
import accountManager

print "=========================================================="
print "Python Script for getting Followers in Social Networks"
print "The Script is given AS IS, dont blame the dev if it doesn't work"
print "If you're not agree , close this script immediately"
print "v0.14 -- 12/07/2014 - linkedin working"
print "=========================================================="



def get_followers():
	getFollowers.get_followers()

def account_manager():
	accountManager.menu()

def quit():
	sys.exit(0)

switch = {
	1 : get_followers,
	2 : account_manager,
	3 : quit
}

selection = raw_input("Insert an option: ")

if selection:
	
	num = int(selection)
	switch[num]()
