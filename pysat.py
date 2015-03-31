#!/usr/bin/python

import sys

def tokenize(phrase):
	"""A simple wrapper to tokenize the inputed Boolean equation. Currently \
	it only tokenizes based on the space character. In the future the \
	internals may be expanded to allow for parentheses and other symbols. \
	"""
	return phrase.split(" ")

def findInputsInPhrase(phrase):
	"""Seeks out all variables named in the boolean equation input. \
	Returns a list containing all unique identifiers. """
	tokens = tokenize(phrase)
	inputs = []
	for token in tokens:
		if token not in ["and", "or", "not"] and token not in inputs:
			inputs.append(token)
	inputs.sort()
	return inputs;
	
def replaceWithTruthLiterals(phrase, inputs, truths):
	"""Taking in the Boolean equation, the list of inputs, and the \
	generated truth value input table, this function replaces all \
	variables named in the equation with the Boolean literals."""
	newphrase = []
	for item in tokenize(phrase):
		if item in inputs:
			newphrase.append(str(truths[inputs.index(item)]))
		else:
			newphrase.append(item)
	return newphrase

def makeTruthTable(numInputs):
	"""This function generates all possible inputs to the Boolean \
	equation. The number of truth value input sets is equal to \
	2^n, where n is the number of variables in the equation. \
	"""
	numberOfTruthPermutations = pow(2, numInputs)
	truthtable = []
	truthrow = [False] * numInputs
	for i in range(0, numberOfTruthPermutations):
		carry = False
		for j in range(0, numInputs):
			if truthrow[j] == False:
				truthrow[j] = True
				break
			else:
				carry = True
				truthrow[j] = False
				continue
		truthtable.append(list(truthrow))
	return truthtable

def main():
	# Take the first argument after the program name as the equation. 
	phrase = sys.argv[1]
	inputs = findInputsInPhrase(phrase);

	# Generate the Boolean literal inputs. 
	truthtable = makeTruthTable(len(inputs))

	# Test all possible inputs to the equation. 
	satsolutions = []
	print "Evaluating \"" + phrase + "\"..."
	for row in truthtable:
		testme = replaceWithTruthLiterals(phrase, inputs, row)
		testme = " ".join(testme)
		if eval(testme) == True:
			satsolutions.append(row)
	
	# If there are any solutions, output them now. 
	if len(satsolutions) > 0:
		print "The following truth values satisfy the equation: "
		for sol in satsolutions:
			print sol
	# There may be no solutions. 
	else:
		print "The equation is not satisfiable. "

if __name__ == "__main__":
	main()

