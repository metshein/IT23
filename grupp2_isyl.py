#Mario
#16.01.21


# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud õigesti
# 	Programm tükeldab selle ja väljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com



kuud = [["jaanuar", -16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3],
["veebruar", -9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18],
["märts", 2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2],
["aprill", -5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2],
["mai", 12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1],
["juuni", 12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22],
["juuli", 15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20],
["august", 7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11],
["september", 21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19],
["oktoober", 2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1],
["november", -6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1],
["detsember", -15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]]

print("------------Kõige soojemad kuupäevad-----")
for i in kuud:
    kuu = i.pop(0)
    print(f"{i.index(max(i))+1}.{kuu}")
    # for j in i:
    #     print(j)







nimekiri = []

while True:
    valik = input("\nLisa toode: ")
    if valik == "":
        break
    nimekiri.append(valik)
print("------------Ostukorv------------")
for i in nimekiri:
    print(i)





# 11. Salakeel
# 	sinu programm kÃ¼sib kasutajalt, kas ta soovib salakeelt luua vÃµi tÃµlkida - 1p
# 	kasutaja sisestab tavalise sÃµna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sÃµna, mis teisendatakse jÃ¤lle normaalseks - 1p
# 	kood kommenteeritud - 1p

valik = input("Kas soovid salakeelt luua (1) või tõlkida (2)? ")
if valik == "1":
    sona = input("Sisesta sõna: ")
    sona = sona.lower()
    salakeel = ""
    for taht in sona:
        taht = taht.lower()
        salakeel+=chr(ord(taht)+1)
    print(salakeel)
if valik == "2":
    sona = input("Sisesta sõna: ")
    sona = sona.lower()
    salakeel = ""
    for taht in sona:
        taht = taht.lower()
        salakeel+=chr(ord(taht)-1)
    print(salakeel)




# # 4. List Less Than Ten
# # 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# # 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# # 	Write this in one line of Python.
# # 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list = []
# kasutaja = 5
# for i in a: new_list.append(i) if i<kasutaja else 0
# print(new_list)

# exit()

# # 2. Vanused
# # 	loo vanuste loend 1p
# # 	leia numbrite suurim ja väikseim arv  1p
# # 	kogusumma  1p
# # 	keskmine 1p

# vanused=[7,6,5,19,18,18,17,20,15,11,7,10,13,12,20,11,10,14,18,14,24,6,17,16,6,17,5,13,11]
# def vanuste_stat(loend):
#     maks = max(vanused)
#     miin = min(vanused)
#     summa = 0
#     for i in vanused:
#         summa+=i
#     print(f"Maksimum: {maks} Miinimum: {miin} Summa: {summa}")
# vanuste_stat(vanused)