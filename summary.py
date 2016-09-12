import summarize
file1=open("infileSummary.txt","r").read()
file2=open("summarizeOutfile.txt","w")

text = summarize.summarize_text(file1)
#print(text)
text = str(text)
file2.write(text)