import Bio.Seq as BioS
import Bio.Alphabet as BioA

genes = ["ACTCATATTTCTTAAATTTCTTAAACTCATGAATAACCTTATACTCATCAAAATTAA"
         "TCTGAAATGATTAATGCTCGT"]         

for gene in genes:
    print "genetic code =\n", gene, "\namino acids = ",
    coding_dna = BioS.Seq(gene, BioA.IUPAC.unambiguous_dna)
    print coding_dna.translate(stop_symbol=' '), "\n"

