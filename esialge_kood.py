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
    for retsept in retseptikogu:
        luger = 0
        for toiduaine in retsept:
            if toiduaine in sisestatud_toiduained:
                luger += 1
        if luger == len(retsept):
            saab_valmistada.append(retsept)
    return saab_valmistada


#Järgnevad funktsioonid kontrollivad roa olemasolu saab_valmistada järjendis ning vajadusel kutsuvad välja funktsiooni, mis väljastab retsepti.
def kas_saab_teha_kanapasta(võimalikud_retseptid):
    if kanapasta in võimalikud_retseptid:
        pasta_fail = "kanapasta.txt"
        print("\nHakkad valmistama kanapastat")
        väljasta_retsept(pasta_fail)


def kas_saab_teha_frikadellisupp(võimalikud_retseptid):
    if frikadellisupp in võimalikud_retseptid:
        frikadellisupp_fail = "frikadellisupp.txt"
        print("\nHakkad valmistama frikadellisuppi")
        väljasta_retsept(frikadellisupp_fail)


def kas_saab_teha_lihapallid(võimalikud_retseptid):
    if lihapallid in võimalikud_retseptid:
        lihapallid_fail = "lihapallid.txt"
        print("\nHakkad valmistama lihapalle")
        väljasta_retsept(lihapallid_fail)


def kas_saab_teha_kanašnitsel(võimalikud_retseptid):
    if kanašnitsel in võimalikud_retseptid:
        kanašnitsel_fail = "kanašnitsel.txt"
        print("\nHakkad valmistama kanašnitslit")
        väljasta_retsept(kanašnitsel_fail)


def kas_saab_teha_caesarisalat(võimalikud_retseptid):
    if caesarisalat in võimalikud_retseptid:
        caesarisalat_fail = "caesarisalat.txt"
        print("\nHakkad valmistama Caesari salatit")
        väljasta_retsept(caesarisalat_fail)



kanapasta = ["kana", "pasta", "piim", "merevaik"]
frikadellisupp = ["kartul", "porgand", "frikadellid", "puljong"]
lihapallid = ["hakkliha", "muna", "riivsai", "sibul", "küüslauk"]
kanašnitsel = ["kana", "muna", "jahu", "riivsai"]
caesarisalat = ["kana", "salat", "tomat", "parmesan", "caesari kaste"]
retspetid = [kanapasta, frikadellisupp, lihapallid, kanašnitsel, caesarisalat]


#Põhifunktsioon
def main():
    toiduained = str(input("Sisesta olemasolevad toiduained: "))
    toiduained = set(toiduained.split(", "))
    saab_teha = kas_saab_valmistada(retspetid, toiduained)
    kas_saab_teha_kanapasta(saab_teha)
    kas_saab_teha_frikadellisupp(saab_teha)
    kas_saab_teha_lihapallid(saab_teha)
    kas_saab_teha_kanašnitsel(saab_teha)
    kas_saab_teha_caesarisalat(saab_teha)


if __name__ == "__main__":
    main()