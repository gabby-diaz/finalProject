#second try on making the dna count thing work

def dnaCount(dnaSeq):
	'''
	Input: DNA Sequence
	Output: four intigers A, C, G, T
	'''
	#
	A = 0
	T = 0
	G = 0
	C = 0

	for nucleotide in dnaSeq:
		#counting the amount of dna nucleotides in the sequence
		if nucleotide == 'A':
			A += 1
		elif nucleotide == 'T':
			T +=1
		elif nucleotide == 'G':
			G +=1
		elif nucleotide == 'C':
			C +=1

	return(A, T, G, C)

def readfile(file_path):
	'''
	input: file 
	output: string of data needed
	''' 
	#so that the function can read the file with the dna data
	with open(file_path) as f:
		file_data = f.read()
	return file_data

if __name__=='__main__':
	file_path ='rosalind_dna.txt'
	#reading the data
	dnaSeq = readfile(file_path)

#printing the result
	print(dnaCount(dnaSeq))