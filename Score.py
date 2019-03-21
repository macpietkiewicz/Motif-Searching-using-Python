"""-----------------------FUNKCJE-------------------------------------------"""

def Score(s, DNA, k):
    aligment = []
    profile = []
    score = 0
    
    
    
    for i, row in enumerate(DNA):
        aligment.append(row[s[i] : s[i] + k])
            
    for j in range(0, k):
        List = []
        for i in range(0, 4):
            List.append(0)
        profile.append(List)
    

    for j in range(0, k):
        for i in range(0, len(aligment)):
                
            if aligment[i][j] == 'a':
                profile[j][0] += 1
                            
            elif aligment[i][j] == 'c':
                profile[j][1] += 1
                        
            elif aligment[i][j] == 'g':
                profile[j][2] += 1
                        
            else:
                profile[j][3] += 1
                        
            assert aligment[i][j] == 'a' or aligment[i][j] == 'c' or \
            aligment[i][j] == 't' or aligment[i][j] == 'g', "Błąd w DNA!!!"
                    
                       
    for column in profile:
        score += max(column)
    
    assert score > 0, "Funkcja Score nie działa poprawnie !!!"
    
    return(score)
    
    
    
def Profile(motifs, DNA, k):
    profile = []
    
    for x in range(0, k):
        List = []
        for j in range(0,4):
            List.append(0)
        profile.append(List)
        
    for i in range(0, k):
        Count_a = 0
        Count_t = 0
        Count_c = 0
        Count_g = 0
        
        for j in range(0, len(motifs)):
            """ Sprawdzam jaki jest znak, a następnie zwiększam odpowiednią wartosć"""
            if DNA[j][motifs[j] + i] == 'a':
                Count_a += 1
                
            elif DNA[j][motifs[j] + i] == 'c':
                Count_c += 1
            
            elif DNA[j][motifs[j] + i] == 'g':
                Count_g += 1
            
            else:
                Count_t += 1
                
        profile[i][0] = Count_a / len(DNA) + 1
        profile[i][1] = Count_c / len(DNA) + 1
        profile[i][2] = Count_g / len(DNA) + 1
        profile[i][3] = Count_t / len(DNA) + 1
        
    return(profile)
    
def MostPropabilityFromProfile(seq, profile, k):
    MostPro = 0
    
    for i in range(0, len(seq) - k):
        propability = 1
        kmer = seq[i : i+k]
        
        for j, nucleotide in enumerate(kmer):
            
            if nucleotide == 'a':
                propability = propability * profile[j][0]
            
            elif nucleotide == 'c':
                propability = propability * profile[j][1]
                
            elif nucleotide == 'g':
                propability = propability * profile[j][2]
                
            else:
                propability = propability * profile[j][3]
                
        if propability > MostPro:
            MostPro = propability
            BestKmer = i
    
    return(BestKmer)
    

"""---------------------------TESTY-----------------------------------------"""
            
if __name__ == '__main__':
    
    DNA = ('ccacataacgatcacgcgcggttcaacgactgcaattggcacgaggatcacttacctggccaatgcgatt',
           'gtgcgcaacttgtggacagcgcctcagacctgtctgcctctgcaaggctagagaattcgaagtacattcc',
           'agagttttttagtgcagggtttatatacctgcgtaaacccttcatactggactccacatgcgtcacaagt',
           'agggccgctgggtagcgcaagtcgactttcgatgatacgtggtagccttaggcgctttcgcaccgaaaca'
           )

    DNA2 = ('cctttgtgaagaggccagtgttatggcccttctcg',
            'cacatggaccttcggcgtgtgaaacttcaacggga',
            'agtatacacgactcgggcaaacaggtccatttgac',
            'actggttaagacgttagagtcgcccgcccccgtcc'
            )
    
    s = [2, 1, 10, 5]
    k = 8
    MostPro = []
    
    print("Score : " + str(Score(s, DNA, k)))
    print("Profil dla motywu : ")
    
    for i, seq in enumerate(DNA):
        print(seq[s[i]: s[i] + 8])
    print("to : " + str(Profile(s, DNA, k)))
        
    for seq in DNA2:
        MostPro.append(MostPropabilityFromProfile(seq,Profile(s, DNA, k), k))
    print("Najbardziej podobny do tego profilu z DNA2 jest motyw : ")
    
    for i, seq in enumerate(DNA2):
        print(seq[MostPro[i]: MostPro[i] + 8])
        
    print("Jej profil to: " + str(Profile(MostPro,DNA2, k)))
        
        
                
            
                    