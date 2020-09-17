#!/usr/bin/python3.6

f = open("/home/bogdan/Desktop/functii.py", "r")

#r/w - adaugam drept de citire/scriere#
#r+/w+ - adaugam drept de citire si scriere#
#a - "append" adauga text la finalul fisierului#

text = " "

while text != '': #atata timp cat nu gaseste nimic...practic citeste tot fisierul ptc in fisier avem informatii#
	text = f.read(50) #sa citeasca doar 25 de bytes din fisier)
	print (text)

f.close()


r = open("/home/bogdan/Desktop/functii2.py", "w")
print ("Writing in file...")
r.write("Text for python\n")

print("Done with writting")

r.close()