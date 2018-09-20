from scrapy.exporters import CsvItemExporter

class MshipCategoryExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        super(MshipCategoryExporter, self).__init__(*args, **kwargs)

    # TODO потренероваться здесь, дописав методы например для
    # создания первой линии курсивом
    # создания пустой строки между новой группой урлов и т.д.
