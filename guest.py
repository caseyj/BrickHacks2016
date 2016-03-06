

import json
import io

class Guest(object):

	preferences = ['Beef','Chicken','Plant based','Pork','Seafood']

	diets = ['Pescetarian','Lacto-ovo vegetarian', 'Lacto vegetarian', 'Ovo vegetaian', 'Vegan', 'Paleo']

	allergies = ['Sesame-Free','Seafood-Free','Tree Nut-Free', \
							'Peanut-Free', 'Egg-Free', 'Soy-Free', 'Gluten-Free', \
									'Wheat-Free', 'Dairy-Free', 'Sulfite-Free']

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
	def pref(self, pref):
		self._pref = pref

	@pref.deleter
	def pref(self):
		del self.pref

	##############################

	@property
	def diet(self):
		return self._diet

	@diet.setter
	def diet(self, diet):
		self._diet = diet

	@diet.deleter
	def diet(self):
		del self.diet

	def dietToString(self):
		diet = []
		output = ''
		for d in range( len(self._diet) ):
			if self._diet[d] == 1:
				diet.append( self.diets[d] )

		for i in range( len(diet) ):
			output = diet[i] + ' ' + output

		return output

	##############################

	@property
	def allergy(self):
		return self._allergy

	@allergy.setter
	def allergy(self, allergy):
		self._allergy = allergy

	@allergy.deleter
	def allergy(self):
		del self.allergy

	def allergyToString(self):
		allergy = []
		output = ''
		for d in range( len(self._allergy) ):
			if self._allergy[d] == 1:
				allergy.append( self.allergies[d] )

		for i in range( len(allergy) ):
			output = allergy[i] + ' ' + output

		return output

	##############################

	@property
	def exclude(self):
		return self._exclude

	@exclude.setter
	def exclude(self, exclude):
		self._exclude = exclude

	@exclude.deleter
	def exclude(self):
		del self.exclude

	def excludeToString(self):
		output = ''
		for i in range( len(self._exclude) ):
			output = self._exclude[i] + ' ' + output 
		return output
	
	##############################
	
	def toDict(self):
		di = dict()
		di['ID'] = self._ID
		di['name'] = self._name
		di['pref'] = list(self._pref)
		di['diet'] = list(self._diet)
		di['allergy'] = list(self._allergy)
		di['exclude'] = list(self._exclude)
		return di
		
	


if __name__ == '__main__':
	# beef, chicken, plant based, pork, seafood
	vic_pref = [0,0,1,0,0]
	john_pref = [0,0,0,1,0]
	victoria_pref = [0,1,0,0,0]
	danny_pref = [1,0,0,0,0]
	
	# pescetarian, vegetarian, laco vegetarian, ovo vegetarian, vegan, paleo
	vic_diet = [0,0,0,0,1,0]
	john_diet =  [0,0,0,0,0,0]
	victoria_diet = [0,0,0,0,0,0]
	danny_diet = [0,0,0,0,0,0]

	# sesame, seafood, treenut, peanut, egg, soy, gluten, wheat, dairy, sulfite 
	vic_allergy = [0,0,0,0,0,0,0,0,1,0] 
	john_allergy = [0,0,1,1,0,1,0,0,1,0]
	victoria_allergy = [0,0,0,0,0,0,0,0,0,0] 
	danny_allergy = [0,0,0,0,0,0,0,1,0,0] 

	vic_exclude =  ['Celery']
	john_exclude = ['Beef', 'Oatmeal'] 
	victoria_exclude = []
	danny_exclude = ['Tomato']

	vic = Guest( '9999', 'Vic', vic_pref, vic_diet, vic_allergy, vic_exclude )
	john = Guest( '8675', 'John', john_pref, john_diet, john_allergy, john_exclude)
	victoria = Guest( '1234', 'Victoria', victoria_pref, victoria_diet, victoria_allergy, victoria_exclude )
	danny = Guest( '8881', 'Danny', danny_pref, danny_diet, danny_allergy, danny_exclude )

	print vic.ID, vic.name, vic.pref, vic.allergy, vic.diet, vic.exclude
	print john.ID, john.name, john.pref, john.allergy, john.diet, john.exclude
	print victoria.ID, victoria.name, victoria.pref, victoria.allergy, victoria.diet, victoria.exclude
	print danny.ID, danny.name, danny.pref, danny.allergy, danny.diet, danny.exclude

	print john.dietToString()
	print john.allergyToString()
	print john.excludeToString()
	
	print vic.allergyToString()

	dvic = vic.toDict()
	#json.dumps(dvic)
	train = list([dvic, john.toDict(), victoria.toDict(), danny.toDict()])
	
	with open('data.json', 'wb') as outfile:
		json.dump(train, outfile)
