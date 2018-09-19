class Product:
    class CSS:
        name = 'a.product-name::text'
        url = 'a[itemprop="url"]::attr(href)'
        title = 'title::text'

class ProductsList:
    class CSS:
        product_snippet = 'div.product-container'