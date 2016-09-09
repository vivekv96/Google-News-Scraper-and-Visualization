from collections import Counter
import nltk
from nltk.corpus import stopwords
s1 = open("sample.txt","r+")
s2 = ""

s = set(stopwords.words('english'))

text = s1.read()

temp = filter(lambda w: not w in s,text.split())
#print(temp)

#tokenize the text
tokens = nltk.word_tokenize(text)
#tag the tokens.Example = Noun or verb etc
tagged = nltk.pos_tag(tokens)


for word in temp:
    #punctuation checking, you can make this more robust through regex if you want
    if word.endswith('.') or word.endswith('!') or word.endswith('?'):
        s2 += word[:-1] + " "
    else:
        s2 += word + " "

c = Counter(s2.lower().split())
#print(tagged)
print(c)
