#TÜ iseseisev töö
#M.Metshein 
#18.12.23
import winsound
import random


# Otil, Trsitanil ja Agatal on hommikuti raske tõusta ja neil on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. 
# Koostada programm, mis küsib kasutajalt, mitu korda äratus heliseb ning
# väljastab sama arv kordi ekraanile Tõuse ja sära!.

def aratus(nr):
    for i in range(nr):
        winsound.Beep(2500, 1000)
        print("Tõuse ja sära!")

# Jänesevanemad on mures, et lapsed ei liigu piisavalt. 
# Laste motiveerimiseks mõtlesid nad välja süsteemi, 
# kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. 
# Paarituarvulistel ringidel porgandeid juurde ei saa. 
# Koostada programm, mis küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid

    print(f"Jänkulaps saab: {porgandid} porgandit!")


# Erinevate täringumängude jaoks on vajalik erinev arv täringuid.
# Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koostada programm, mis
# küsib kasutajalt vajalike täringute arvu;
# viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
# väljastab iga arvu eraldi reale.

def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))
        
# Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu. Leiutaja oli “tagasihoidlik” ja palus tasuks
# esimese ruudu eest 1 nisutera;
# teise ruudu eest 2 korda rohkem ehk 2;
# kolmanda ruudu eest veel 2 korda rohkem ehk 4;
# neljanda ruudu eest siis 8;
# viienda ruudu eest 16 jne.
# Malelaual on 64 ruutu. Koostada programm, mis
# küsib kasutajalt ühe täisarvu;
# arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu eest leiutaja küsis;
# tulemus väljastatakse ekraanile pärast tsüklit.

def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(nisuterad)

# male(5)

# kordused = int(input("Äratuste arv: "))
# aratus(kordused)

# ringid = int(input("Ringide arv: "))
# porgandid(ringid)

# taringud(6)


def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad-=pounad
        print(pounad)
    print(f"Lumivalgekesekesekele jäi {ounad} õuna")

lumivalgeke(6)




