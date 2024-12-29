import requests
from bs4 import BeautifulSoup


# def check_url(set_url):
#     urls_to_check = set_url.copy()
#     for each_url in urls_to_check:
#         if "https://www.bbc.com/pidgin" in each_url:
#             set_hyperlinks = find_hyperlinks(each_url)
#             set_url.update(set_hyperlinks


# check_url(set_url)
# check_url(set_url)
# check_url(set_url)
# check_url(set_url)


# print(set_url)    


# def check_hyperlinks(url): 
#     set_hyperlink = set()
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     hyperlink_elements = soup.find_all("a")
#     for hyperlink in hyperlink_elements:
#         if hyperlink.get("href") and hyperlink["href"].startswith("/"):
#             hyperlink_url = url + hyperlink['href']
#             set_hyperlink.add(hyperlink_url)
#     if len(set_hyperlink) > 0:
#         return True
#     else:
#         return False

    


# FIRST DEMO THAT ACTUALLY WORKS ACCORDING TO MY WANT
# demo = soup.find_all('div',attrs={'class':'bbc-14gzkm2 e718b9o0'})
# for div in demo:
#     for section in div:
#         print(section.text.strip())

# SECOND DEMO
# demo2  = soup.find_all('section',attrs={'class':'bbc-iinl4t euhul101'})
# there must be a code to handle the last section


# for section in content:
#     print_text(section)


# THIRD DEMO THAT ACTUALLY WORKS          

# html = """
# <div dir="ltr" class="bbc-14gzkm2 e718b9o0">
# <h3 class="bbc-dvfk01 ea6by782">
# <a href="/pidgin/articles/cv2j9er1e0po" aria-labelledby="promo-pidginarticlescv2j9er1e0po-text-1" class="focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0">
# <span id="promo-pidginarticlescv2j9er1e0po-text-1">Why lawmakers dey stay office longer dan president for Nigeria?</span>
# </a>
# </h3>

# <p class="bbc-dvyt8e ea6by781">Di tenure of di 9th Assembly for go end on Sunday 11 June, but becos 12 June na public holiday being Democracy day, di inauguration dey expected to hold on 13 June, wen di president go make di official proclamation of di 10th Assembly.</p>
# <time datetime="2023-06-05" class="bbc-idwms3 e1mklfmt0">52 minutes wey don pass</time>

# <div data-e2e="index-alsos" class="bbc-1p4i6rh e1p0xx4z3">
# <h4 class="bbc-m04vo2">Another thing we de for inside dis tori</h4>
# <ul role="list" class="bbc-1kz5jpr e1p0xx4z1">
# <li role="listitem" class="bbc-16wjryy e1p0xx4z2"><a href="/pidgin/tori-65747253" class="focusIndicatorDisplayInlineBlock bbc-oqw416 e1p0xx4z0">
# <span>Key points from President Bola Tinubu inauguration speech</span>
# </a></li>
# <li role="listitem" class="bbc-16wjryy e1p0xx4z2"><a href="https://www.bbc.com/pidgin/articles/c6pvlwd57d7o" class="focusIndicatorDisplayInlineBlock bbc-oqw416 e1p0xx4z0">
# <span>Tins to know about Femi Gbajabiamila and di work of Chief of Staff</span>
# </a></li>
# </ul>
# </div>

# </div>
# """

# demo_soup = BeautifulSoup(html,'html.parser')
# print_text(demo_soup)


# URL can be a list of URLs stands for ultimate resources locator?
URL = 'https://realpython.github.io/fake-jobs'
# Must written line, first is to get the link and set it equals a variable. Second is to call the Beautiful Soup function
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")

# out = soup.find(id="ResultsContainer")
#job_elements find all the "div" html element whose are in the "card-content" class
job_elements = soup.find_all("div",class_="card-content")
# print(job_elements)

#using a for loop to access each job element, and set each factors such as title, location, company to variables. Then.text.strip and print them. 
for job_element in job_elements:
    title = job_element.find(class_="title")
    location = job_element.find(class_="location")
    company = job_element.find(class_="company")
    # print(title.text.strip())
    # print(location.text.strip())
    # print(company.text.strip(), end='\n'*2)


