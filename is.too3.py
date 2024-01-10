#TÜ iseseisev töö
#M.Metshein 
#18.12.23

import random

failinimi = input("Palun sisestage failinimi: ")
fail = open(f"c:\\Users\\mario.metshein\\Desktop\\python_harj\\IT23\\{failinimi}", encoding="utf-8")
fail = open(failinimi, encoding="utf-8")







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