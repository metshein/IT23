#M.Metshein
#5.12.23
import math

def kera(r):
    v = round((4*math.pi*r**3)/3,2)
    print(f"Kera ruumala on {v}")

def kuup(a):
    v = a**3
    print(f"Kuubi ruumala on {v}")

def koonus():
    print(f"Koonuse ruumala on ")

def silinder():
    print(f"Silindri ruumala on ")

loop = 1
while loop==1:
    print("**************** MEGA HEA KALK ********************")
    print("1. Kera\n2. Kuup\n3. Koonus\n4. Silinder\n5. VÄLJU PROGRAMMIST\n")
    valik = int(input("Sisesta valik: "))
    print("***************************************************")

    if valik==1:
        r = int(input("Sisesta kera raadius: "))
        kera(r)
    elif valik==2:
        k = int(input("Sisesta kuubi 1 külg: "))
        kuup(k)
    elif valik==3:
        koonus()
    elif valik==4:
        silinder()
    else:
        loop = 0
        print("Täname, et kasutasite meie mega head kalkulaatorit")


input()
def tervita(nimi, keel="ge"):
    if keel=="en":
        print(f"Hi {nimi}!")
    elif keel=="et":
        print(f"Tere {nimi}!")
    else:
        print(f"Hallo {nimi}!")


tervita("Märt","en")
tervita("Märt","et")
tervita("Märt","esdfsdfsdf<sdfn")
tervita("Märt")
