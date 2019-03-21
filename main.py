"""-------------------------IMPORT------------------------------------------"""
from Greedy import GreedyMotifSearch
from Random import RandomMotifSearch
from Brute import BruteForceMotifSearch

"""------------------------ZMIENNE------------------------------------------"""

DNA = (
    'tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
    'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
    'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
    'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
    'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
    'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
    'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctgactgtgtagatccgta',
    'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
    'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
    'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg'
       )


k = 5

"""-------------------------MAIN--------------------------------------------"""

"""
BruteForceMotifSearch zakomentowałem żeby mozna było sprawdzić działanie pozostałych algorytmów
#BruteForce
with open('Brute.txt', 'w') as file:
    score1, s1 = BruteForceMotifSearch(DNA, len(DNA), len(DNA[0]), k)
    print("Score : " + str(score1) + '\n', file=file)

    for i, seq in enumerate(DNA):
        print(seq[s1[i]: s1[i] +k], file=file)
"""

     
#Greedy
with open('Greedy.txt', 'w') as file:
    score2, s2 = GreedyMotifSearch(DNA, k, len(DNA))
    print("Score : " + str(score2), file=file)

    for i, seq in enumerate(DNA):
        print(seq[s2[i]: s2[i] +k], file=file)
        
#Random
with open('Random.txt', 'w') as file:
    score3, s3 = RandomMotifSearch(DNA, k, len(DNA))
    print("Score : " + str(score3), file=file)

    for i, seq in enumerate(DNA):
        print(seq[s3[i]: s3[i] +k], file=file)


    
    
