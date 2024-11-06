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


kana_pasta = ["kana", "pasta", "piim", "merevaik"]
frikadelli_supp = ["kartul", "porgand", "frikadellid", "puljong"]
retspetid = [kana_pasta, frikadelli_supp]


def main():
    toiduained = str(input("Sisesta olemasolevad toiduained: "))
    toiduained = set(toiduained.split(", "))
    saab_teha = kas_saab_valmistada(retspetid, toiduained)
    pasta(saab_teha)

if __name__ == "__main__":
    main()