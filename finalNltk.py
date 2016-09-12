import nltk
import sys
import string
from nltk.corpus import stopwords

stopset = set(nltk.corpus.stopwords.words('english'))
file1 = open("output.tsv","w")
article = open("input.txt","r").read()
table = string.maketrans("","")
article = article.translate(table, string.punctuation)
tokens = nltk.word_tokenize(article)
tagged = nltk.pos_tag(tokens)
filtered_words = [word for word in tokens if word not in stopset]

#Word Count part :-

clean_tokens = []
for word in filtered_words:
    if word.isalpha():
        clean_tokens.append(word)

fd = nltk.FreqDist(clean_tokens)
file1.write("word"+"	"+"freq"+"\n")
for token in fd:
	file1.write(str(token)+"	"+str(fd[token])+"\n")
