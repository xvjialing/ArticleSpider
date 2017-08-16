# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112170/']

    def parse(self, response):
        title = response.xpath('//*[@id="post-112170"]/div[1]/h1/text()').extract()[0]
        # title = response.css('.entry-hearder h1::text').extract()[0]
        create_time=response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        praise_number=response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
        praise_number=response.css('.vote-post-up h10:text')
        fav_number=response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()
        match_re=re.match(".*(\d).*",fav_number)
        if match_re:
            fav_number=match_re.group(1)
        comment_number=response.xpath("//a[@href='#article-comment']/span/text()").extract()
        match_comment=re.match(".*(\d).*",comment_number)
        if match_comment:
            print(match_comment)
            comment_number=match_comment.group(1)

        content=response.xpath("//div[@class='entry']").extract()
        tag=response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()[0].strip().replace("·","").strip()


        pass
