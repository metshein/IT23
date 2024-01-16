#tekstifailid
#5.12.23
#M.Metshein

"""
    https://metshein.com/python/s6pru_l6ustaraamatus.txt
    1. Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates.
    2. Täienda eelmist programmi nii, et kuvataks kui palju on nimekirjas kodanikke Reformierakonnast ja kui palju Keskerakonnast
        Reformikaid: 3
        Kesikuid: 1
    3. Täienda programmi veelgi ja leia, kui palju oli erinevaid erakondi kokku.
        Erakondi kokku: 4
    4. Viimase täiendusena salvestab sinu programm ainult poliitikute nimed uude faili (loetavalt).
"""
fail=open("s6pru_l6ustaraamatus.txt", "r")
erakonnad = []
re = 0
ke = 0
for rida in fail:
    # enimi, perenimi, erak, sobrad = rida.split(" ")
    poliitik = rida.split(" ")
    print(f"{poliitik[0]:10} {poliitik[1]:10} {poliitik[2]:4} {poliitik[3]}", end="")
    if poliitik[2]=="RE":
        re+=1 #re = re + 1
    elif poliitik[2]=="KE":
        ke+=1
    #lisab unikaalsed erakonnad massiivi
    if poliitik[2] not in erakonnad:
        erakonnad.append(poliitik[2])
    
    #kirjutab tekstifaili
    with open("poliitikud.txt","a") as kirjutamiseks:
        kirjutamiseks.write(poliitik[0]+" "+poliitik[1]+"\n")

print()
print(f"Reformikad: {re} \nKesikud: {ke}")
print(f"Erakondi kokku: {len(erakonnad)}")
fail.close


