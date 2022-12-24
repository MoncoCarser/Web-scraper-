from bs4 import BeautifulSoup
import requests

    
res = requests.get("https://news.ycombinator.com")
soup =  BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")

res2 = requests.get("https://news.ycombinator.com/?p=2")
soup2 =  BeautifulSoup(res2.text, "html.parser")
links2 = soup2.select(".titleline > a")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2


    
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, reverse=True)

def create_custom_HN(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):  
            points = int(vote[0].getText().replace(" points", ""))
            if points >100:
                hn.append(f"{points} - {title},\n {href}")
    return sort_stories_by_votes(hn)

    

hn = create_custom_HN(mega_links, mega_subtext)

for item in hn:
    print(item)
    print()