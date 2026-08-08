# Audible Scrapy Scraper

[Portfolio](https://github.com/code-diver-pk/web-scraping-portfolio) • Business Email: lifenotsay@gmail.com

A professional Scrapy project that extracts audiobook product listings using a resilient crawler pipeline and adaptive request headers.

## Professional Overview

This repository shows how to build a production-grade Scrapy spider for ecommerce catalog scraping. It includes header rotation, checkpoint resume behavior, pagination, and cookie-enabled requests to scrape product data reliably.

## Business Problem Solved

Ecommerce research projects often need structured data from product search results. This Scrapy spider converts search pages into a dataset of titles, authors, and prices, which is useful for market research and competitor analysis.

## Features

- Scrapy-based spider architecture
- Randomized browser-like request headers
- Pagination through next page links
- Checkpoint resume support via `checkpoint.txt`
- Cookie-enabled requests
- Structured CSV/JSON export

## Technical Highlights

- `start_requests()` with saved checkpoint resume support
- Custom request headers for rotating user-agent values
- XPath selectors for item extraction
- Pagination detection and follow-through
- Scrapy best practices for scalable crawling

## Technologies

- Python 3
- Scrapy
- pandas (optional for local handling)

## Architecture

- `audible_scraper/spiders/audible_spider.py` — main spider implementation
- `audible_scraper/` — Scrapy project package
- `requirements.txt` — dependencies for crawling and data export

## How it Works

1. The spider starts from the search page.
2. It reads `checkpoint.txt` if present and resumes from the last page.
3. Custom headers are applied to mimic browser traffic.
4. Each product listing is parsed with XPath selectors.
5. The spider follows the next page link until the crawl ends.
6. Output can be exported to `audible_books.csv` or `audible_books.json`.

## Installation

```bash
git clone https://github.com/code-diver-pk/audible-scrapy-scraper.git
cd audible-scrapy-scraper
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
cd audible-scrapy-scraper
scrapy crawl audible -o audible_books.csv
```

## Sample Output

Output file: `audible_books.csv`
 
Columns:
- `title`
- `author`
- `price`

## What This Project Demonstrates

- Professional Scrapy architecture
- Pagination handling in a crawler
- Request header rotation
- Checkpoint resume support
- Structured data export
- Maintainable spider design

## Difficulty

**Advanced** — This project uses Scrapy crawler architecture and resume capabilities, which are essential for scalable production scraping.

## Real World Applications

- Ecommerce product research
- Competitive price monitoring
- Catalog aggregation for marketplaces
- Audiobook and digital product analytics

## Possible Client Use Cases

- Scrape product listings for competitor benchmarking
- Build market research datasets for digital content
- Collect product metadata for inventory analysis

## Future Improvements

- Add dedicated pipelines for CSV, JSON, and database exports
- Add smart retry/backoff logic for transient request failures
- Add rotating proxy support for larger ecommerce crawls
- Add structured metadata extraction for categories, ratings, and publishers

## Contact

- Portfolio: https://github.com/code-diver-pk/web-scraping-portfolio
- Business Email: lifenotsay@gmail.com

## License

MIT License
