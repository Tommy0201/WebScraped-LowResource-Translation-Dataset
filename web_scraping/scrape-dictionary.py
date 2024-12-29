import requests
from bs4 import BeautifulSoup
import os
import time
import pickle

# CODE TO CREATE A LIST OF ALL URLS AVAILABLE

def find_hyperlinks(URL):
    list_url = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    elements = soup.find_all("div", class_='container content')
    for div in elements:
        article_elements = div.find_all("a")
        for article in article_elements:
            if article.get("href") and article["href"].startswith("/words"):
                    article_link = 'http://naijalingo.com'+article['href']
                    list_url.append(article_link)
        return(list_url)


alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_url = [ 'http://naijalingo.com/words/' + x + '/alphabet' for x in alphabets]


list_word_url = []

for url in alphabet_url:
    new_urls = find_hyperlinks(url)
    list_word_url += new_urls

file_name = "list_url_" + 'naijalingo' + '.txt'
with open(file_name,'wb') as file:
     pickle.dump(list_word_url,file)
file.close()

# CODE TO SCRAPE THE LINKS

def scrape_a_page(url):
    out = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find_all('div', class_="left clearBoth")
    for div in content:
        out.append(div.text.strip())
    return "\n".join(out)


def scraping_a_webpage(list_url,index):
    file_name = 'naijalingo.com.txt'
    # if "http:" in URL:
    #     file_name = URL.replace("http://", "") + ".txt"
    # elif "https" in URL:
    #     file_name = URL.replace("https://", "") + ".txt"
    directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    if os.path.exists(file_name):
        mode = "a"
    else:
        mode = "w"
    with open(file_name, mode, encoding="utf-8") as file:
        for i in range(index,len(list_url)):
            if (i+1)%100 ==0:
                time.sleep(5)
            scraped_text = scrape_a_page(list_url[i])
            file.write(scraped_text + "\n")
    print("Scraping Complete")

URL = 'http://naijalingo.com/'


file_name = "list_url_" + 'naijalingo' + '.txt'
with open(file_name,'rb') as file:
     word_urls =pickle.load(file)
print(len(word_urls))



scraping_a_webpage(word_urls,1000)
