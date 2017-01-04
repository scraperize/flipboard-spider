# -*- coding: utf-8 -*-
import PyRSS2Gen
import datetime
import re
import cgi

class FlipboardPipeline(object):

    rss_items = []

    def close_spider(self, spider):

        rss = PyRSS2Gen.RSS2(
            title="Flipboard RSS feed",
            link=spider.start_urls[0],
            description="Flipboard RSS feed",
            lastBuildDate=datetime.datetime.utcnow(),
            items=self.rss_items,
            language="en"
        )

        output_file = re.sub(r"^.+@(.+)/(.+)$", r"\1-\2", spider.start_urls[0])
        rss.write_xml(open("output/" + output_file + ".xml", "w"), "utf-8")

    def process_item(self, item, spider):

        self.rss_items.append(PyRSS2Gen.RSSItem(
            title=cgi.escape(item['title']),
            link=item['link'],
            description=cgi.escape(item['description']),
            guid=PyRSS2Gen.Guid(item['link']),
            pubDate=datetime.datetime.utcnow(),
            categories=[cgi.escape(item['category'])]
        ))

        return item
