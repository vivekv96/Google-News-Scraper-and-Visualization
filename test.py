import nltk
s1 = open("sample.txt", "r+")
text = s1.read()
tokens = nltk.word_tokenize(text)

#print(text)

print(tokens)