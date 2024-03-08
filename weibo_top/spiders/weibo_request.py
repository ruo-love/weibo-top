import scrapy
import re

from weibo_top.items import WeiboTopItem

class QuotesSpider(scrapy.Spider):
    name = "weibo_top"
    allowed_domains = ['s.weibo.com']
    def start_requests(self):
        yield scrapy.Request(url="https://s.weibo.com/top/summary?cate=realtimehot")

    def parse(self, response, **kwargs):
        trs = response.css('#pl_top_realtimehot > table > tbody > tr')
        count = 0
        for tr in trs:
            if count >= 30:  # 获取前3条数据
                break  # 停止处理后续数据
            item = WeiboTopItem()
            title = tr.css('.td-02 a::text').get()
            link = 'https://s.weibo.com/' + tr.css('.td-02 a::attr(href)').get()
            item['title'] = title
            item['link'] = link
            if link:
                count += 1  # 增加计数器
                yield scrapy.Request(url=link, callback=self.parse_detail, meta={'item': item})
            else:
                yield item

    def parse_detail(self, response, **kwargs):

        item = response.meta['item']
        list_items = response.css('div.card-wrap[action-type="feed_list_item"]')
        limit = 0
        for li in list_items:
            if limit >= 1:
                break  # 停止处理后续数据
            else:
                content = li.xpath('.//p[@class="txt"]/text()').getall()
                processed_content = [re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9【】,]', '', text) for text in content]
                processed_content = [text.strip() for text in processed_content if text.strip()]
                processed_content = ','.join(processed_content).replace('【,','【')
                item['desc'] = processed_content
                print(processed_content)
                yield item
                limit += 1  # 增加计数器
