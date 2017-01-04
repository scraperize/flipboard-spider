# -*- coding: utf-8 -*-
import scrapy

class FlipboardSpider(scrapy.Spider):

    name = "flipboard"
    allowed_domains = ["flipboard.com"]

    def __init__(self, *args, **kwargs):

        board = kwargs.get('board')
        if (not board):
            exit('You must specify board URL : -a board="@username/board"')

        super(FlipboardSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://flipboard.com/" + board]

    def parse(self, response):

        for item in response.css("#main > .item"):

            yield {
                'title': str(item.css("h3 a ::text").extract_first().encode('utf-8')),
                'description': str(item.css("p ::text").extract_first().encode('utf-8')),
                'link': str(item.css("h3 a ::attr(href)").extract_first()),
                'category': str(item.css("a.topic ::text").extract_first().encode('utf-8')),
            }
