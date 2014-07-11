import sys, json

class FileHelper:

	def openReadOnlyJSONFile(self, fileName):

		return self.openJSONFile(fileName, 'r')

	def openReadOnlyJSONFileASObject(self, fileName):

		json_data = self.openJSONFile(fileName, 'r')

		data = self.parseJSONDataToJSONObject(json_data)

		self.closeStream(json_data)

		return data

	def openWriteJSONFile(self, fileName):

		return self.openJSONFile(fileName, 'rw')

	def parseJSONDataToJSONObject(self, json_data):
		return json.load(json_data)

	def openJSONFile(self, fileName, mode):

		try:
			return open(fileName, mode)
		except:
			print "parsing exception!"
			sys.exit(1)

	def closeStream(self, stream):

		stream.close()