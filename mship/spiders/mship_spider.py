import scrapy
from pandas import read_csv

from . import scraper_meta as meta
from ..items import Product, Category


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ['mship.no']

    def start_requests(self):
        urls = [
            'https://mship.no/22-engines-equipment',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # handle if blocked by distil networks
        if response.status == 405:
            req_url = response.meta.get('redirect_urls', [response.url])[0]
            self.logger.warning(
                'parse: wrong response status {}. Sleep 3 sec and retry open {}'.format(
                    response.status,
                    req_url
                )
            )
            time.sleep(3)
            yield scrapy.Request(req_url, callback=self.parse, dont_filter=True)
        else:
            products_snippets = response.css(meta.ProductsList.CSS.product_snippet)

            for product_snippet in products_snippets:
                yield self.parse_product(response, product_snippet)

    def parse_product(self, response, product_snippet):
        product = Product()
        product['name'] = product_snippet.css(meta.Product.CSS.name).extract_first()
        product['url'] = product_snippet.css(meta.Product.CSS.url).extract_first()
        return product


class CategorySpider(scrapy.Spider):
    name = "category"

    allowed_domains = ['mship.no']
    start_urls = [
        'https://mship.no/22-engines-equipment',
        'https://mship.no/23-spare-parts'
    ]

    # TODO сделать рекурсивный обход каждой категории.
    # Сейчас все категории получаем просто из вложенного списка на главной.

    def parse(self, response):
        categories_snippets = response.css(meta.CategoriesList.CSS.snippet)
        for category_snippet in categories_snippets:
            yield self.parse_category(response, category_snippet)

    def parse_category(self, response, category_snippet):
        category = Category()
        category['name'] = category_snippet.css(meta.Category.CSS.name).extract_first().strip()
        category['url'] = category_snippet.css(meta.Category.CSS.url).extract_first()
        return category