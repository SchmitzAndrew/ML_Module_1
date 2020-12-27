import requests
import csv
from bs4 import BeautifulSoup

BASE_URL = "https://sellercentral.amazon.com/forums/"

PAGE = {'general': "c/selling-on-amazon/general-selling-questions", 'feedback': "c/selling-on-amazon/order-management-shipping-feedback-returns", 'new_sellers': "c/selling-on-amazon/help-for-new-sellers"}

for item in PAGE.values():
    page = requests.get(BASE_URL + item)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('a')
    del titles[-1]
    print(titles)


    #print(soup.prettify())




