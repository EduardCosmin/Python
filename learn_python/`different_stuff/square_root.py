#Aflarea patratelor perfecte

import math

n=int(input("Introdu un numar natural:"))
if math.sqrt(n)*math.sqrt(n)==n:
    print("Este patrat pefect")
else:
    print("Nu este patrat perfect")

 