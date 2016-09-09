import nltk 
s1 = "My name is Vivek"
t = nltk.word_tokenize(s1)
tag = nltk.pos_tag(t)
print(tag)