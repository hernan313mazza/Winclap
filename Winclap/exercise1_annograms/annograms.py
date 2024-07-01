import pathlib


def isAnnograms(word1, word2):
    list_word1=list(word1)
    list_word2=list(word2)
    list_word1.sort()
    list_word2.sort()
    return list_word1==list_word2

def annograms(word):
    
    try:
        words = [w.rstrip().lower() for w in open(f'{pathlib.Path(__file__).parent.resolve().joinpath("WORD.lst")}')]

        list_words=list()
        for w in words:
            if( isAnnograms(w, word.rstrip().lower())):
                list_words.append(w)
    except(FileNotFoundError):
        print(f'The "WORD.lst" file must exist in the directory: {pathlib.Path(__file__).parent.resolve()}.')    
        list_words=None
    return list_words

if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))
