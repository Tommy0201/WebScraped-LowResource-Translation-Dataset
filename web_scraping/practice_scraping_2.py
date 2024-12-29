import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pickle
import os
import time
import concurrent.futures


# SCRAPING ONE PAGE
def has_html_children(soup_obj):
    if isinstance(soup_obj,str):
        return False
    child_elements = soup_obj.find_all(lambda tag: isinstance(tag, (Tag, NavigableString)) and len(tag.find_all()) > 0)
    return len(child_elements) > 0 

def print_text(soup_obj,out):
    if has_html_children(soup_obj) == False:
                strip_soup = soup_obj.text.strip()
                # if  "function" not in strip_soup and "Morph.toInit.bundles.push(function()" not in strip_soup and "var bs_ajax_paginate" not in strip_soup and "Morph.toInit.payloads.push(function()" not in strip_soup and "@-moz-keyframes" not in strip_soup and "sc-component-id:" not in strip_soup:
                if "function" not in strip_soup and "Moprh." not in strip_soup and "Morph.init();" not in strip_soup and "var bs_ajax_paginate" not in strip_soup and "require.config" not in strip_soup:
                    out.add(strip_soup)
    else:
        for element in soup_obj:
            print_text(element,out)

def scrape_a_page(url):
    out = set()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find_all('div')
    for div in content:
        print_text(div,out)
    out1= list(out)
    return "\n".join(out1)





# FINDING ALL HYPERLINKS OF A WEBPAGE AND SAVE IT TO A FILE


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

# def find_hyperlinks(URL):
#     set_url = set()
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content,"html.parser")
#     article_elements = soup.find_all("a")
#     for article in article_elements:
#         if article.get("href") and article["href"].startswith(URL[:11]):
#             if 'wp-login' not in article["href"] and 'jpeg' not in article["href"]:
#                 set_url.add(article['href'])
#     return(set_url)

# def update_set_url(set_url,URL):
#     urls_to_process = list(set_url)
#     index = len(set_url)
#     for i in range(index-1,index-300,-1):
#         set_url.update(find_hyperlinks(urls_to_process[i]))
#         if (i + 1) % 100 == 0:
#             time.sleep(7) 
#     set_name = "set_url_" + URL[11:] + ".txt"
#     with open(set_name, 'wb') as file:
#             pickle.dump(set_url, file)
        
def update_set_url(set_url):
    urls_to_process = list(set_url)
    index = len(set_url)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(9778,9959):
            if (i+1)%100 == 0:
                time.sleep(5)
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
    # set_name = "set_url_" + URL[11:] + ".txt"
    with open("set_url_bbc.txt", 'wb') as file:
        pickle.dump(set_url, file)
    file.close()

# SAVE THE HYPERLINKS TO A SET AND STORE IN A FILE TO KEEP TRACK OF THE DATASET EASIER. ALSO PROVIDE CODE TO ACCESS THE SET. (DOES NOT INCLUDED IN THE CHUNKY CODE)
# URL = "https://www.bbc.com/pidgin"
URL = "https://www.bbc.com/igbo"
# with open("set_url_bbc.txt", "rb") as f:
#     set_url = pickle.load(f)

# print(len(set_url))
# update_set_url(set_url)
# with open('set_url_bbc.txt', 'rb') as file:
#     set_url= pickle.load(file)
# print(len(set_url))
# file.close()



# FINDING ALL THE TEXT CONTENT OF A WEBPAGE AND SAVE IT TO A FILE
# def scraping_a_webpage(set_url,URL,index):
#     list_url = list(set_url)
#     if "http:" in URL:
#         file_name = URL.replace("http://", "") + ".txt"
#     elif "https" in URL:
#         file_name = URL.replace("https://", "") + ".txt"
#     directory = os.path.dirname(os.path.abspath(__file__))
#     os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
#     if os.path.exists(file_name):
#         mode = "a"
#     else:
#         mode = "w"
#     with open(file_name, mode, encoding="utf-8") as file:
#         for i in range(index, len(set_url)):
#             if (i+1)%100 ==0:
#                 time.sleep(7)
#             scraped_text = scrape_a_page(list_url[i])
#             file.write(scraped_text + "\n")
#     print("Scraping Complete")


def scraping_a_webpage(set_url,index):
    list_url = list(set_url)
    file_name = "bbc_igbo.txt"
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
        for i in range(index, 6732):
            if (i+1)%100 ==0:
                time.sleep(3)
            try: 
                scraped_text = scrape_a_page(list_url[i])
                file.write(scraped_text + "\n")
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
    print("Scraping Complete")


# scraping_a_webpage(set_url,URL,8000)

