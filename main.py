import requests
from bs4 import BeautifulSoup

result = []

page = requests.get('https://themeforest.net/category/site-templates/admin-templates?discounted_only=1')
soup = BeautifulSoup(page.text, 'html.parser')
repo = soup.find(class_="search-item_cards_container_component__list")
repo_list = repo.find_all(class_='shared-item_cards-card_component__root')

for repo in repo_list:
    name = repo.find(class_='shared-item_cards-item_name_component__itemNameLink').text
    url = repo.find(class_='shared-item_cards-item_name_component__itemNameLink', href=True)['href']
    livePreviewUrl = repo.find(class_='shared-item_cards-preview_button_with_analytics_component__root', href=True)['href']
    price = int(repo.find(class_='shared-item_cards-price_component__originalPrice').text[1:])
    promo = int(repo.find(class_='shared-item_cards-price_component__promoPrice').text[1:])
    percent = int(((price-promo) / price) * 100)
    item = {
        'name': name,
        'url': url,
        'live_preview': livePreviewUrl,
        'price': price,
        'promo': promo,
        'percent': percent
    }
    result.append(item)
print(result)