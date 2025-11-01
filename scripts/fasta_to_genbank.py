import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def fasta_to_genbank(fasta_file, genbank_file):
    records = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_record = SeqRecord(
            Seq(str(record.seq)),
            id=record.id,
            description=record.description
        )
        seq_record.annotations["molecule_type"] = "DNA"  # Add molecule_type annotation
        records.append(seq_record)
    
    SeqIO.write(records, genbank_file, "genbank")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fasta_to_genbank.py <input.fasta> <output.gb>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    genbank_file = sys.argv[2]
    fasta_to_genbank(fasta_file, genbank_file)
    print(f"Converted {fasta_file} to {genbank_file}")