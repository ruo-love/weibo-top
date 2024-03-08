# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeiboTopPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        # 将item添加到列表中
        self.items.append(item)
        print('\n\nitem',item)
        return item

    def close_spider(self, spider):
        # 打开文件，将所有items写入文件
        with open('weibo_top_data.txt', 'w', encoding='utf-8') as file:
            for item in self.items:
                title = item.get('title', '')
                desc = item.get('desc', '')
                output_string = f'{title}\n{desc}\n\n'
                file.write(output_string)