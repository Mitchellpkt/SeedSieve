# seedSieve.py
# IsthmusCrypto 2018.05
# see jupyter notebook demo
# github.com/Mitchellpkt/SeedSieve

# Inputs:
# rawStr: the string to be tested and/or redacted
# minimumSeedHits: How many seed words must be observed to trigger redaction
# seedRatio:  Minimum ratio (0,1) of seed:all words to trigger redaction
# wordlist: List of words to search for and redact 
# replaceWith: Short string to replace the redacted words

# demo:
# $ from seedSieve import *
# $ [outputString,qTriggered] = seedSieve("Very simple example", 1, 0.1, "word example simple test", "[#XYZ]");
# $ print(outputString)
# > "Very [#XYZ] [#XYZ]"

def seedSieve(rawStr, minimumSeedHits, seedRatio, wordlist, replaceWith):
    
    import re; # regular expressions

    # initialization
    qTriggered = 0; # init 0, whether to redact
    counts = 0; # init 0, num seed words counter
    foundThese = []; # init empty
    rawStrWords = rawStr.split();
    
    # count (loop) over words in the input string 
    for word in rawStrWords: 
        wordOnly = re.sub('[^A-Za-z]+', '',word.lower()); # lowercase & remove punctuation
        if wordOnly in wordlist:
            counts = counts + 1;
            foundThese.append(wordOnly)
            
    # Calculate ratio of seedwords to all words
    numWordsTotal = len(rawStr.split());
    actualRatio = counts/numWordsTotal;
        
    # set triggered if both criteria met
    if (actualRatio > seedRatio) and (counts > minimumSeedHits):
        qTriggered = 1;
    
    if(qTriggered):
        cleaningString = rawStr;
        for word in foundThese:
            cleaningString = re.sub(word, replaceWith, cleaningString, flags=re.I); 
        outputString = cleaningString
    else:
        outputString = rawStr;
    
    return [outputString, qTriggered]
