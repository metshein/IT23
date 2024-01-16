# Mario Metshein IT23 
# 16.01.24

import random
print("\n--------------------------------------------------\n")

print("\n--------------------------------------------------\n")

# 7. Eurokalkulaator
# koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# küsitakse valuuta kogust ja tehakse arvutused - 2p

def eur_kalk(arv, valik):
    try:
        if valik == "EUR":
            return arv * 15.6466
        else:
            return arv / 15.6466
    except:
        print("Midagi läks katki, kontrolli sisestust") 
try:
    while True:
        valuuta = input("Mis valuuta sul on (EUR/EEK)")
        if valuuta.upper() == "EUR" or valuuta.upper() == "EEK":
            valuuta_kogus = float(input("Mitu raha sul on: "))
            print(eur_kalk(valuuta_kogus, valuuta))
            break
        else:
            print("Pidid valmima EUR või EEK")
except:
    print("Midagi läks katki, kontrolli sisestust") 


 
print("\n--------------------------------------------------\n")
# 5. Shopping List
# Create a program that will keep track of items for a shopping list. 
# The program should keep asking for new items until nothing is entered (no input followed by enter/return key). 
# The program should then display the full shopping list.

shopping_list = []
while True:
    item = input("Lisa toode: ")
    if not item:
        break
    shopping_list.append(item)
print("Items in list")
for i in shopping_list:
    print(i,end=",")

print("\n--------------------------------------------------\n")
# 3. Positiivsed ja negatiivsed
# 	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
# 	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
# 	nulli lisamisel ei tehta midagi 1p
# 	väljasta mõlemad loendit 1p
        
pos = []
neg = []

kord = 0

while kord < 5:
    arv = int(input("Sisesta täisarv: "))
    if arv > 0:
        pos.append(arv)
        kord+=1
    elif arv < 0:
        neg.append(arv)
        kord+=1
    else:
        print("Ära nulli lisa!")

print(pos)
print(neg)
print("--------------------------------------------------")
# 1. Korrutamise kontrollimine
# 	programm esitab korrutustehte
# 	ootab kasutajalt vastuse sisestamist
# 	kontrollib vastuse õigsust
# 	väljastab, kas vastus oli õige või väär.
# 	kokku antakse lahendamiseks 10 ülesannet.

def korrutamine(a,b):
    return a*b

for i in range(10):
    arv1 = random.randint(1,5)
    arv2 = random.randint(1,5)
    kasutaja = int(input(f"{arv1} * {arv2} = "))
    if korrutamine(arv1,arv2)== kasutaja:
        print(f"ÕIGE: {arv1} * {arv2} =  {korrutamine(arv1,arv2)}")
    else:
        print(f"VALE! Õige vastus on {arv1} * {arv2} = {korrutamine(arv1,arv2)}")


