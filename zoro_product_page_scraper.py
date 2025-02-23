from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json
import re

crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def scrape_product_page(product_url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000',
    }
    response = crawling_api.get(product_url, options)

    if response['headers']['pc_status'] == '200':
        soup = BeautifulSoup(response['body'], 'html.parser')

        title = {re.sub(r'\s+', ' ', soup.select_one('h1[data-za="product-name"]').text.strip())} if soup.select_one('h1[data-za="product-name"]') else ''
        price = soup.select_one('div[data-za="product-price"] span.currency').text.strip() if soup.select_one('div[data-za="product-price"]  span.currency') else ''
        description = re.sub(r'\s+', ' ', soup.select_one('div.product-description div.description-text').text.strip()) if soup.select_one('div.product-description div.description-text') else ''
        specifications = {re.sub(r'\s+', ' ', row.find_all('td')[0].text.strip()): re.sub(r'\s+', ' ',row.find_all('td')[1].text.strip()) for row in soup.select('div.product-details-info table tr') if len(row.find_all('td')) == 2}
        image_urls = [img['src'] for img in soup.select('div.product-images img.product-image') if 'src' in img.attrs]

        return {
            'title': title,
            'price': price,
            'description': description,
            'specifications': specifications,
            'image_urls': image_urls,
            'url': product_url
        }
    else:
        print(f"Failed to fetch product page: {product_url}. Status: {response['headers']['pc_status']}")
        return {}

def save_product_data(data, filename='zoro_products.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Product data saved to {filename}")

if __name__ == "__main__":
    product_urls = [
        "https://www.zoro.com/apex-tool-group-3-drawer-tool-box-83151/i/G6893443/",
        "https://www.zoro.com/k-tool-international-tool-box-10-drawer-black-41-in-w-kti75132/i/G406006122/",
        "https://www.zoro.com/proto-general-purpose-double-latch-tool-box-with-tray-steel-red-20-w-x-85-d-x-95-h-j9975r/i/G0067825/"
    ]

    all_product_data = []
    for url in product_urls:
        print(f"Scraping product: {url}")
        product_data = scrape_product_page(url)
        if product_data:
            all_product_data.append(product_data)

    save_product_data(all_product_data)