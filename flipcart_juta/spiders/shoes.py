# -*- coding: utf-8 -*-
import scrapy

filpcart = 'https://www.flipkart.com'

class ShoesSpider(scrapy.Spider):
    all_urls = []
    name = 'shoes'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&page=1',
        # 'https://www.flipkart.com/mens-footwear/casual-shoes/pr?sid=osp%2Ccil%2Ce1f&otracker=nmenu_sub_Men_0_Casual+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove',
    ]

    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        crawled_urls = response.css('._2mylT6 ::attr("href")').extract()
        self.all_urls = self.all_urls + crawled_urls

        for item_url in crawled_urls:
            yield response.follow(filpcart + str(item_url), callback=self.parse_items)

        # try:
        #     next_page = response.css('._3fVaIS ::attr("href")').extract()[-1]
        #     print("===============================", next_page)
        #     if next_page is not None:
        #         next_page = filpcart + str(next_page)
        #         print("===============================", next_page)
        #         yield scrapy.Request(next_page)
        #
        #     print("======================================================", len(self.all_urls))
        # except Exception as e:
        #     pass

    def parse_items(self, response):
        title = response.css('._35KyD6 ::text').extract_first()
        # print("from parse items:", response.request.url)
        mother_url = response.request.url
        # print(title)
        color_size_component = response.css('.fUBI-_').extract()
        if len(color_size_component) == 2:
            color_urls = response.css('.fUBI-_ li ::attr("href")').extract()
            # print("color urls:", color_urls)
            for color_url in color_urls:
                yield response.follow(filpcart + str(color_url), callback=self.parse_size_urls, meta={'title': title, 'mother_url': mother_url})
        elif len(color_size_component) == 1:
            # size_urls = response.css('.fUBI-_ li ::attr("href")').extract()[-1]
            # for size_url in size_urls:
            #     yield response.follow(filpcart + str(size_url), callback=self.parse_variations, meta={'title': title, 'mother_url': mother_url})
            pass
        else:
            pass

    def parse_size_urls(self, response):
        mother_url = response.meta['mother_url']
        title = response.meta['title']
        size_urls = response.css('.fUBI-_ li ::attr("href")').extract()[1]
        print('############################', size_urls)
        # print(filpcart + str(size_urls))
        # for size_url in size_urls:
        #     print('################',filpcart + str(size_url))
            # yield response.follow(filpcart + str(size_url), callback=self.parse_variations, meta={'title': title, 'mother_url': mother_url})
            # res = scrapy.Request(filpcart + str(size_url))
            # print(res)


    def parse_variations(self, response):
        pass