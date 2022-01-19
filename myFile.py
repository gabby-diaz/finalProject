#testing
#counting dna nucleotides
#first try
# def dnaCount(dnaSeq):
#	'''
#	Input: DNA Sequence
#	Output: four intigers A, C, G, T
#	'''
#	A = 0
#	T = 0
#	G = 0
#	C = 0

#	for nucleotide in dnaSeq:
#		if nucleotide == 'A':
#			A += 1
#		elif nucleotide == 'T':
#			T +=1
#		elif nucleotide == 'G':
#			G +=1
#		elif nucleotide == 'C':
#			C +=1

#	return(A, T, G, C)

#if __name__=='__main__':
#	print(dnaCount('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))

#second try on making the dna count thing work
#problem 1 Counting DNA nucleotides - DNA

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
	
#transcribing dna into rna - RNA
#1-17-22

def DtoR(dnaSeq):
    '''
    input: DNA Sequence
    output: RNA Sequence (Nucleotide T becomes U)
    '''
    rnaSeq = ''
#making it so that every T becoemes a U and everything else stays the same
    for nucleotide in dnaSeq:
        if nucleotide == 'T':
            rnaSeq += 'U'
        else:
            rnaSeq += nucleotide

    return rnaSeq

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
print(DtoR(dnaSeq))
#Complementing a strand of DNA -REVC

def Rcompliment(dnaSeq):
    '''
    input: DNA Sequence
    output: The reverse complimentary nucleotides of the DNA Sequence
    '''
    # A compliments T, G compliments C, vise versa
    #reverse the dna sequence
    dnaReverse = dnaSeq[::-1]

    DNAreverseCompliment= {'A':'T', 'A':'T', 'C':'G','G':'C'}

    Rcompliment = ''
    for nucleotide in dnaReverse:
       Rcompliment += DNAreverseCompliment[nucleotide]

    return(Rcompliment)

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
print(Rcompliment(dnaSeq))

# 1-18-22
#RNA 2 Prot

def dna2protein(rnaSeq):
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
   aminoacid = codonTableD[codon]
   acidSequence += aminoacid 
   i += 3
  return protSequence 


	
	
