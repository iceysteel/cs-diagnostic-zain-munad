#didnt really have time to finish this problem :(

class Automobile(object):

	
	def __init__(self, color):
		super (Automobile, self).__init__()
		self.color = color
		
	# def honk():
	# 	print 'Beep Beep!'

	# def description():
	# 	print( self.number_of_wheels )
	# 	print( self.make )
	# 	print( self.model )
	# 	print( self.top speed )
	# 	print self.color

class Car(Automobile):

	#shouldnt all parts of the class be settable when the object is instatiated?
	def __init__(self, color):
		super (Car, self).__init__()
		self.number_of_wheels = 4
		self.make = 'chevy'
		self.model = 'cobalt'
		self.top speed = 125

		self.color = color
		
	def honk():
		print 'Beep Beep!'

	def description():
		print( self.number_of_wheels )
		print( self.make )
		print( self.model )
		print( self.top speed )
		print self.color

class SemiTruck(Automobile):

	#shouldnt all parts of the class be settable when the object is instatiated?
	def __init__(self, color):
		super (SemiTruck, self).__init__()
		self.number_of_wheels = 18
		self.make = 'chevy'
		self.model = 'big truck'
		self.top speed = 80

		self.color = color
		
	def honk():
		print 'Beep Beep!'

	def description():
		print( self.number_of_wheels )
		print( self.make )
		print( self.model )
		print( self.top speed )
		print self.color


