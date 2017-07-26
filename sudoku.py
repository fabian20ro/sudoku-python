matrice = [
	[8, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 3, 6, 0, 0, 0, 0, 0],
	[0, 7, 0, 0, 9, 0, 2, 0, 0], 
	[0, 5, 0, 0, 0, 7, 0, 0, 0],
	[0, 0, 0, 0, 4, 5, 7, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 3, 0],
	[0, 0, 1, 0, 0, 0, 0, 6, 8],
	[0, 0, 8, 5, 0, 0, 0, 1, 0],
	[0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def afiseazaMatricea():
	for rand in matrice:
		print rand
	print ""

nums = range (1, 10)
cols = range (0, 9)
ranges = [[0,1,2],[0,1,2],[0,1,2],[3,4,5],[3,4,5],[3,4,5],[6,7,8],[6,7,8],[6,7,8]]

def potPuneNumarul(numarul, linie, coloana):
	if matrice[linie][coloana] != 0:
		return matrice[linie][coloana] == numarul
	for element in matrice[linie]:
		if element == numarul:
			return False
	for index in cols:
		if numarul == matrice[index][coloana]:
			return False
	for i in ranges[linie]:
		for j in ranges[coloana]:
			if numarul == matrice[i][j]:
				return False
	return True

def afiseazaSolutiile(linie, coloana):
	if linie == 9:
		print "Solutia este:"
		afiseazaMatricea()
	else:
		numarExistent = matrice[linie][coloana]
		for n in nums:
			if potPuneNumarul (n, linie, coloana):
				matrice[linie][coloana] = n
				if coloana == 8:
					afiseazaSolutiile(linie + 1, 0)
				else:
					afiseazaSolutiile(linie, coloana + 1)
			matrice[linie][coloana] = numarExistent

print "Matricea initiala este:"
afiseazaMatricea()

afiseazaSolutiile(0, 0)
