import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)


from Attack import phyAttack
from getStat import getSkillRoll, getSTR, getDEX, getCON, getWIL, getSPI, getMAN, getLCK
from Conditions import inflictCondition, cureCondition, setStance, pushTurn, pushDefender
from Core import menuChoice, multiMenuChoice, buffList, debuffList, getFolder, getPronoun
from Damage import newHPAmt
from Attack import abilityGate
from Header import menuChoiceBig, multiMenuChoiceBig, headerModule
#menuChoiceBig(itemList, headerQuestion)
#multiMenuChoiceBig(itemList, headerLine)
#headerModule()

# 0 == not usable
# 1 == usable (with penalty)
# 2 == recomended weapon!

favoredWeapons = {
	'heavy sword':	2,
	'light sword':	2,
	'light axe':	2,
	'heavy axe':	2,
	'dagger':		2,
	'club':			2,
	'gauntlet':		2,
	'chain':		2,
	'staff':		2,
	'lance':		2,
	'bow':			2,
	'wand':			2,
	'shield':		2
}

def flamingBile(attacker, offFolder, roomHeroes, roomMonsters):
	# HEADER METADATA
	degree = 0
	manaReq = 1				
	bothWepState = False
	abilityTicket, penaltyList, weaponMatrix = abilityGate(attacker, offFolder, manaReq, favoredWeapons, bothWepState)

	# PROCEED WITH ABILITY
	if abilityTicket == True:
		headerQuestion = attacker + " is using Fire Spray!\n--------------------------------\nWho is " + attacker + "'s target?"
		defender = menuChoiceBig(roomHeroes+roomMonsters, headerQuestion)
		defFolder = getFolder(defender, roomHeroes)

		buffList[0] += 1
		
		# CALL PHYATTACK
		damage, damageStyle = phyAttack(weaponMatrix[0], penaltyList, buffList, debuffList, offFolder, attacker, defFolder, defender, roomMonsters, roomHeroes, "fire")

		# PUSH TURNS
		pushTurn(offFolder, attacker, True)
		
		return degree
	
	# EJECT IF abilityTicket == FALSE
	else:
		return -1