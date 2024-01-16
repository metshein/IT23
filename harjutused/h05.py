#M.Metshein
#28.11.23
"""
Vanused
    Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
"""
vanused = [3,54,5,15,49,45,54,49,4,1,2]
print(f"Kõige vanem {max(vanused)} ja kõige noorem {min(vanused)}")
print(f"Vanuste summa {sum(vanused)} ja vanuste keskmine {round(sum(vanused)/len(vanused),2)}")

for vanus in vanused:
    print(vanus * "*")




input()
"""
Duplikaadid
    Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
    Loo kood, mis ei väljasta kordusi.
"""
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
nimed = []

for opilane in opilased:
    if opilane not in nimed:
        nimed.append(opilane)
print(nimed)
"""
Õpilased
    Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
"""
nr = 1
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
for opilane in opilased:
    print(f"{nr}. {opilane}")
    nr+=1
valik = int(input("Mitmendat nime soovid muuta: "))
del opilased[valik-1]

uus_nimi = input("Lisa uus või parandatud nimi: ")
opilased.insert(valik-1, uus_nimi)

for opilane in opilased:
    print(f"{opilane}")





'''
Nimede lisamine loendisse
    Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.

nimed = []
n = ""
k = 0

for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)



print(nimed)

'''