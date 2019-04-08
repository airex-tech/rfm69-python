class Logger():
	def __getattr__(self, name):
		def method(*args):
			if args:
				print(name + ": " + str(args))
		return method

def getLogger(name):
	return Logger()