# zoro-scraper

## Description

This repository contains Python-based scrapers for extracting product data from Zoro.com. These scrapers utilize the Crawlbase Crawling API to bypass JavaScript rendering, CAPTCHA challenges, and anti-bot protections, enabling seamless data extraction.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-zoro-website-data/) to learn more.

## Scrapers Overview

### Zoro Search Results Scraper

The Zoro Search Results Scraper (`zoro_serp_scraper.py`) extracts product details from Zoro's search listings, including:

1. **Product Title**
2. **Price**
3. **Brand**
4. **Product URL**
5. **Thumbnail Image**

It supports pagination, ensuring that multiple pages of search results can be scraped efficiently. Extracted data is stored in a structured JSON file.

### Zoro Product Page Scraper

The Zoro Product Page Scraper (`zoro_product_page_scraper.py`) extracts detailed product information from individual product pages, including:

1. **Product Title**
2. **Price**
3. **Product Description**
4. **Specifications**
5. **Product Images**

This scraper takes product URLs from the search listings scraper and extracts in-depth details, saving the data in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux/macOS
python --version
```

Install the required dependencies:

```bash
pip install crawlbase beautifulsoup4 pandas
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.
- **Pandas** – Formats and stores extracted data for easy analysis.

## Running the Scrapers

### 1. Get Your Crawlbase Access Token

- Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
- Use the JS token for Zoro scraping, as the site relies on JavaScript-rendered content.

### 2. Run the Search Listings Scraper

This scraper extracts product details from search listings and saves them in `zoro_search_data.json`:

```bash
# Use python3 if required (for Linux/macOS)
python zoro_serp_scraper.py
```

### 3. Run the Product Page Scraper

Once you have the search results, extract detailed product information using:

```bash
python zoro_product_page_scraper.py
```

This will fetch and save product details in `zoro_product_data.json`.

## To-Do List

- Extend scrapers to extract additional details like customer reviews and seller information.
- Improve scraping efficiency with multi-threading.
- Add support for structured data exports (CSV, JSON, database integration).

## Why Use This Scraper?

- **Bypasses anti-bot protections** using Crawlbase.
- **Handles JavaScript-rendered content** efficiently.
- **Extracts structured product data** for e-commerce insights.
