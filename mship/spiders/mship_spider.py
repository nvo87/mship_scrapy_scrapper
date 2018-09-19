import scrapy
from . import scraper_meta as meta
from ..items import Product

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
            product_snippets = response.css(meta.ProductsList.CSS.product_snippet)

            for product_snippet in product_snippets:
                yield self.parse_products_list(response, product_snippet)


    def parse_products_list(self, response, product_snippet):
        product = Product()
        name = product_snippet.css(meta.Product.CSS.name).extract_first()
        url = product_snippet.css(meta.Product.CSS.url).extract_first()
        product['name'] = name
        product['url'] = url
        return product