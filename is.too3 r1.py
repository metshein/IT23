#TÜ iseseisev töö
#M.Metshein 
#18.12.23, 10.01.24

#jukebox
siiamidagi = input("Anna failinimi: ")
fail = open(siiamidagi, encoding="utf-8")
print("Muusikapalade valik:")




#sissetulekud
fail = open("konto.txt")
for i in fail:
    if float(i) > 0:
        print(i,end="")


#rebased

# fail = open("rebased.txt", encoding="utf-8")
# vastuvoetud = []
# for rida in fail:
#     vastuvoetud.append(int(rida))

# #2011-2019
# #print(vastuvoetud)
# aasta = 2011
# print(f"Aastal {aasta} võeti vastu {vastuvoetud[aasta-2011]} õpilast")

# fail.close()