import requests
import csv
from bs4 import BeautifulSoup

BASE_URL = "https://sellercentral.amazon.com/forums/"

PAGE = {'general': "c/selling-on-amazon/general-selling-questions", 'feedback': "c/selling-on-amazon/order-management-shipping-feedback-returns", 'new_sellers': "c/selling-on-amazon/help-for-new-sellers"}

count = 0

def analysis(filtered_titles, count):
    global general_topics
    global feedback_topics
    global new_seller_topics
    if count == 1:
        c = 0
        for t in filtered_titles:
            c += 1
        general_topics = c
    elif count == 2:
        c = 0
        for t in filtered_titles:
            c += 1
        feedback_topics = c
    else:
        c = 0
        for t in filtered_titles:
            c += 1
        new_seller_topics = c
    return general_topics
    return feedback_topics
    return new_seller_topics





for item in PAGE.values():
    page = requests.get(BASE_URL + item)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('a')
    del titles[0:3]
    del titles[len(titles)-7:]
    title_text = [t.getText() for t in titles]
    cleaned_titles = [t.replace('\n', '') for t in title_text]
    filtered_titles = [t for t in cleaned_titles if len(t) > 3]
    count += 1
    analysis(filtered_titles, count)



if (general_topics == feedback_topics and feedback_topics == new_seller_topics ):
    print("Each page has the same number of topics")

print("General topics " + str(general_topics))
print("Feedback topics " + str(feedback_topics))
print("New Seller topics " + str(new_seller_topics))







#print(soup.prettify())




