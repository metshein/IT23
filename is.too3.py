#TÜ iseseisev töö
#M.Metshein 
#18.12.23, 10.01.24

import random
import datetime
# from datetime import *


#Tahvli juurde
fail = open("nimekiri.txt", encoding="utf-8")

p  = datetime.datetime.now().day
nr = 1
for rida in fail:
    if nr==p:
        print(f"Tahvli ette tuleb: {rida}.")
    nr+=1



#Jukebox
# failinimi = input("Palun sisestage failinimi: ")
# fail = open(failinimi, encoding="utf-8")
# nr = 1
# for rida in fail:
#     print(f"{nr}. {rida}",end="")
#     nr+=1

# fail.seek(0)
# nr = 1
# jrk = int(input("\nValige laulu järjekorranumber: "))
# for rida in fail:
#     if nr==jrk:
#         print(f"Mängitav muusikapala on: {rida}.")
#     nr+=1









#sissetulekud
# fail = open("konto.txt", encoding="utf-8")
# for rida in fail:
#     if float(rida) > 0:
#         print(float(rida))

# fail.close()


#rebased

# fail = open("rebased.txt", encoding="utf-8")
# vastuvoetud = []
# for rida in fail:
#     vastuvoetud.append(int(rida))

# #2011-2019
# #print(vastuvoetud)
# aasta = 2011
# print(f"Aastal {aasta} võeti vastu {vastuvoetud[aasta-2011]} õpilast")

fail.close()