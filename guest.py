import numpy

class Guest(object):

	def __init__(self, ID, name, pref, diet, allergy, exclude):
		self._ID = ID
		self._name = name
		self._pref = pref
		self._diet = diet
		self._allergy = allergy
		self._exclude = exclude

	##############################

	@property
	def ID(self):
		return self._ID

	@ID.setter
	def ID(self, ID):
		self._ID = ID

	@ID.deleter
	def ID(self):
		del self.ID

	##############################

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@name.deleter
	def name(self):
		del self.name

	##############################

	@property 
	def pref(self):
		return self._pref

	@pref.setter
	def pref(self, name):
		self._pref = pref

	@pref.deleter
	def pref(self):
		del self.pref

	##############################

	@property
	def diet(self):
		return self._diet

	@diet.setter
	def diet(self, name):
		self._diet = diet

	@diet.deleter
	def diet(self):
		del self.diet

	##############################

	@property
	def allergy(self):
		return self._allergy

	@allergy.setter
	def allergy(self, name):
		self._allergy = allergy

	@allergy.deleter
	def allergy(self):
		del self.allergy

	##############################

	@property
	def exclude(self):
		return self._exclude

	@exclude.setter
	def exclude(self, name):
		self._exclude = exclude

	@exclude.deleter
	def exclude(self):
		del self.exclude


if __name__ == '__main__':

	# pescetarian, vegetarian, laco vegetarian, ovo vegetarian, vegan, paleo
	vic_diet = numpy.asarray( [0,0,0,0,1,0] )
	john_diet = numpy.asarray( [0,0,0,0,0,0] )
	victoria_diet = numpy.asarray( [0,0,0,0,0,0] )
	danny_diet = numpy.asarray( [0,0,0,0,0,0] )

	# sesame, seafood, treenut, peanut, egg, soy, gluten, wheat, dairy, sulfite 
	vic_allergy = numpy.asarray( [0,0,0,0,0,0,0,0,1,0] )
	john_allergy = numpy.asarray( [0,0,1,1,0,1,0,0,1,0] )
	victoria_allergy = numpy.asarray( [0,0,0,0,0,0,0,0,0,0] )
	danny_allergy = numpy.asarray( [0,0,0,0,0,0,0,1,0,0] )

	vic_exclude = numpy.asarray( ['Celery'] )
	john_exclude = numpy.asarray( ['Beef'] )
	victoria_exclude = numpy.asarray( [''] )
	danny_exclude = numpy.asarray( ['Tomato'] )

	vic = Guest( '9999', 'Vic', 'Tofu', vic_diet, vic_allergy, vic_exclude )
	john = Guest( '8675', 'John', 'Pork', john_diet, john_allergy, john_exclude)
	victoria = Guest( '1234', 'Victoria', 'Chicken', victoria_diet, victoria_allergy, victoria_exclude )
	danny = Guest( '8881', 'Danny', 'Beef', danny_diet, danny_allergy, danny_exclude )

	print vic.ID, vic.name, vic.pref, vic.allergy, vic.diet, vic.exclude
	print john.ID, john.name, john.pref, john.allergy, john.diet, john.exclude
	print victoria.ID, victoria.name, victoria.pref, victoria.allergy, victoria.diet, victoria.exclude
	print danny.ID, danny.name, danny.pref, danny.allergy, danny.diet, danny.exclude


