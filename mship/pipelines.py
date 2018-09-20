# -*- coding: utf-8 -*-
from .exporters import MshipCategoryExporter

class CsvPipeline(object):
    def __init__(self):
        self.file = open('categories.csv', 'wb')
        self.exporter = MshipCategoryExporter(self.file,
                                        encoding='utf-8',
                                        include_headers_line=True)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MshipPipeline(object):
    def process_item(self, item, spider):
        return item
