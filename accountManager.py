import sys
import json

def menu():

	print '*****ACCOUNT MANAGER*****'
	print ''
	print '0 - Show this menu'
	print '1 - Create a new client and his group of accounts'
	print '2 - Add a new social account'
	print '3 - Delete a new social account'
	print '4 - List actual accounts'
	print '5 - List actual clients'
	print '6 - To exit from accout manager'
	print ''

	switch = {
		0 : menu,
		1 : create_account_group,
		2 : add_account,
		3 : delete_account,
		4 : list_accounts,
		5 : list_clients,
		6 : quit
	}

	selection = raw_input("Insert an option: ")

	if selection:
	
		num = int(selection)
		switch[num]()

def create_account_group(name=None, accounts=None):

	if name:
		print 'crea la cuenta'
	else:
		print 'no la crea'

def add_account(name=None, account=None):

	print 'comming soon'

def delete_account(name=None, account=None):

	print 'comming soon'

def list_accounts(Name=None):

	filename = "data.txt"
	print "Trying to read data from %s" % filename
	try:
		json_data=open(filename)
		data = json.load(json_data)
		#pprint(data)
		print "Loaded %d Accounts" % len(data['clients'])
		json_data.close()
	except:
		print "parsing exception!"
		sys.exit()

	print 'Client list:'
	print ''

	for client in data['clients']:

		print client['name']
		print '- Accounts:'

		for account in client['accounts']:
			
			accountInfo = account.split(':')

			print '--' + accountInfo[0]
			print '--' + accountInfo[1]

def list_clients():

	filename = "data.txt"
	print "Trying to read data from %s" % filename
	try:
		json_data=open(filename)
		data = json.load(json_data)
		#pprint(data)
		print "Loaded %d Accounts" % len(data['clients'])
		json_data.close()
	except:
		print "parsing exception!"
		sys.exit()

	for client in data['clients']:

		print '--' + client['name']


def quit():
	sys.exit(0)