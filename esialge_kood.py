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

pasta = ["kana", "makaronid", "koor"]
supp = ["kartul", "porgand", "frikadellid"]
retspetid = [pasta, supp]

def main():
    toiduained = str(input("Sisesta olemasolevad toiduained: "))
    toiduained = toiduained.split()
    for retsept in retspetid:
        for toiduaine in retsept:
            if toiduaine in toiduained:
                print(toiduaine)


if __name__ == "__main__":
    main()