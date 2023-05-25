from bs4 import BeautifulSoup
import requests
import re

website = 'https://www.flipkart.com/apple-iphone-14-starlight-128-gb/product-reviews/itm3485a56f6e676?pid=MOBGHWFHABH3G73H&lid=LSTMOBGHWFHABH3G73HVXY5AV&marketplace=FLIPKART'
page_number = 0
review_page = website + '&page=' + str(page_number)
result = requests.get(review_page)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

txts = [ x.get_text() for x in soup.find_all(class_="_2afbiS")]
total_reviews = (txts[1].strip().split(' ')[0])
total_reviews = int(total_reviews.replace(",", ""))
print(total_reviews)
page_limit = total_reviews//10 + 1
print(page_limit)

reviews = []

while(page_number < page_limit):
    page_number += 1
    review_page = website + '&page=' + str(page_number)
    result = requests.get(review_page)
    content = result.text

    soup = BeautifulSoup(content, 'html.parser')

    product_name = soup.find('div', class_='_2s4DIt').get_text()

    product_review = soup.find_all('div', {'class': 't-ZTKy'})
    
    for element in product_review:
        review = element.text.strip()
        reviews.append(review)

    with open(f'{product_name}.txt', 'w', encoding='utf-8') as file:
        file.write(product_name)
        file.write('\n')
        file.write('--------------------------------------------------------\n')
        file.write('\n\n'.join(reviews))