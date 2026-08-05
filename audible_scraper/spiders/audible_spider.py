import random
import os
import scrapy

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
]


class AudibleSpider(scrapy.Spider):
    name = "audible"
    start_urls = ["https://www.audible.com/search"]

    custom_settings = {
        "DOWNLOAD_DELAY": 4,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 3,
        "AUTOTHROTTLE_MAX_DELAY": 15,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1.0,
        "CONCURRENT_REQUESTS": 1,
        "COOKIES_ENABLED": True,
    }

    def get_headers(self):
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
        }

    def start_requests(self):
        checkpoint_path = "checkpoint.txt"
        if os.path.exists(checkpoint_path):
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                url = f.read().strip()
        else:
            url = self.start_urls[0]

        yield scrapy.Request(url=url, headers=self.get_headers(), callback=self.parse)

    def parse(self, response):
        books = response.xpath(
            '(//ul[contains(@class,"bc-list")])[11]/li[contains(@class,"productListItem")]'
        )

        self.logger.info(f"Books found: {len(books)}")

        for book in books:
            title = book.xpath('.//h3[contains(@class,"bc-heading")]/a/text()').get(default="").strip()
            author = [
                a.strip()
                for a in book.xpath('.//li[contains(@class,"authorLabel")]/span/a/text()').getall()
                if a.strip()
            ]
            price = book.xpath('.//p[contains(@class,"buybox-regular-price")]/span[1]/text()').get(default="").strip()

            if not title:
                continue

            yield {
                "title": title,
                "author": author,
                "price": price,
            }

        next_page = response.xpath('//span[contains(@class,"nextButton")]/a/@href').get()
        disabled = response.xpath('//span[contains(@class,"nextButton")]/a/@aria-disabled').get()

        if next_page and disabled is None:
            next_url = response.urljoin(next_page)
            with open("checkpoint.txt", "w", encoding="utf-8") as f:
                f.write(next_url)

            yield scrapy.Request(
                url=next_url,
                headers=self.get_headers(),
                callback=self.parse,
            )
