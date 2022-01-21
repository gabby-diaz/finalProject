#Complementing a strand of DNA -REVC
DNAreverseCompliment= {'A':'T', 'T':'A', 'C':'G','G':'C'}

def Rcompliment(dnaSeq):
    '''
    input: DNA Sequence
    output: The reverse complimentary nucleotides of the DNA Sequence
    '''
    # A compliments T, G compliments C, vise versa
    #reverse the dna sequence
    dnaReverse = dnaSeq[::-1]


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
