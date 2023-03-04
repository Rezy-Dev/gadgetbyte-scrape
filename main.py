import pandas as pd
import requests
from bs4 import BeautifulSoup

productName = []
price = []
details = []


for i in range(2, 14):
    url = f"https://www.gadgetbytenepal.com/cat/mobile/page/{i}"
    # url = "https://www.gadgetbytenepal.com/cat/mobile/page/5/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")


    # GETTING PRODUCT NAMES
    names = soup.find_all("h3", class_ = "woocommerce-loop-product__title")
    for i in names:
        name = i.text
        productName.append(name)


    # GETTING PRODUCT PRICES
    prices = soup.find_all("span", class_ = "woocommerce-Price-amount amount")
    for i in prices:
        pricee = i.text
        newP = pricee[3:]
        PP = newP.replace(",", "")
        price.append(int(PP))


    # GETTING details
    detailsssss = soup.find_all("div", class_ = "specifications-wrap")
    for i in detailsssss:
        name = i.text
        details.append(name)
# print(details)


df = pd.DataFrame({"Product Name": productName, "price": price, "descriptions": details})
print(df)
