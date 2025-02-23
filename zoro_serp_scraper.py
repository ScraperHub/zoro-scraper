from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def scrape_zoro_listings(base_url, page_number):
    base_url = f"{base_url}&page={page_number}"
    options = {
        'ajax_wait': 'true',  # Ensure JavaScript content loads
        'page_wait': '5000',  # Wait 5 seconds for slow pages
    }
    response = crawling_api.get(base_url, options)

    if response['headers']['pc_status'] == '200':
        soup = BeautifulSoup(response['body'], 'html.parser')
        data = []

        products = soup.select('section[data-za="product-cards-list"] > div.search-product-card')
        for product in products:
            brand = product.select_one('span.brand-name').text.strip() if product.select_one('span.brand-name') else ''
            title = product.select_one('div.product-title').text.strip() if product.select_one('div.product-title') else ''
            price = product.select_one('div.price').text.strip() if product.select_one('div.price') else ''
            url = product.select_one('div.product-title a')['href'] if product.select_one('div.product-title a') else ''
            image_url = product.select_one('img[data-za="product-image"]')['src'] if product.select_one('img[data-za="product-image"]') else ''

            data.append({
                'brand': brand,
                'title': title,
                'price': price,
                'url': f"https://www.zoro.com{url}",
                'image_url': image_url
            })

        return data
    else:
        print(f"Failed to fetch page {page_number}. Status: {response['headers']['pc_status']}")
        return []

def scrape_all_pages(base_url, max_pages=None):
    all_data = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        page_data = scrape_zoro_listings(base_url, page)

        # Break the loop if no data is returned from the current page
        if not page_data:
            print("No more data found. Stopping pagination.")
            break

        all_data.extend(page_data)
        page += 1

        # Stop if the maximum page limit is reached
        if max_pages and page > max_pages:
            print(f"Reached the maximum limit of {max_pages} pages.")
            break

    return all_data

def save_to_json(data, filename='zoro_listings.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    base_url = 'https://www.zoro.com/search?q=tool+box'
    scraped_data = scrape_all_pages(base_url, 1)
    save_to_json(scraped_data)