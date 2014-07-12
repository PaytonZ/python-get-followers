import sys, json

class FileHelper:

	'''
	Returns the stream to a fileName given
	'''
	def openReadOnlyJSONFile(self, fileName):

		return self.openJSONFile(fileName, 'r')

	'''
	Returns an object from file in json format
	'''
	def openReadOnlyJSONFileASObject(self, fileName):

		json_data = self.openJSONFile(fileName, 'r')

		data = self.parseJSONDataToJSONObject(json_data)

		self.closeStream(json_data)

		return data

	'''
	Open a file in write mode
	Returns a stream
	'''
	def openWriteJSONFile(self, fileName):

		return self.openJSONFile(fileName, 'rw')

	'''
	Write data object into a file named fileName
	Returns True if no error occurred or False if an errror occurred
	'''
	def writeJSONDataToAFile(self, fileName, data):

		stream = self.openWriteJSONFile(fileName)

		return self.writeJSONDataToAStream(stream, data)

	'''
	Write data object into a stream
	Returns True if no error occurred or False if an errror occurred
	'''
	def writeJSONDataToAStream(self, stream, data):

		noError = True

		try:
			json.dump(data, stream)
		except:
			noError = False
			print "Error writting file"

		return noError and self.closeStream(stream)

	'''
	Parse a stream from a file in json format to a object
	Returns the object parsed
	'''
	def parseJSONDataToJSONObject(self, stream):
		return json.load(stream)

	'''
	Open a file with name fileName in indicated mode
	Returns a stream
	'''
	def openJSONFile(self, fileName, mode):

		try:
			return open(fileName, mode)
		except:
			print "parsing exception!"
			sys.exit(1)

	'''
	Close a stream
	Returns True if the file was closed successfully or False if not
	'''
	def closeStream(self, stream):

		if stream:
			stream.close()
			return True
		else:
			return False