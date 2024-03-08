# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class WeiboTopSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class WeiboTopDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        self.cookie_string = "SUB=_2AkMS10-nf8NxqwFRmfoXyG3jaoxxygHEieKki758JRMxHRl-yT9vqhIrtRB6OVdhSYUGwRsrtuQyFPy_aLfaay7wguyu; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhBJpfihr9Mo_TDhk.fIHFo; _s_tentry=www.baidu.com; UOR=www.baidu.com,s.weibo.com,www.baidu.com; Apache=5259811159487.941.1709629772294; SINAGLOBAL=5259811159487.941.1709629772294; ULV=1709629772313:1:1:1:5259811159487.941.1709629772294:"
        # self.referer = "https://sh.ke.com/chengjiao/"

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        cookie_dict = self.get_cookie()
        request.cookies = cookie_dict
        request.headers['User-Agent'] = UserAgent().random
        request.headers['Host'] = 's.weibo.com'
        # request.headers["referer"] = self.referer
        return None

    def get_cookie(self):
        cookie_dict = {}
        for kv in self.cookie_string.split(";"):
            k = kv.split('=')[0]
            v = kv.split('=')[1]
            cookie_dict[k] = v
        return cookie_dict

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
