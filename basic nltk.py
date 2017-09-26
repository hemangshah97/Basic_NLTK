# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:48:16 2017

@author: Admin
"""

    from nltk.stem import WordNetLemmatizer 
    wnl = WordNetLemmatizer() 
    words = ["game","gaming","gamed","games", 'engineering', 'engineers', 'resumes', 'resumed', 'resuming'] 
    print ('Output of Wordnet Lemmatizer (only nouns)')
    for word in words: 
        print(wnl.lemmatize(word)) 
    print ('Output of Wordnet Lemmatizer (for verbs)')
    for word in words: 
        print(wnl.lemmatize(word, pos='v')) 

    import nltk 
    line = 'I am the king of the world' 
    print ('Sentence: ', line) 
    sentences = nltk.sent_tokenize(line) #tokenize sentences 
    nouns = [] #empty to hold all nouns 
    for sentence in sentences: 
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))): 
            print (word, '/', pos) 
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))): 
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):  # to extract only nouns 
                 nouns.append(word) 
        print (nouns) 
        
    from nltk import word_tokenize, ne_chunk, pos_tag 
    sentence = 'Barack Obama meets Michael Jackson in Nihonbashi' 
    token = word_tokenize(sentence ) 
    postag = pos_tag(token) 
    chunked = ne_chunk(postag) 
    for i in chunked: 
        print (i) 
        
        
    import nltk 
    your_grammar = nltk.CFG.fromstring(""" 
    S -> V NP 
    V -> 'describe' | 'present' 
    NP -> PRP N  
    PRP -> 'your'  
    N -> 'work' 
    """) 
    parser = nltk.ChartParser(your_grammar) 
    sent = 'describe your work'.split() 
    print ('Sentence: ', sent )
    print ('') 
    print ('Parsing output')
    print (list(parser.parse(sent))) 
    
    from nltk.corpus import wordnet as wn 
    for i,j in enumerate(wn.synsets('man')): 
        print (j.lemma_names())     #[u'book', u'volume'] 
        print  (", ".join(j.lemma_names()))  #book, volume 
        print ('') 


    from nltk.corpus import wordnet as wn 
    book = wn.synset('book.n.02')  # 2nd sense 
    print ('Synonyms: ', book.lemma_names() )
    print ('' )
    print ('Hypernyms: ', book.hypernyms() )
    print ('' )
    print ('Hyponyms: ', book.hyponyms() )
    print ('' )
    print ('Holonyms: ', book.member_holonyms() )

    from nltk.corpus import wordnet as wn 
    #book = wn.synset('book.n.01')  # 1st sense 
    print ('Antonyms: ', wn.lemma('good.a.01.good').antonyms())
    print ('Antonyms: ', wn.lemma('slow.a.01.slow').antonyms())
    print ('Antonyms: ', wn.lemma('increase.v.01.increase').antonyms())
    print ('Antonyms: ', wn.lemma('boy.n.01.boy').antonyms())
    

    from nltk.corpus import wordnet as wn 
    hit = wn.synset('man.n.01') 
    slap = wn.synset('boy.n.01') 
    dog = wn.synset('dog.n.01') 
    cat = wn.synset('cat.n.01') 
    print ('Wu-Palmer Similarity' )
    print ('man & boy: ', wn.wup_similarity(hit, slap))     # Wu-Palmer Similarity 
    print ('dog & cat: ', wn.wup_similarity(dog, cat) )
    print ('' )
    print ('Leacock-Chodorow Similarity' )
    print ('man & boy: ', wn.lch_similarity(hit, slap))     # Leacock-Chodorow Similarity 
    print ('dog & cat: ', wn.lch_similarity(dog, cat) )


    from nltk.corpus import wordnet as wn 
    from nltk.corpus import genesis 
    #from nltk.corpus import brown 
    genesis_ic = wn.ic(genesis, False, 0.0) 
    #brown_ic = wn.ic(brown, False, 0.0) 
    hit = wn.synset('hit.v.01') 
    slap = wn.synset('slap.v.01') 
    dog = wn.synset('dog.n.01') 
    cat = wn.synset('cat.n.01') 
    print ('Jiang-Conrath Similarity' )
    print ('hit & slap: ', hit.jcn_similarity(slap, genesis_ic))     # Jiang-Conrath Similarity 
    print ('dog & cat: ', dog.jcn_similarity(cat, genesis_ic) )
    print ('' )
    print ('Resnik Similarity' )
    print ('hit & slap: ', hit.res_similarity(slap, genesis_ic))     # Resnik Similarity 
    print ('dog & cat: ', dog.res_similarity(cat, genesis_ic) )
    print ('' )
    #print 'Lin Similarity using Brown IC' 
    #print 'hit & slap: ', hit.lin_similarity(slap, brown_ic)     # Lin Similarity 
    #print 'dog & cat: ', dog.lin_similarity(cat, brown_ic) 
    print ('' )
    print ('Lin Similarity using Genesis IC' )
    print ('hit & slap: ', hit.lin_similarity(slap, genesis_ic))     # Lin Similarity 
    print ('dog & cat: ', dog.lin_similarity(cat, genesis_ic) )
