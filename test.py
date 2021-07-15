import requests

from bs4 import BeautifulSoup


def countWordinWeb(url, word, depth):

  print("depth:", depth, "url", url)

  try:  
    page = requests.get(url)
  except requests.RequestException as e:
    print(str(e))
    return 0
    
  else:
    soup = BeautifulSoup(page.content, 'html.parser')

    # extract text paragraphs
    pageText = list(soup.find_all('p'))
    raw = []
    count = 0
    # make one big string
    for x in pageText:
	    raw.append(x.get_text())
    fullText = ' '.join(raw)
    # count the word
    count = fullText.count(word)

    # follow links on page
    if depth <= 1:
      linkObjs = soup.find_all('a', href=True)
      linkSet = set()
      for linkObj in linkObjs:
        linkSet.add(str(linkObj['href']))

      # see if it is a relative link or an absolute link
      for link in linkSet:
        if (link.count("http") == 0):
          sublink = url + link
        else:
          sublink = link

        # recursive call
        count = count + countWordinWeb(sublink, word, depth + 1)
  
    return count
  
print("final result: ", countWordinWeb("https://www.d-one.ai", "data", 1))

#Value
#Zuehlke: 82
#Microsoft: 71
#d-one: 43

#Data
#D-One: 661
#Zuehlke: 211
#Microsoft: 733

