#TÜ iseseisev töö
#M.Metshein 
#10.01.24

import random
import datetime

#4.5. Mündid



pronksikarva_summa()




#------------------------------------------------------------

# 4.4. Tervitused
def tervitus(jrk):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {jrk}. kord tervitada, mõtiskleb võõrustaja.")
    print('Külaline: "Tere, suur tänu kutse eest!"')

kylaliste_arv = int(input("Mitu inimest on kutsutud: "))
for i in range(kylaliste_arv):
    tervitus(i+1)

#------------------------------------------------------------

#4.3. Peo eelarve
def eelarve(arv):
    kogusumma = arv * 10 + 55
    return kogusumma

kylaliste_arv = int(input("Mitu inimest on kutsutud: "))
kylaliste_arv_tegelik = int(input("Mitu inimest tuleb: "))
print(f"MAX eelarve: {eelarve(kylaliste_arv)}")
print(f"MIN eelarve: {eelarve(kylaliste_arv_tegelik)}")
#------------------------------------------------------------

#4.2. Õunamahl
def mahlapakkide_arv(kg):
    mahlapakkidearv = round(kg * 0.4 / 3)
    return mahlapakkidearv

ountekogus = float(input("Sisesta õunte kogus: "))
print(mahlapakkide_arv(ountekogus))
#------------------------------------------------------------

#4.1. Bänner
def banner(l):
    print(l.upper())

kord = int(input("Mitu korda: "))
tekst = input("Lisa tekst: ")

for i in range(kord):
    banner(tekst)
#------------------------------------------------------------






# #4.6. Kuupäev
# kuunimi()
# kuupäev_sõnena()









#sissetulekud
# fail = open("konto.txt", encoding="utf-8")
# for rida in fail:
#     if float(rida) > 0:
#         print(float(rida))

# fail.close()