#!/usr/bin/python3.6

# valoare = input("Introdu un numar: ")

# def calcul_suma(valoare):
# 	suma = 0
# 	for i in range(int (valoare) + 1):
# 		suma = suma + i
# 	return suma

# rezultat = str(calcul_suma(valoare))
# print ("Suma pentru " + valoare + " este " + rezultat)

#Calculeaza suma nerelor numarului introdus#




def calcul_persoana(nume, varsta):
	print("Ok, te numesti " + nume+ " si ai " + varsta + " ani")

	ani=int(varsta) + 20
	print("Peste 20 de ani vei avea: " + str(ani) + " de ani!")

	return

nume = input("Salut! Cum te numesti:")
varsta=input("Cati ani ai:")


calcul_persoana(nume, varsta)

#Afiseaza numele tau si varsta si cati ani vei avea peste 20 de ani#