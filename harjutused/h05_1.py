#Massiivid - Array
#28.11.23, 5.12.23
#M.Metshein

"""
Vanused
    Loo vanuste loend. Leia numbrite suurim ja väikseim arv, 
    kogusumma, keskmine
    Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.
"""
vanused = [13,12,5,4,5,4,45,5,5,53,44,4,4,4,4]
print(f"Suurim arv on {max(vanused)} ja väikseim arv on {min(vanused)}")
print(f"Vanuste summa: {sum(vanused)}")
print(f"Vanuste keskmine: {round(sum(vanused)/len(vanused),2)}")

for vanus in vanused:
    print(vanus * "*")








print("")
input()

"""
Duplikaadid
    Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
    Loo kood, mis ei väljasta kordusi.
"""
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus_opilased = []
#käib kõik läbi
for opilane in opilased:
   #kontrollib kas on uues loendis olemas
   if opilane not in uus_opilased:
       #kui pole, siis lisan
       uus_opilased.append(opilane)

print(uus_opilased)



"""
Õpilased
    Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
"""
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
jrk = 1
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
valik = int(input("Mitmendat nime tahad muuta: "))
uusnimi = input("Lisa uus nimi: ")
del opilased[valik-1]
opilased.insert(valik-1, uusnimi)

print(opilased)




"""
Nimede lisamine loendisse
    Küsi kasutajalt viis nime. 
    Salvesta need loendisse ja kuva tähestikulises järjekorras. 
    Kuva eraldi viimati lisatud nimi.


nimed = []

for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
print("Viimati lisatud nimi:",nimed[-1])
nimed.sort()
print(nimed)
"""