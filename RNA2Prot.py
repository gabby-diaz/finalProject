# 1-18-22
#RNA 2 Prot

import codonDict as codonDict
import DNAtoRNA as rna 

rnaSeq = DtoR(dnaSeq)


def rna2protein(rnaSeq):
  '''Given a rnaSeq, output corresponding aa chain.

  Input: str of rna sequence 
  Output: str of protein
  '''
  #variables 
  protSequence = ''
  i=0
  print(type(rnaSeq))
  print(type(i))
  while i < (len(dnaSeq)-2):
   codon = dnaSeq[i:i+3] 
   aminoacid = codonDict[codon]
   acidSequence += aminoacid 
   i += 3
  return protSequence 

def readfile(file_path):
	'''
	input: file 
	output: string of data needed
	''' 
	#so that the function can read the file with the dna data
	with open(file_path) as f:
		file_data = f.read()
	return file_data

if __name__ == '__main__':
  file_path ='rosalind_dna.txt'
	#reading the data
  dnaSeq = readfile(file_path)

#printing the result
print(rna2protein(dnaSeq))