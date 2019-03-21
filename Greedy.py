"""-------------------------IMPORT------------------------------------------"""

from Score import Score, Profile, MostPropabilityFromProfile


"""-------------------------FUNKCJE-----------------------------------------"""

def GreedyMotifSearch(DNA, k, t):
    BestMotifs = []
    motifs = []
    
    for seq in DNA:
        BestMotifs.append(0)
        motifs.append(0)
        
    for j in range(0, len(DNA[0]) - k):
        motifs[0] = j
        for i in range(1, t):
            profil = Profile(motifs, DNA, k)
            motifs[i] = MostPropabilityFromProfile(DNA[i], profil, k)
        
        if Score(motifs, DNA, k) > Score(BestMotifs, DNA, k):
            BestMotifs = motifs
    
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
    
    score, s = GreedyMotifSearch(DNA, 3, len(DNA))
    print("Score : " + str(score))
    
    for i, seq in enumerate(DNA):
        print(seq[s[i]:s[i] + 3])
    
