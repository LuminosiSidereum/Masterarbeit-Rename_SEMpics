import os
import sys
from pathlib import Path

def DatumEingeben()->str:
    aufnahmedatum:str = input("Bitte geben Sie das Datum (YYMMDD), an dem die REM-Aufnahmen gemacht wurden, ein: ")
    korrektesDatum:bool = False
    while korrektesDatum == False:
        if len(aufnahmedatum) != 6 or not aufnahmedatum.isdigit():
            print("Das angegebene Datum entspricht nicht dem Foramt (YYMMDD)!")
            aufnahmedatum = input("Aufnamedatum im Format (YYMMDD) eingeben: ")
        else:
            korrektesDatum = True
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
    modusauswahl:bool = True
    while modusauswahl:
        modus: str = input("Modus auswählen: 0 für Datum einfügen, 1 für Datum ändern: ")
        if modus == "0" or modus == "1":
            modusauswahl = False
        else:
            print("Ungültige Eingabe!")

    aufnahmedatum:str = DatumEingeben()

    # Pfad der aktuellen Python-Datei ermitteln
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Setze das Arbeitsverzeichnis auf den Ordner der Python-Datei (normalerweise ging das immer ohne, aber anscheinend nicht mehr)
    os.chdir(script_dir)
    
    if modus == "0":
        einfuegenDatum(aufnahmedatum)
        try:
            os.chdir(os.getcwd()+"/PlainImages")
            einfuegenDatum(aufnahmedatum)
        except FileNotFoundError:
            print("Ordner PlainImages nicht gefunden!")
    if modus == "1":
        aendernDatum(aufnahmedatum)
        try:
            os.chdir(os.getcwd()+"/PlainImages")
            aendernDatum(aufnahmedatum)
        except FileNotFoundError:
            print("Ordner PlainImages nicht gefunden!")