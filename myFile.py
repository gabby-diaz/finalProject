#testing
#counting dna nucleotides

import resources

def dnaCount(dnaSeq):
	'''
	Input: DNA Sequence
	Output: four intigers A, C, G, T
	'''
	A = 0
	T = 0
	G = 0
	C = 0

	for nucleotide in dnaSeq:
		if nucleotide == 'A':
			A += 1
		elif nucleotide == 'T':
			T +=1
		elif nucleotide == 'G':
			G +=1
		elif nucleotide == 'C':
			C +=1

	return(A, T, G, C)

if __name__=='__main__':
	print(dnaCount('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
