import os
from pathlib import Path

def DatumEingeben()->str:
    aufnahmedatum:str = input("Bitte geben Sie das Datum (YYMMDD), an dem die REM-Aufnahmen gemacht wurden, ein: ")
    while len(aufnahmedatum) != 6:
        print("Das angegebene Datum entspricht nicht dem Foramt (YYMMDD)!")
        aufnahmedatum = input("Aufnamedatum im Format (YYMMDD) eingeben: ")
    return aufnahmedatum

def einfuegenDatum(aufnahmedatum:str)->None:
    directorycontent:list = os.listdir()
    for file in directorycontent:
        if file.endswith(".tif"):
            f:Path = Path(file)
            name, extension = f.stem, f.suffix
            newFilename:str = f"{name[0:11]}{aufnahmedatum}-{name[12:]}{extension}"
            f.rename(newFilename)

def aendernDatum(aufnamedatum:str)->None:
    directorycontent:list = os.listdir()
    for file in directorycontent:
        if file.endswith(".tif"):
            f:Path = Path(file)
            name, extension = f.stem, f.suffix
            nameblocks:list[str] = name.split("-")
            nameblocks[3] = aufnahmedatum
            newFilename:str = "-".join(nameblocks)+extension
            f.rename(newFilename)
            
if __name__=="__main__":
    mudousauswahl:bool = True
    while modusauswahl:
        modus: str = input("Modus auswählen: 0 für Datum einfügen, 1 für Datum ändern: ")
        if modus == "0" or modus == "1":
            modusauswahl = False
        else:
            print("Ungültige Eingabe!")

    aufnahmedatum:str = DatumEingeben()

    if modus == "0":
        einfuegenDatum(aufnahmedatum)
        os.chdir(os.getcwd()+"/PlainImages")
        einfuegenDatum(aufnahmedatum)
    if modus == "1":
        aendernDatum(aufnahmedatum)
        os.chdir(os.getcwd()+"/PlainImages")
        aendernDatum(aufnahmedatum)