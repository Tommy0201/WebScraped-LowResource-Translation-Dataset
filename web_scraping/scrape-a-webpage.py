from practice_scraping_2 import  find_hyperlinks, scraping_a_webpage
from practice_scraping_2 import scrape_a_page, has_html_children,print_text
import requests
import pickle
import concurrent.futures
import time
from bs4 import BeautifulSoup

def update_set_url(set_url):
    urls_to_process = list(set_url)
    index = len(set_url)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(6500,6706):
            if (i+1)%100 == 0:
                time.sleep(8)
            try: 
                set_url.update(executor.submit(find_hyperlinks,urls_to_process[i]).result())
            except requests.exceptions.ConnectionError:
                print("ConnectionTimeout occurred. Retrying..")
                time.sleep(5)
            except requests.exceptions.ReadTimeout:
                print("ReadTimeout occurred. Retrying...")
                time.sleep(5) 
            except AssertionError as e:
                print("AssertionError occurred...")
                print(f"Error message: {e}")
                time.sleep(5) 
    set_name = "set_url_bbc.com.igbo.txt"
    with open(set_name, 'wb') as file:
        pickle.dump(set_url, file)
    file.close()


def find_hyperlinks(URL):
    set_url = set()
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    article_elements = soup.find_all("a")
    for article in article_elements:
        if article.get("href") and article["href"].startswith("/igbo"):
            article_url = "https://www.bbc.com" + article['href']
            if article_url not in set_url:
                set_url.add(article_url)
    return(set_url)

# def web_scraper(URL):
#     set_url = find_hyperlinks(URL)
#     set_name = "set_url_bbc.com.igbo.txt"
#     with open(set_name,"wb") as file:
#          pickle.dump(set_url,file)
#     print(len(set_url))
#     file.close()
    # scraping_a_webpage(set_url,URL,0)

# def continue_web_scraper(URL):
#     set_name = "set_url_" + URL[7:] +".txt"
#     with open(set_name,"rb") as file:
#         set_url=pickle.load(file)
#     prev_set = len(set_url)
#     update_set_url(set_url,URL)
#     print(len(set_url))
#     scraping_a_webpage(set_url,URL,prev_set)


# def specified_web_scraper(URL,index):
#     set_name = "set_url_" + URL[7:] +".txt"
#     with open(set_name,"rb") as file:
#         set_url=pickle.load(file)
#     scraping_a_webpage(set_url,URL,index)

    
# URL = "https://www.bbc.com/pidgin"
# URL = "http://igbo.von.gov.ng"
URL = "https://www.bbc.com/igbo"
# web_scraper(URL)
# continue_web_scraper(URL)
# specified_web_scraper(URL,131)



set_name = "set_url_bbc.com.igbo.txt"
# CODE TO UPDATE THE SET
# with open(set_name,"rb") as file:
#     set_url=pickle.load(file)
# print(len(set_url))
# update_set_url(set_url)
with open(set_name,"rb") as file:
    set_url=pickle.load(file)




# updated_set = {x for x in set_url if (".jpg" not in x and ".webp" not in x) }
# with open(set_name, 'wb') as file:
#     pickle.dump(updated_set, file)
# print(len(set_url))
print(len(set_url))
scraping_a_webpage(set_url,6000)
# update_set_url(set_url,URL)
# with open(set_name,"rb") as file:
#     set_url=pickle.load(file)

# print(len(set_url))
