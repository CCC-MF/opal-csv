Python Script zur Ermittlung der Anzahl der Conditions nach Durchlauf der BZKF-RWDP.

Als Datengrundlage dient die CSV-Datei, die in OPAL veröffentlicht werden soll.

**Wird im Projekt [bzkf-rwdp-check](https://github.com/CCC-MF/bzkf-rwdp-check) weitergeführt.**

## Benutzung

Eingabedatei ist die CSV-Datei für OPAL, die Ausgabedatei ist eine CSV-Datei, die die Anzahl der Conditions enthält,
gruppiert nach relevanten ICD10-Gruppen.

```
python3 opal-csv.py <CSV-INPUTFILE> <CSV-OUTPUTFILE>
```
