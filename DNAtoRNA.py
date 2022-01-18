#transcribing dna into rna
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
