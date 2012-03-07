import subprocess

from Bio import Entrez, SeqIO
from Bio.Emboss.Applications import NeedleCommandline

Entrez.email = "stowers@imp.ac.at"

handle = Entrez.efetch(db="nucleotide", id="AF182035",rettype="gb", retmode="text")
homo = SeqIO.read(handle, "genbank")

handle = Entrez.efetch(db="nucleotide", id="AY863830",rettype="gb", retmode="text")
drosophila = SeqIO.read(handle, "genbank")

open("homo.fasta","w").write(biosomething.homo.format("fasta"))
ls
cat homo.fasta
open("drosophila.fasta","w").write(biosomething.drosophila.format("fasta"))

n = NeedleCommandline(asequence="homo.fasta", bsequence="drosophila.fasta",gapopen=10, gapextend=0.5, outfile="needle.txt")
n
n
print n
!needle -outfile=needle.txt -asequence=homo.fasta -bsequence=drosophila.fasta -gapopen=10 -gapextend=0.5
from Bio import AlignIO
align = AlignIO.read("needle.txt", "emboss")
align
print align
!needle -outfile=needle.txt -asequence=homo.fasta -bsequence=drosophila.fasta -gapopen=1 -gapextend=0.5
align = AlignIO.read("needle.txt", "emboss")
print align
!needle -outfile=needle.txt -asequence=homo.fasta -bsequence=drosophila.fasta -gapopen=100 -gapextend=0.5
align = AlignIO.read("needle.txt", "emboss")
print align
!needle -outfile=needle.txt -asequence=homo.fasta -bsequence=drosophila.fasta -gapopen=10 -gapextend=10
align = AlignIO.read("needle.txt", "emboss")
print align
history



