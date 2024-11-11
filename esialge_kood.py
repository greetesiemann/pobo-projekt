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
# mõningane eeskuju:
#
# Lisakommentaar (nt käivitusjuhend):
#
##################################################

def väljasta_retsept(faili_nimi):
    fail = open(faili_nimi, encoding = "utf-8")
    for rida in fail:
        print(rida, end="")
    fail.close()


def kas_saab_valmistada(retseptid, toiduained):
    saab_valmistada = []
    for retsept in retspetid:
        luger = 0
        for toiduaine in retsept:
            if toiduaine in toiduained:
                luger += 1
        if luger == len(retsept):
            saab_valmistada.append(retsept)
    return saab_valmistada


def pasta(järjend):
    if kana_pasta in järjend:
        pasta_fail = "kanapasta.txt"
        väljasta_retsept(pasta_fail)

def frikadelli_supp(järjend):
    if frikadelli_supp in järjend:
        frikadellisupp_fail = "frikadellisupp.txt"
        väljasta_retsept(frikadellisupp_fail)

def lihapallid(järjend):
    if lihapallid in järjend:
        lihapallid_fail = "lihapallid.txt"
        väljasta_retsept(lihapallid_fail)

def kanašnitsel(järjend):
    if kanašnitsel in järjend:
        kanašnitsel_fail = "kanašnitsel.txt"
        väljasta_retsept(kanašnitsel_fail)


kana_pasta = ["kana", "pasta", "piim", "merevaik"]
frikadelli_supp = ["kartul", "porgand", "frikadellid", "puljong"]
lihapallid = ["hakkliha", "muna", "riivsai", "sibul", "küüslauk"]
kanašnitsel = ["kana", "muna", "jahu", "riivsai"]
retspetid = [kana_pasta, frikadelli_supp, lihapallid, kanašnitsel]


def main():
    toiduained = str(input("Sisesta olemasolevad toiduained: "))
    toiduained = set(toiduained.split(", "))
    saab_teha = kas_saab_valmistada(retspetid, toiduained)
    pasta(saab_teha)
    frikadelli_supp(saab_teha)
    lihapallid(saab_teha)
    kanašnitsel(saab_teha)


if __name__ == "__main__":
    main()