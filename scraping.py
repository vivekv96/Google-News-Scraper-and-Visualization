import unirest
import json

response = unirest.get("https://dev132-toi-times-of-india-v1.p.mashape.com/news?token=YUhSMGNEb3ZMM1JwYldWemIyWnBibVJwWVM1cGJtUnBZWFJwYldWekxtTnZiUzltWldWa2N5OXVaWGR6Wm1WbFpDOHRNakV5T0Rrek5qZ3pOUzVqYlhNL1ptVmxaSFI1Y0dVOWMycHpiMjQ9NTc1ZDZlMzE0MmViMA%3D%3D",
  headers={
    "X-Mashape-Key": "eFwRSmDkTkmshEeijgMRWdjoTPaGp1FRLEkjsn2vpnq1PQ9DMt",
    "Accept": "application/json"
  }
)

jsonFile = response.body
with open('sample.json','w') as outfile:
	json.dump(jsonFile,outfile)

with open('sample.json','r') as infile:
	some_dict = json.load(infile)

story=[]
headline=[]
url=[]
#a = json.loads(some_dict)
for i in range(10):
	story.append(some_dict["NewsItem"][i]["Story"])
	headline.append(some_dict["NewsItem"][i]["HeadLine"])
	url.append(some_dict["NewsItem"][i]["WebURL"])

print(url[0])
print(headline[0])
print(story[0])

