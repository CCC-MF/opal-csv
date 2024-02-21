import pandas
import sys

def map_entries(entry):

    match entry:
        case 'D39.1' | 'D09.0' | 'D41.4':
            icd10 = entry
        case _:
            icd10 = entry.split('.')[0]

    match icd10:
        case 'C00' | 'C01' | 'C02' | 'C03' | 'C04' | 'C05' | 'C06' | 'C07' | 'C08' | 'C09' | 'C10' | 'C11' | 'C12' | 'C13' | 'C14':
            return 'C00-C14'
        case 'C15':
            return 'C15'
        case 'C16':
            return 'C16'
        case 'C18' | 'C19' | 'C20' | 'C21':
            return 'C18-C21'
        case 'C22':
            return 'C22'
        case 'C23' | 'C24':
            return 'C23-C24'
        case 'C25':
            return 'C25'
        case 'C32':
            return 'C32'
        case 'C33' | 'C34':
            return 'C33-C34'
        case 'C43':
            return 'C43'
        case 'C50' | 'D05':
            return 'C50, D05'
        case 'C53' | 'D06':
            return 'C53, D06'
        case 'C54' | 'C55':
            return 'C54-C55'
        case 'C56' | 'D39.1':
            return 'C56, D39.1'
        case 'C61':
            return 'C61'
        case 'C62':
            return 'C62'
        case 'C64':
            return 'C64'
        case 'C67' | 'D09.0' | 'D41.4':
            return 'C67, D09.0, D41.4'
        case 'C70' | 'C71' | 'C72':
            return 'C70-C72'
        case 'C73':
            return 'C73'
        case 'C81':
            return 'C81'
        case 'C82' | 'C83' | 'C84' | 'C85' | 'C86' | 'C87' | 'C88' | 'C96':
            return 'C82-C88, C96'
        case 'C90':
            return 'C90'
        case 'C91' | 'C92' | 'C93' | 'C94' | 'C95':
            return 'C91-C95'
        case _:
            return 'OTHER'

if len(sys.argv) < 3:
    print("Usage: python3 opal-csv.py <INPUTFILE> <OUTPUTFILE>")
    sys.exit(1)

def apply_entries(entry):
    return len(entry)

print("Lese Datei: ", sys.argv[1])
print("Schreibe Datei: ", sys.argv[2])

csv = pandas.read_csv(sys.argv[1], usecols=lambda col: col.upper() in ["CONDCODINGCODE"])
data = csv.map(map_entries).groupby(['condcodingcode']).apply(apply_entries, include_groups=False)

data.to_csv(sys.argv[2])

print(data)
