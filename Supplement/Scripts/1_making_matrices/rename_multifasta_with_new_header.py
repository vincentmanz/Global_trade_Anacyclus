#!/usr/bin/env python2
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import sys

fasta_file = sys.argv[1]
#fasta_file = "269584723.fasta"
new_mane_list = open("new_name.list","r")
f = open("../1_rename_header/"+fasta_file, 'w')
print fasta_file
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	sequences = {}
	sequence = str(seq_record.seq)
	ID = seq_record.id.split("_")[0]
	allele = seq_record.id.split("_")[-1]
	new_mane_list = open("new_name.list","r")
	for newname in new_mane_list:
		newname = newname.split("\n")[0] 
		newname_split = newname.split("_")[-1]
		if ID == newname_split:
			newname = newname.split("\n")[0] + "_" + str(allele)
			new_record = SeqRecord(Seq(sequence), id= newname,description="")

			SeqIO.write(new_record, f, "fasta")
print "done!"







