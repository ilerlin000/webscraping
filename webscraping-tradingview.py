from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

companies = soup.findAll("span",attrs={"calss":"tv-screener_description"})

print(companies)

for company in companies[:5]:
    print(company.text.strip())




    

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

stock_table = soup.findAll('tbody')
# tbody means the body of the table

stock_table = stock_table[0]
# first element in the list 0 - first full table

rows = stock_table.findAll('tr')
# tr = table rows 

for row in rows[:5]:
    cols = row.findAll('td')
    print(cols[0])
    # extract the name, price, change %
    name = cols[0].find("span",attrs ={'class':'tv-screener__description'})
    name = name.text.strip()
    price = float(cols[1].text)
# change % - cannot use float bc it has a % in it - so you have to strip 
    change_text = cols[2].text
    change_float = float(cols[2].text.strip('%'))

    s_price = round(price/(1+change_float),2)

    print(f"Compnay Name: {name}")
    print(f"Current Price: {price}")
    print(f"% Change: {change_text}")
    print(f"Starting Price: {s_price}")
    input()

