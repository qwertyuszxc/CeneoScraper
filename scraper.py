import requests
from bs4 import BeautifulSoup

#product_code = input('Dodaj kod produktu: ')
product_code = '124124'
url = f'https://www.ceneo.pl/{product_code}#tab=reviews'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select('div.js_product-review')
all_opinions = []   
for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion['data-entry-id'],
        "author":  opinion.select_one('span.user-post__author-name').text.strip(),
        "recommendation":  opinion.select_one('spam.user-post__author-recommendation').text.strip(),
        "score":  opinion.select_one('span.user-post__score-count').text.strip(),
        "purchased":  opinion.select_one('div.review-pz').text.strip(),
        "published_at":  opinion.select_one('span.user-post__published > time:nth-child(1)')[ 'datetime'].strip(),
        "purchased_at":  opinion.select_one('span.user-post__published > time:nth-child(2)')[ 'datetime'].strip(),
        "thumbs_up":  opinion.select_one('button.vote-yes > span').text.strip(),
        "thumbs_down":  opinion.select_one('button.vote-no > span').text.strip(),
        "content":  opinion.select_one('div.user-post__text').text.strip(),
        "pros":  [pros.text.strip() for pros in opinion.select('div.review-feature__col:has(> div.review-feature__title-positives) > div.review-feature__item')],       
        "cons":  [cons.text.strip() for cons in opinion.select('div.review-feature__col:has(> div.review-feature__title-negatives) > div.review-feature__item')]
    }
    all_opinions.append(single_opinion)
Print(all_opinions)