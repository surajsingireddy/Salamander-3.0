import pickle

class Character:
	def __init__(self, name, playerClass):
		try:
			self = pickle.load(open("Characters/"+name+".p", "rb"))
		except:
			self.name = name
			self.playerClass = playerClass
			self.level = 1
			self.pos = 0
			self.team = 0
			self.initStats()
			self.save()

	def initStats(self):
		x = (self.level + 1) / 2
		self.strength = self.playerClass.strength * x
		self.defense = self.playerClass.defense * x
		self.magic = self.playerClass.magic * x
		self.will = self.playerClass.will * x
		self.constitution = self.playerClass.constitution * x
		self.speed = self.playerClass.speed
		self.maxHP = self.constitution * 4
		self.curHP = self.maxHP

	def save(self):
		pickle.dump(self, open("Characters/"+self.name+".p", "wb"))

class Class:
	def __init__(self, strength, defense, magic, will, constitution, speed):
		self.strength = strength
		self.defense = defense
		self.magic = magic
		self.will = will
		self.constitution = constitution
		self.speed = speed

Fighter = Class(5, 5, 3, 3, 5, 3)
Rogue = Class(6, 3, 3, 4, 4, 4)
Sorcerer = Class(3, 3, 6, 4, 4, 2)