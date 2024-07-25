import nltk
import sys


TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to" | "until"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP Conj NP VP | NP VP P NP VP
VP -> V | V NP | V PP | Adv VP | VP Adv | VP  Conj VP
NP -> N | Det NP | AP NP | N PP | Conj NP | NP Adv
AP -> Adj | Adj AP | Adv AP
PP -> P NP

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


    if len(sys.argv) >= 2:
        if not os.path.exists(sys.argv[1]):
            print("File does not exist.")
            return
        with open(sys.argv[1], 'r') as f:
            s = f.read()

    try:
        trees = list(parser.parse(s))
    except nltk.ParseException as e:
        print(e)
        return


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    words=[]


    for word in nltk. word_tokenize(sentence):
        for i in word:
            if (i.isalpha()):
                words.append(word.casefold())
                break
    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    l=[]
    for s in tree.subtrees(lambda t: t.label()=="NP"):
        m=0
        for i in s.subtrees(lambda t: t.label()=="NP"):
            m+=1
        if m==1:
            l.append(s)
    return l


if __name__ == "__main__":
    main()
