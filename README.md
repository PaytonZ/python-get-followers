python-get-followers
====================

Program that tries to automate the process to get the number of followers of certain social networks

"Should" be compatible with (list below) and have a 'good' way to manage accounts
*   Facebook
*   Twitter
*   Google +
*   Pinterest
*   Linkedin
*   Youtube

REQUIRED MODULES
================

PySide 1.2.1 
	should be enough for Windows
	or
	go to http://qt-project.org/wiki/Get-PySide for other platforms

Qt 4.8

Linkedin requires
https://github.com/ozgur/python-linkedin
$ pip install python-linkedin
$ pip install requests
$ pip install requests_oauthlib

Twitter requires
$ pip install twython

DEVELOPERS TOOLS
================

compileGUI.sh -> is a script that generate a python gui code from .ui files (QDesigner and QCreator format descriptor for guis)
