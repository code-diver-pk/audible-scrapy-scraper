# Audible Scrapy Scraper

A professional Scrapy project that extracts Audible-style product information using a resilient crawler architecture.

## Features

- Scrapy-based spider architecture
- Randomized browser-like request headers
- Pagination handling
- Checkpoint resume support
- Cookie-enabled requests
- Structured JSON/CSV export

## Technologies Used

- Python 3
- Scrapy
- Pandas (optional for local data processing)

## Project Structure

- `audible_scraper/` — Scrapy project package
- `audible_scraper/spiders/audible_spider.py` — main spider
- `requirements.txt` — project dependencies
- `.gitignore` — ignored files and folders
- `screenshots/` — placeholder for screenshots
- `sample_output/` — placeholder for example output

## Installation

Clone the repository and install dependencies.

## Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
cd audible-scrapy-scraper
scrapy crawl audible -o audible_books.csv
```

## Example Output

The project can write scraped book data to `audible_books.csv`.

## Learning Outcomes

- Building a maintainable Scrapy project
- Managing request headers and cookies
- Implementing pagination in Scrapy
- Adding checkpoint-based crawl resume behavior
- Writing professional spider code

## Future Improvements

- Add item pipelines for storage
- Add automated testing for XPath selectors
- Add logging enhancements and metrics
- Add Playwright support for JavaScript pages

## License

MIT License
