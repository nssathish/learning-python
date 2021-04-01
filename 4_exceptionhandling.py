try {
# operation
}
catch(Exception ex) {
	# handling the exception
}
finally {
}

try:
	# do something

except ValueError as ex:




def chumma(value):
	try:
		#do someging
		# doing something
		# exception thrown
		obj = GoogleAPI(value)
		if obj is None:
			raise('object not found in google api')
		print ( 1/ 0)
	except Exception as ex:
		print('value error stacktrace: ' + ex.with_traceback())
	finally:
		



if __name__ == "__main__":
	chumma(5)
