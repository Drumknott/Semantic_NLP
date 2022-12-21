import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("eggs")
word2 = nlp("milk")
word3 = nlp("cat")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
In this example I've used the words Eggs, Milk and Cat. Eggs and milk are more similar to each other than to cat as they 
are both foods, but cat is more similar to milk than eggs as cats are associated with drinking milk.

using 'en_core_web_sm' rather than 'en_core_web_md' produces higher similarity results but won't be as accurate as the 
similarities are based on tags rather than vectors. 
'''
