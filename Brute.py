"""-------------------------IMPORT------------------------------------------"""

from Score import Score


"""-------------------------FUNKCJE-----------------------------------------"""

def BruteForceMotifSearch(DNA, t, n, l):
    BestScore = 0
    s = []
    
    for i in range(0, t):
        s.append(0)
    
    for i in range(0, pow((n-l), t) - 1):
        for j in range(0, len(s)):
            #print(s)
            if s[j] == n-l:
                s[j] = 0
                s[j+1] += 1
            
        if Score(s, DNA, l) > BestScore:
            BestScore = Score(s, DNA, l)
            #print(BestScore)
            BestMotif = s
        
        s[0] += 1
    
    return(BestScore, BestMotif)
    
    
"""-------------------------TESTY-------------------------------------------"""

if __name__ == '__main__':
    
    DNA = (
            'tggatcgctcggattctcagaggaa',
            'actcgcaggagcgcccaaggttgct',
            'cgtggtccccaccacgggctaaggc',
            'tcagtagcatccgcacacttggagc',
            'aaatcgcttcgtgccgtgtgcaagc'
    )
    
    score, s = BruteForceMotifSearch(DNA, len(DNA), len(DNA[0]), 3)
    print("Score : " + str(score))
    
    for i, seq in enumerate(DNA):
        print(seq[s[i]:s[i] + 3])