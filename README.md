# REM-Bild-Umbenennungstool

## Funktionsweise
Dieses Skript ergänzt die fehlenden Namensbestandteile von **REM-Aufnahmen**, da das **REM-Gerät eine Zeichenbegrenzung von 30 Zeichen** hat und der vollständige Dateiname nicht direkt eingegeben werden kann.  
Derzeit wird nur das **Aufnahmedatum** ergänzt oder geändert.  

Das Skript verarbeitet `.tif`-Dateien im aktuellen Verzeichnis und im Unterverzeichnis **"PlainImages"**, falls vorhanden.  

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet `.tif`-Dateien im aktuellen Verzeichnis.  
- Die Dateinamen müssen in **"-"** getrennte Blöcke unterteilt sein.  
- Das Aufnahmedatum wird als vierter Block im Dateinamen eingefügt oder ersetzt.  

### Ausführung
1. Stelle sicher, dass sich die `.tif`-Dateien im Verzeichnis befinden.  
2. Starte das Skript `main.py`.  
3. Wähle den gewünschten Modus:  
   - **`0`** → Fügt das Datum in die Dateinamen ein.  
   - **`1`** → Ersetzt das bestehende Datum im Dateinamen.  
4. Gib das Aufnahmedatum im Format **YYMMDD** ein.  
5. Das Skript passt die Dateinamen an und überprüft, ob der Ordner **"PlainImages"** existiert, um dort ebenfalls die Anpassungen vorzunehmen.  

### Ausgabe
- Die `.tif`-Dateien werden mit dem korrekten Aufnahmedatum gespeichert.  
- Falls der **"PlainImages"**-Ordner existiert, werden dort die Namen ebenfalls angepasst.  
- Eine Bestätigung der Umbenennung wird in der Konsole ausgegeben.  

