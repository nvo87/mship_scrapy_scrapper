class Product:
    class CSS:
        name = 'a.product-name::text'
        url = 'a[itemprop="url"]::attr(href)'
        title = 'title::text'


class ProductsList:
    class CSS:
        product_snippet = 'div.product-container'

class ProductData:
    class CSS:
        name_h1 = 'h1[itemprop="name"]::text'
        title = 'title::text'


class Category:
    class CSS:
        url = 'a::attr(href)'
        name = 'a::text'


class CategoriesList:
    class CSS:
        snippet = '#categories_block_left li'