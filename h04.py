import random
# Mario Metshein
# 21.11.2023
# Ülesanne 04

#KUUBID
for i in range(1,11):
    print(f"{i:2} {i**2:4} {i**3:4}")

#PANK
raha = 10000
konto = raha
aastad = 5
intress = 0.05

print(f"Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range(aastad):
    print(f"{i+1:<7} {konto:.2f} {konto*0.05:9.2f} {konto + konto * intress:13.2f}")
    konto = konto + konto * intress

print(f"Summa kokku: {round(konto,2)}")
print(f"Kasum: {round(konto - raha,2)}")

input()
#WHILE+FOR - Avamismäng
loop = 1
kordadeArv = 0

while loop == 1:
    kordadeArv += 1
    print(f"Katse: {kordadeArv}")
    print("Arva arv 1-10\n-----------------")
    suvArv = random.randint(1,10)
    print(suvArv)

    for i in range(3):
        vastus = int(input("Sinu arv: "))
        if suvArv == vastus:
            print("Arvasid ära")
            break
        else:
            print("Proovi veel")
    print("Game Over")
    uusMang = input("Soovid uut mängu? jah/ei: ")
    if uusMang == "ei":
        loop = 0



#viisikud
for i in range(1,51):
    if i%5==0:
        print(i)

#pisike korrutustabel
for j in range(1,11):
    for i in range(1,11):
        print(f"{j} x {i} = {j*i}")


#paaris/paaritu
for arv in range(11):
    if arv % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(arv, v)

#loto
for x in range(5):
    print(random.randint(0,9),end="")


print()
#tärnid

j = 5
for i in range(5):
    print("* "*j)
    #j = j - 1
    j -= 1

print()
j = 5
for i in range(j):
    print("* "*(i+1))
print()
j = 5
for i in range(j):
    print("* "*j)

    
print()

#jalka
sugu = "mees"
if sugu == "apache":
    vanus = 10
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast meeskonda!")
    else:
        print("Vanus ei sobi")
else:
    print("Ei pääse meeskonda")

#müük
hind = 20
if hind <= 10:
    ale = 0.1
else:
    ale = 0.2
    
vastus = hind - hind * ale
print(f"Sinu soodushind on {vastus}€")


# juubel
v = 20
if v % 5 == 0:
    vastus = "on"
else:
    vastus = "ei ole"
print(f"Vanus {v}: {vastus} juubel")





#21.11

"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm
    küsib kasutajalt, mis tehet ta soovib (+-*/)
    ning viib kasutaja valiku ellu.
    Koosta vastab plokkskeem ja salvesta
    see samasse kataloogi programmiga.
"""

nr1 = int(input("arv1: "))
nr2 = int(input("arv2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "ära pulli mees!"
    
print(f"{nr1} {tehe} {nr2} = {vastus}")


"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm
    tuvastab kas tegemist saab olla ruuduga.
    Koosta vastab plokkskeem ja salvesta
    see samasse kataloogi programmiga.
    ==
    !=
    > < >= <=
"""
nr1 = int(input("Ruudu 1. külg: "))
nr2 = int(input("Ruudu 2. külg: "))

if nr1 == nr2:
    print("ruut")
else:
    print("mingi muu asi")
