"""-------------------------IMPORT------------------------------------------"""

import random
from Score import Score, Profile, MostPropabilityFromProfile


"""-------------------------FUNKCJE-----------------------------------------"""

def RandomMotifSearch(DNA, k, t):
    motifs = []
    
    for i in range(0, t):
        index = random.randint(0, len(DNA[0]) - k)
        motifs.append(index)
        
    BestMotifs = motifs
    
    while True:
        profile = Profile(motifs, DNA, k)
        
        for n in range(0, t):
            motifs[n] = MostPropabilityFromProfile(DNA[n], profile, k)
        
        if Score(motifs, DNA, k) > Score(BestMotifs, DNA, k):
            BestMotifs = motifs
        
        else:
            return(Score(BestMotifs, DNA, k), BestMotifs)


    
    
"""-------------------------TESTY-------------------------------------------"""

if __name__ == '__main__':
    
    DNA = (
            'tggatcgctcggattctcagaggaa',
            'actcgcaggagcgcccaaggttgct',
            'cgtggtccccaccacgggctaaggc',
            'tcagtagcatccgcacacttggagc',
            'aaatcgcttcgtgccgtgtgcaagc'
    )
    
    score, s = RandomMotifSearch(DNA, 3, len(DNA))
    print("Score : " + str(score))
    
    for i, seq in enumerate(DNA):
        print(seq[s[i]:s[i] + 3])
    