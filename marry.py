import sys
import random

def genPrefTables(n):
	values = [x for x in range(n)]
	for i in range(n):
		for j in range(n):
			selection = random.choice(values)
			maleTable[i][j] = selection
			values.remove(selection)
		values = [x for x in range(n)]
	for i in range(n):
		for j in range(n):
			selection = random.choice(values)
			femaleTable[i][j] = selection
			values.remove(selection)
		values = [x for x in range(n)]
	print "\nRandomly-Generated Male Preferences Table:\n", maleTable
	print "\nRandomly-Generated Female Preferences Table:\n", femaleTable

def printResults(dudes):
	print "\nResults:"
	for i in range(n):
		print "\nDude ", i, " Chick ", dudes[i]

def stableMatching(n):
	mec = [0 for i in range(n)]
	nana = [0 for i in range(n)]
	#k = guy[k]
	k = 0
	r = 0
	singleCount = 0
	proceed = True
	while proceed:
		#Starts the 1st round or a round where the next female
		#on guy k's list is single
		if nana[maleTable[k][r]] == 0:
			mec[k] = nana[maleTable[k][r]]
			nana[maleTable[k][r]] = mec[k]
		else:
			for i in range(n):
				if femaleTable[maleTable[k][r][i]] == nana[maleTable[k][r]]:
					rank_current = i
				elif femaleTable[maleTable[k][r][i]] == k:
					rank_prospect = i
			if rank_prospect > rank_current:
				nana[maleTable[k][r]] = k
				mec[k] = maleTable[k][r]
				mec[femaleTable[maleTable[k][r]][rank_current]] = 0
			k = k + 1
			if k > n - 1:
				k = 0s
		for i in range(n):
			if mec[i] == 0:
				singleCount = singleCount + 1
		if singleCount > 0:
			proceed = True
		else:
			proceed = False
	printResults(mec)

if(len(sys.argv) < 2):
	print "Usage: \'marriage.py n\' where n is the number of couples."
else:
	n = int(sys.argv[1])
	maleTable = [[0 for i in range(n)] for j in range(n)]
	femaleTable = [[0 for i in range(n)] for j in range(n)]
	genPrefTables(n)
	stableMatching(n)