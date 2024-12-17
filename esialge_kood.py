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


#Impordime kasutajaliidese
import tkinter as tk
from tkinter import messagebox

#Funktsioon, mis väljastab sobiliku retsepti, lugedes andmed failist.
def väljasta_retsept(faili_nimi):
    try:
        with open(faili_nimi, encoding="utf-8") as fail:
            retsept = fail.read()
            return retsept
    except FileNotFoundError:
        return f"Retsepti fail {faili_nimi} ei leitud."
    


#Funktsioon, mis kontrollib, kas toitu saab valmistada ja seejärel lisab järjendisse.
def kas_saab_valmistada(retseptikogu, sisestatud_toiduained):
    saab_valmistada = {}
    puuduvate_toiduainete_retseptid = {}
    for retsept, koostisosad in retseptikogu.items():
        luger = 0
        puuduvad_toiduained = []
        for toiduaine in koostisosad:
            if toiduaine in sisestatud_toiduained:
                luger += 1
            else:
                puuduvad_toiduained.append(toiduaine)
        if luger == len(koostisosad):
            saab_valmistada[retsept] = koostisosad
        elif len(puuduvad_toiduained) <= 2:
            puuduvate_toiduainete_retseptid[retsept] = puuduvad_toiduained

            print(f"Ostes juurde: ", end="")
            for puuduv in puuduvad_toiduained:
                print(f"{puuduv},", end=" ")
            print(f"saad valmistada {retsept}")
    return saab_valmistada, puuduvate_toiduainete_retseptid

#Funktsioon, mis väljastab uues aknas retsepti, lugedes selle vastavast failist.
def kuva_retsept(retsepti_nimi):
    retsept = väljasta_retsept(f"{retsepti_nimi}.txt")
    messagebox.showinfo(f"Retsept - {retsepti_nimi}", retsept)


retseptid = {"kanapasta": ["kana", "pasta", "piim", "merevaik"], "frikadellisupp": ["kartul", "porgand", "frikadellid", "puljong"], 
             "lihapallid": ["hakkliha", "muna", "riivsai", "sibul", "küüslauk"], "kanašnitsel": ["kana", "muna", "jahu", "riivsai"], 
             "caesarisalat": ["kana", "salat", "tomat", "parmesan", "caesari kaste"], "lillkapsasteik": ["lillkapsas", "riivjuust", "õli"],
             "köögiviljavokk": ["külmutatud köögiviljad", "munanuudlid", "sojakaste", "mesi"]}


#Põhifunktsioon
def main():
    def kontrolli_toiduaineid():
        toiduained = toiduained_sisend.get()
        toiduained = set(toiduained.split(", "))
        saab_teha, puuduvate_toiduainete_retseptid = kas_saab_valmistada(retseptid, toiduained)
        if not saab_teha and not puuduvate_toiduainete_retseptid:
            messagebox.showwarning("Kahjuks ei ole ühtegi retsepti, mida saaks olemasolevatest toiduainetest valmistada")
        else:
            if saab_teha:
                for retsept in saab_teha.keys():
                    kuva_retsept(retsept)
            
            if puuduvate_toiduainete_retseptid:
                puuduvate_tekst = ""
                for retsept, puuduvad_toiduained in puuduvate_toiduainete_retseptid.items():
                    puuduvate_tekst += f"\nKui ostad juurde {', '.join(puuduvad_toiduained)}, saad valmistada {retsept}."
                    retsepti_tekst = väljasta_retsept(f"{retsept}.txt")
                    puuduvate_tekst += f"\n\nRetsept:\n{retsepti_tekst}\n"
                messagebox.showinfo("Puuduvate koostisainetega retseptid:", puuduvate_tekst)
        
    #Loome kasutajaliidese jaoks akna
    aken = tk.Tk()
    aken.title("Retseptivalija")

    #Kasutajaliidese elemdid
    juhis = tk.Label(aken, text="Sisesta olemasolevad toiduained, eraldades need komadega:")
    juhis.pack(pady=5)

    toiduained_sisend = tk.Entry(aken, width=50)
    toiduained_sisend.pack(pady=5)

    kontrolli_nupp = tk.Button(aken, text="Vaata retsepte", command=kontrolli_toiduaineid)
    kontrolli_nupp.pack(pady=10)

    #Käivitame akna
    aken.mainloop()



if __name__ == "__main__":
    main()