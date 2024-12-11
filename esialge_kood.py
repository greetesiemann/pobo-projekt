################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt: Pobo köögis
# Teema: Mida võiks süüa teha?
#
#
# Autorid: Hanna Samelselg, Greete Siemann
#
#
# Lisakommentaar (nt käivitusjuhend): 
# Käivita programm ning sisesta toiduained omavahel eraldatud komaga.
# Näide: toiduaine, toiduaine ...
#
##################################################


#Funktsioon, mis väljastab sobiliku retsepti, lugedes andmed failist.
def väljasta_retsept(faili_nimi):
    fail = open(faili_nimi, encoding = "utf-8")
    for rida in fail:
        print(rida, end="")
    fail.close()


#Funktsioon, mis kontrollib, kas toitu saab valmistada ja seejärel lisab järjendisse.
def kas_saab_valmistada(retseptikogu, sisestatud_toiduained):
    saab_valmistada = []
    puuduvad_toiduained = []
    for retsept in retseptikogu:
        luger = 0
        for toiduaine in retsept:
            if toiduaine in sisestatud_toiduained:
                luger += 1
            else:
                puuduvad_toiduained.append(toiduaine)
        if luger == len(retsept):
            saab_valmistada.append(retsept)
        elif len(puuduvad_toiduained) <= 2:
            print(f"Ostes juurde: ", end="")
            for puuduv in puuduvad_toiduained:
                print(f"{puuduv},", end=" ")
            print("saad valmistada...")
    if len(saab_valmistada) != 0:
        return saab_valmistada
    elif len(puuduvad_toiduained) == 0 and len(saab_valmistada) == 0:
        print("Kahjuks ei ole ühtegi retsepti, mida saaks olemasolevatest toiduainetest valmistada")


#Järgnevad funktsioonid kontrollivad roa olemasolu saab_valmistada järjendis ning vajadusel kutsuvad välja funktsiooni, mis väljastab retsepti.
def kas_saab_teha_kanapasta(võimalikud_retseptid):
    if kanapasta in võimalikud_retseptid:
        print("\nHakkad valmistama kanapastat")
        väljasta_retsept("kanapasta.txt")


def kas_saab_teha_frikadellisupp(võimalikud_retseptid):
    if frikadellisupp in võimalikud_retseptid:
        print("\nHakkad valmistama frikadellisuppi")
        väljasta_retsept("frikadellisupp.txt")


def kas_saab_teha_lihapallid(võimalikud_retseptid):
    if lihapallid in võimalikud_retseptid:
        print("\nHakkad valmistama lihapalle")
        väljasta_retsept("lihapallid.txt")


def kas_saab_teha_kanašnitsel(võimalikud_retseptid):
    if kanašnitsel in võimalikud_retseptid:
        print("\nHakkad valmistama kanašnitslit")
        väljasta_retsept("kanašnitsel.txt")


def kas_saab_teha_caesarisalat(võimalikud_retseptid):
    if caesarisalat in võimalikud_retseptid:
        print("\nHakkad valmistama Caesari salatit")
        väljasta_retsept("caesarisalat.txt")


def kas_saab_teha_lillkapsasteik(võimalikud_retseptid):
    if lillkapsasteik in võimalikud_retseptid:
        print("\nHakkad valmistama lillkapsasteike")
        väljasta_retsept("lillkapsasteik.txt")


def kas_saab_teha_köögiviljavokk(võimalikud_retseptid):
    if köögiviljavokk in võimalikud_retseptid:
        print("\nHakkad valmistama köögiviljavokki")
        väljasta_retsept("köögiviljavokk.txt")



kanapasta = ["kana", "pasta", "piim", "merevaik"]
frikadellisupp = ["kartul", "porgand", "frikadellid", "puljong"]
lihapallid = ["hakkliha", "muna", "riivsai", "sibul", "küüslauk"]
kanašnitsel = ["kana", "muna", "jahu", "riivsai"]
caesarisalat = ["kana", "salat", "tomat", "parmesan", "caesari kaste"]
lillkapsasteik = ["lillkapsas", "riivjuust", "õli"]
köögiviljavokk = ["külmutatud köögiviljad", "munanuudlid", "sojakaste", "mesi"]
retspetid = [kanapasta, frikadellisupp, lihapallid, kanašnitsel, caesarisalat, lillkapsasteik, köögiviljavokk]


#Põhifunktsioon
def main():
    toiduained = str(input("Sisesta olemasolevad toiduained: "))
    toiduained = set(toiduained.split(", "))
    saab_teha = kas_saab_valmistada(retspetid, toiduained)
    if len(saab_teha) != 0:
        kas_saab_teha_kanapasta(saab_teha)
        kas_saab_teha_frikadellisupp(saab_teha)
        kas_saab_teha_lihapallid(saab_teha)
        kas_saab_teha_kanašnitsel(saab_teha)
        kas_saab_teha_caesarisalat(saab_teha)
        kas_saab_teha_lillkapsasteik(saab_teha)
        kas_saab_teha_köögiviljavokk(saab_teha)


if __name__ == "__main__":
    main()