from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

# Ruta del archivo en formato GenBank del escritorio (Bacillum)
filename = "/mnt/c/Users/abrah/Desktop/COMPUTACION/GCF_000321185.1_ASM32118v1_genomic.gbff"

def summarize_contents(filename):
listAOM = []
listAOM = os.path.split(filename)
print("file:", listAOM[1], "\npath:", listAOM[0])
all_records = []
records = list(SeqIO.parse(filename, "genbank"))
print("num_records = %i records" % len(records))
print("records:")
for seq_record in SeqIO.parse(filename, "genbank"):
all_records.append(seq_record.name)
print("- id:",seq_record.id)
print("name: ", seq_record.name)
print("description: ", seq_record.description)
print("\n")
summarize_contents(filename)
