"""
Michael Terranova
roll.py
A simple dice rolling simulator made for fun

how to use:
choose a die size (d2,d4,d6,d8,..) there is no limit to die size!
choose amount of rolls needed
1d20 will rolls a 20 sided die once
4d10 will roll 4 10 sided dice

####	#######  #######
#   #	   #	    #
####       #	    #
#	#      #        #
#	 #  #######     #
"""

import random

rolled = [] #store all our rolls so we can add for a sum if desired

"""
Our roll function
grabs a pseudo-randomly generated number bewteen 1 and x
x being the size of the die
"""
def randRoll(x):
	roll = random.randint(1,x)
	rolled.append(roll)

"""
Bring everything together so that it runs and prompts
"""
def main():
	inp = raw_input("Enter amount of rolls and die to use (eg: 1d4,2d8, ...): ")
	inpa = list(inp)
	n = 0
	for char in inpa:
		if char == 'd': #find where the d is so we know where rolls end and die begins
			break
		else:
			n += 1
	die = int(''.join(inpa[n+1:])) #die is the index of n+1 and the remaining string 
	rolls = int(''.join(inpa[:n])) #rolls is the index of n and everything before it
	while rolls != 0:
		rolls -= 1
		randRoll(die) #run our roll and add it to our list
	print rolled #print the rolled incase user wants to know the individual rolls
	print sum(rolled) #print the sum incase user wants a sum


main()