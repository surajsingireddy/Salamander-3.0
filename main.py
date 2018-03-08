from os import listdir, system
import pickle
from character import *

def load():
	characters = []
	for file in listdir("Characters"):
		characters += pickle.load(open("Characters/"+file, "rb")),
		characters[-1].pos = 0
		characters[-1].curHP = characters[-1].maxHP
	return characters

def main():
	while True:
		print("Menu")
		print("---------------------------------------------")
		print("1. Combat")
		print("2. Make Character")
		i = int(input("\n"))
		system("cls")
		if i == 1:
			combat()
		elif i == 2:
			makeChar()

def makeChar():
	name = input("Name: ")
	playerClass = input("Class: ")
	if playerClass == "Fighter":
		playerClass = Fighter
	elif playerClass == "Rogue":
		playerClass = Rogue
	elif playerClass == "Sorcerer":
		playerClass = Sorcerer
	Character(name, playerClass)

def combat():
	characters = load()
	for i,c in enumerate(characters):
		c.pos = input("Where is "+c.name+"(0=fleeing)? ")
		if not c.pos: del characters[i]
		c.team = input("Which team is "+c.name+" on (1=Allies, 2=Enemies)? ")
	
	characters.sort(key=lambda c: c.name)
	characters.sort(key=lambda c: -c.speed)

	i = 0
	while True:
		if characters[i].curHP <= 0: continue
		action(i, characters)
		action(i, characters)
		i = (i+1)%len(characters)

def printBoard(characters):
	board = sorted(characters, key=lambda c: c.pos)
	pos = 0
	for char in board:
		if pos != char.pos:
			pos = char.pos
			print("Zone", char.pos, end=": ")
		print(char.name, end=" ")
	input("\n...")
	system("cls")

def action(i, characters):
	c = characters[i]
	printBoard(characters)
	print(c.name)
	input("\n...")
	system("cls")

main()