from Bio import Entrez, SeqIO
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
Entrez.email = input("NIBIB Email: ")
searchTerm = input("Gene: ").upper() + " gene human"

handle = Entrez.esearch(db="nucleotide", term=searchTerm, sort="relevance", idtype="acc")
record = Entrez.read(handle)
topId = record["IdList"][0]

handle = Entrez.efetch(db="nucleotide", id=topId, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print(f'Accession: {record.id}')
print(f'Description: {record.description}')
print(f'Sequence Length: {len(record.seq)}')

if len(record.seq) > 700:
    print('\nSequence: Sequence is too large for this simple program!')
else:
    print('\nSequence:')
    print(record.seq)
