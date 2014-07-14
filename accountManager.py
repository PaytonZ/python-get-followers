import sys
import json
from helpers import FileHelper

def menu():

	print '*****ACCOUNT MANAGER*****'
	print ''
	print '0 - Show this menu'
	print '1 - Create a new client and his group of accounts'
	print '2 - Add a new social account'
	print '3 - Delete a new social account'
	print '4 - Delete client and his accounts'
	print '5 - List actual accounts'
	print '6 - List actual clients'
	print '7 - To exit from accout manager'
	print ''

	switch = {
		0 : menu,
		1 : create_account_group,
		2 : add_account,
		3 : delete_account,
		4 : delete_client,
		5 : list_accounts,
		6 : list_clients,
		7 : quit
	}

	selection = raw_input("Insert an option: ")

	if selection:
	
		num = int(selection)
		switch[num]()

def create_account_group(name=None, accounts=None, console=True):

	fileHelper = FileHelper()

	data = fileHelper.openReadOnlyJSONFileASObject('data.txt')

	if name:
		print 'crea la cuenta'

		clients = data['clients']

		if name not in clients:
			clients[name] = accounts

			fileHelper.writeJSONDataToAFile('data.txt', data)

	elif console:
		clientName = raw_input('Insert the clien name: ')

		twitter = 'twitter:' + raw_input('Insert the twitter account (left blank if you dont have one): ')
		youtube = 'youtube:' + raw_input('Insert the youtube account (left blank if you dont have one): ')
		googleplus = 'googleplus:' + raw_input('Insert the googleplus account (left blank if you dont have one): ')
		linkedin = 'linkedin:' + raw_input('Insert the linkedin account (left blank if you dont have one): ')
		facebook = 'facebook:' + raw_input('Insert the facebook account (left blank if you dont have one): ')
		pinterest = 'pinterest:' + raw_input('Insert the pinterest account (left blank if you dont have one): ')

		if clientName:
			clients = data['clients']

			if clientName not in clients:
				i = len(clients)
				clients.append({ 'name':clientName, 'accounts':[ twitter, youtube, googleplus, linkedin, facebook, pinterest ]})

				fileHelper.writeJSONDataToAFile('data.txt', data)

def add_account(name=None, account=None):

	print 'comming soon'

def delete_account(name=None, account=None):

	fileHelper = FileHelper()

	data = fileHelper.openReadOnlyJSONFileASObject('data.txt')

	clients = data['clients']

	if name and account:
		for client in clients:
			if client == name:
				for ac in client['accounts']:
					if ac == account:
						client['accounts'].remove(cuenta)
						break
				break
	else:
		nombre = raw_input("Write the client account owner: ")
		cuenta = raw_input("Write the account name: ")

		for client in clients:
			if client['name'] == nombre:
				accounts = client['accounts']
				for ac in range(0, len(accounts)):
					if client['accounts'][ac].split(':')[0] == cuenta:
						client['accounts'].pop(ac)
						print 'Deleted account: ' + cuenta
						break
				break

	fileHelper.writeJSONDataToAFile('data.txt', data)

	print '**Deleted account**'

def delete_client(name=None):

	fileHelper = FileHelper()

	data = fileHelper.openReadOnlyJSONFileASObject('data.txt')

	clients = data['clients']

	if name:
		for client in clients:
			if client['name'] == name:
				clients.remove(name)
				print 'Removed client: ' + name
				break
	else:
		nombre = raw_input("Write the client account owner: ")
		i = 0
		for client in clients:
			if client['name'] == nombre:
				cli = clients[i]
				clients.remove(cli)
				print 'Removed client: ' + nombre
				break
			i = i + 1

	fileHelper.writeJSONDataToAFile('data.txt', data)

def list_accounts(name=None):
	data = FileHelper().openReadOnlyJSONFileASObject('data.txt')
	print "Loaded %d Accounts" % len(data['clients'])

	if name:
		print "no esta hecho"
	else:

		print 'Client list:'
		print ''

		for client in data['clients']:

			print client['name']
			print '- Accounts:'

			for account in client['accounts']:
				
				accountInfo = account.split(':')

				print '  --' + accountInfo[0] + ' : ' + accountInfo[1]

def list_clients():
	data = FileHelper().openReadOnlyJSONFileASObject('data.txt')
	print "Loaded %d Accounts" % len(data['clients'])

	for client in data['clients']:

		print ' --' + client['name']


def quit():
	sys.exit(0)