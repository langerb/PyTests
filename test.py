import requests

from bs4 import BeautifulSoup


def countWordinWeb(url, word, depth):
    
  try:  
    page = requests.get(url)
  except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))
    return 0
    
  else:
  
    if (page.status_code > 200):
      return 0

    soup = BeautifulSoup(page.content, 'html.parser')

    pageText = list(soup.find_all('p'))
    raw = []

    count = 1
    for x in pageText:
	    raw.append(x.get_text())
    fullText = ' '.join(raw)
    #print(fullText)
    count = fullText.count(word)
    #print("Number of occurences: ", count)

    if depth <= 1:
      linkObjs = soup.find_all('a', href=True)
      linkSet = set()
      for linkObj in linkObjs:
        linkSet.add(str(linkObj['href']))

      for link in linkSet:
        if (link.count("http") == 0):
          sublink = url + link
        else:
          sublink = link
        newdepth = depth + 1
        print("depth: ", newdepth, "url: ", sublink)
        count = count + countWordinWeb(sublink, word, newdepth)
  
    return count
  
print("final result: ", countWordinWeb("https://www.microsoft.com", "data", 1))

#Value
#Zuehlke: 82
#Microsoft: 71
#d-one: 43

#Data
#D-One: 661
#Zuehlke: 211
#Microsoft: 733

