import itertools 
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
topStories = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&output=rss").read()
worldNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=w&output=rss").read()
businessNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=b&output=rss").read()
techNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=tc&output=rss").read()
entertainmentNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=e&output=rss").read()
sportsNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=s&output=rss").read()
scienceNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=snc&output=rss").read()
healthNews = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=m&output=rss").read()
'''
def f1(choice):
	try:
		if(choice == '1'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&output=rss").read()
		elif(choice == '2'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=w&output=rss").read()
		elif(choice == '3'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=b&output=rss").read()
		elif(choice == '4'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=tc&output=rss").read()
		elif(choice == '5'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=e&output=rss").read()
		elif(choice == '6'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=s&output=rss").read()
		elif(choice == '7'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=snc&output=rss").read()
		elif(choice == '8'):
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&topic=m&output=rss").read()
		elif(choice == '9'):
			q = input("Enter query to be searched for :")
			linkChoice = urlopen("http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&output=rss&q=" + str(q).replace(" ","+")).read()
		else:
			print("Wrong Choice !!!")
			quit()
		bsObj = BeautifulSoup(linkChoice,"html.parser")
		bsObj.prettify()
		for title, link in zip(bsObj.findAll("title"), bsObj.findAll("link")):
			print(title.get_text())
			print(link.get_text())
			#articleUrl = re.search(b'url=\$', title, re.M|re.I)
			#print(articleUrl)
	except Exception as e:
		print(e)


print("1.Top Stories")
print("2.World News")
print("3.Business")
print("4.Tech")
print("5.Entertainment")
print("6.Sports")
print("7.Science")
print("8.Health")
print("9.Search for something")

choice = input("Enter choice number :")
f1(choice)
