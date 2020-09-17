#!/usr/bin/python3.6

def formular(nume, varsta, cod_numeric_personal, serie_buletin, adresa):

	#Prima varianta

	#print("Va numiti: " + nume)
	#print("Aveti frumoasa varsta de: " + varsta)
	#print("Codul dvs. personal este: " + cod_numeric_personal)
	#print("Seria dvs. de buletin este: " + serie_buletin)
	#print("Adresa dvs. de domiciliu este: " + adresa)

	#A doua varianta

	print("Va numiti " + nume + ", aveti frumoasa varsta de " + varsta + " de ani.Codul dvs. numeric personal este " + cod_numeric_personal + ", iar seria dvs. este " + serie_buletin + ", domiciliul fiind situat in " + adresa +".")
	
	return


nume = input("Numele dvs. este: ")
varsta = input("Cati ani aveti(impliniti): ")
cod_numeric_personal = input("Introduceti codul numeric personal: ")
serie_buletin = input("Seria dvs este: ")
adresa = input("Adresa de domiciliu stabil: ")

formular(nume, varsta, cod_numeric_personal, serie_buletin, adresa)