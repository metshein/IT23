import random
# Mario Metshein
# 21.11.2023
# Ülesanne 04

nimi = "sdgdfg"
arv = 155.4854165156151
print(f"Tere {arv:.2f}")


#PANK
raha = 10000
aasta = 5
konto = raha
intress = 0.05

print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range(aasta):
    print(f"{i+1} {konto:14.2f} {konto*intress:9.2f} {konto+konto*intress:13.2f}")
    konto = konto + konto * intress

print(f"Summa kokku: {konto:.2f}€")
print(f"Kasum: {konto-raha:.2f}€")


input()

#arvamismäng WHILE+FOR
loop = 1
voidud = 0

while loop == 1:
    print("--------- ARVAMISMÄNG ---------")
    suv = random.randint(1,3)
    #print(suv)
    for i in range(3):
        arva = int(input("Paku arv 1-3: "))
        if suv == arva:
            print("Arvasid ära!")
            voidud += 1
            break
        else:
            print("Proovi veel!")
    print("--------- GAME OVER ---------")
    print(f"Võidud: {voidud}")
    jatka = input("Soovid jätkata? y/n: ")
    if jatka == "n":
        loop = 0


input()
#Viisikud
for i in range(1,101):
    if i%5 == 0:
        print(i)

input()
#Pisike korrutustabel
for j in range(1,11):
    for i in range(1,11):
        print(f"{j} x {i} = {j*i}")
