# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
import json
from scrapy import Selector

# from datetime import datetime
# start_time = datetime.now()

filpcart = 'https://www.flipkart.com'


class ShoesSpider(scrapy.Spider):
    all_urls = []
    name = 'shoes_fully_scrapy'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&page=1',
        # 'https://www.flipkart.com/mens-footwear/casual-shoes/pr?sid=osp%2Ccil%2Ce1f&otracker=nmenu_sub_Men_0_Casual+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove',
    ]

    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        try:
            crawled_urls = response.css('._2mylT6 ::attr("href")').extract()
            self.all_urls = self.all_urls + crawled_urls

            # yield response.follow(filpcart + str(crawled_urls[50]), callback=self.parse_items)
            # i = 0
            for item_url in crawled_urls:
                yield response.follow(filpcart + str(item_url), callback=self.parse_items)
                # if i >= 5:
                #     break
                # i += 1
        except Exception as e:
            pass

        try:
            next_page = response.css('._3fVaIS ::attr("href")').extract()[-1]
            # print("===============================", next_page)
            if next_page is not None:
                next_page = filpcart + str(next_page)
                # print("===============================", next_page)
                yield scrapy.Request(next_page)

            print("======================================================", len(self.all_urls))
        except Exception as e:
            pass

    def parse_items(self, response):
        try:
            title = response.css('._35KyD6 ::text').extract_first()
            mother_url = response.request.url

            # all_urls_colors_size = response.css('._2UBURg a ::attr("href")').extract()
            #
            # print(len(all_urls_colors_size))
            # for i in all_urls_colors_size:
            #     print(filpcart+str(i))

            color_size_component = response.css('.fUBI-_').extract()
            if len(color_size_component) == 2:
                color_comp = response.css('.fUBI-_')[0]
                color_urls = color_comp.css('._2UBURg a ::attr("href")').extract()

                # print(len(color_urls))
                for color_url in color_urls:
                    yield response.follow(filpcart + str(color_url), callback=self.parse_size_urls, meta={'title': title, 'mother_url': mother_url})
            if len(color_size_component) == 1:
                print("from size only")
                size_comp = response.css('.fUBI-_')
                size_urls = size_comp.css('._2UBURg a ::attr("href")').extract()

                # print(len(size_urls))
                for size_url in size_urls:
                    # print("so:", filpcart + str(size_url))
                    yield response.follow(filpcart + str(size_url), callback=self.parse_variations, meta={'title': title, 'mother_url': mother_url})
            else:
                pass
        except Exception as e:
            pass

    def parse_size_urls(self, response):
        try:
            mother_url = response.meta['mother_url']
            title = response.meta['title']

            size_comp = response.css('.fUBI-_')[1]
            size_urls = size_comp.css('._2UBURg a ::attr("href")').extract()

            print(len(size_urls))
            for size_url in size_urls:
                # print("csb:", filpcart+str(size_url))
                yield response.follow(filpcart + str(size_url), callback=self.parse_variations, meta={'title': title, 'mother_url': mother_url})
        except Exception as e:
            pass

    def parse_variations(self, response):
        try:
            if not response.css('._9-sL7L'):
                mother_url = response.meta['mother_url']
                variations_url = response.request.url
                variations_title = response.css('._35KyD6 ::text').extract_first()
                variations_brand = response.css('._2J4LW6 ::text').extract_first()
                if response.css('._3qQ9m1 ::text').extract_first()[1:]:
                    variations_discounted_price = response.css('._3qQ9m1 ::text').extract_first()[1:]
                variations_stock_price = response.css('._1POkHg ::text').extract()[1]
                variations_color_size = response.css('._3c2Xi9').extract()
                if len(variations_color_size) == 2:
                # if response.xpath('//a[contains(@class, "_3c2Xi9")]/following-sibling::div/div/text()').extract_first():
                    variations_color = response.xpath('//a[contains(@class, "_3c2Xi9")]/following-sibling::div/div/text()').extract_first()
                variations_size = response.css('._3c2Xi9 ::text').extract_first()
                images_tiny = response.xpath("//div[contains(@class, '_2_AcLJ')]//@style").re(r'url\((.*)\)')
                images = [str(image).replace('128/128/', '') for image in images_tiny]

                variations = {
                    'mother_url': mother_url,
                    'variations_url': variations_url,
                    'variations_title': variations_title,
                    'variations_brand': variations_brand,
                    'variations_discounted_price': variations_discounted_price,
                    'variations_stock_price': variations_stock_price,
                    'variations_color': variations_color,
                    'variations_size': variations_size,
                    'images': images
                }

                yield variations
            else:
                pass
        except Exception as e:
            pass


# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))




