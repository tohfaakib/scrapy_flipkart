# -*- coding: utf-8 -*-
import json

import scrapy
from bs4 import BeautifulSoup
import requests

from flipcart_juta.utils.fetch import get_shoe_variant_json_data, get_shoe_template_json_date

filpcart = 'https://www.flipkart.com'

write_file = open("products.json", "w+")
log_file = open("log.txt", "w+")

class ShoesSpider(scrapy.Spider):
    all_urls = []
    name = 'shoes_test'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&page=1',
        # 'https://www.flipkart.com/mens-footwear/casual-shoes/pr?sid=osp%2Ccil%2Ce1f&otracker=nmenu_sub_Men_0_Casual+Shoes&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove',
    ]

    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        crawled_urls = response.css('._2mylT6 ::attr("href")').extract()
        self.all_urls = self.all_urls + crawled_urls

        # yield response.follow(filpcart + str(crawled_urls[50]), callback=self.parse_items)
        i = 0
        for item_url in crawled_urls:
            yield response.follow(filpcart + str(item_url), callback=self.parse_items)
            if i >= 5:
                break
            i += 1

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
        global product
        total_products = []
        all_products = []
       
        title = response.css('._35KyD6 ::text').extract_first()
        # print("from parse items:", response.request.url)
        product_parent_url = response.request.url
        # print(title)

        # all_urls_colors_size = response.css('._2UBURg a ::attr("href")').extract()
        #
        # print(len(all_urls_colors_size))
        # for i in all_urls_colors_size:
        #     print(filpcart+str(i))
        product_variants_list = []
        color_size_component = response.css('.fUBI-_').extract()
        if len(color_size_component) == 2:
            color_comp = response.css('.fUBI-_')[0]
            color_urls = color_comp.css('._2UBURg a ::attr("href")').extract()

            # print(len(color_urls))
            for color_url in color_urls:
                try:
                    color_url_a = filpcart + str(color_url)
                    # print("Debuggggg", color_url_a)
                    res = requests.get(color_url_a)
                    # print(res.status_code)
                    soup = BeautifulSoup(res.content, 'html.parser')
                    size_comp = soup.find_all("ul", {"class": "fUBI-_"})[1]
                    size_urls = size_comp.find_all("a", {"class": "_2UBURg"})

                        # css('._2UBURg a ::attr("href")').extract()

                    # res =
                    # size_comp = res.css('.fUBI-_')[1]
                    # size_urls = size_comp.css('._2UBURg a ::attr("href")').extract()
                    #
                    print(len(size_urls))
                    for size_url in size_urls:
                        product_variants_list.append(get_shoe_variant_json_data(filpcart + str(size_url['href'])))

                        # print("csb:", filpcart+str(size_url['href']))
                except Exception as e:
                    pass
            product = get_shoe_template_json_date(title,product_parent_url,product_variants_list)
            total_products.append(product)
            
                # print(filpcart+str(color_url))
                # yield response.follow(filpcart + str(color_url), callback=self.parse_size_urls, meta={'title': title, 'mother_url': mother_url})
        if len(color_size_component) == 1:
            print("from size only")
            size_comp = response.css('.fUBI-_')
            size_urls = size_comp.css('._2UBURg a ::attr("href")').extract()

            print(len(size_urls))
            for size_url in size_urls:
                product_variants_list.append(get_shoe_variant_json_data(filpcart + str(size_url['href'])))
                # print(json.dumps(get_shoe_variant_json_data(filpcart + str(size_url['href'])), indent=4, sort_keys=True))
                # print("shoe:", filpcart + str(size_url))
            product = get_shoe_template_json_date(title, product_parent_url, product_variants_list)
            total_products.append(product)
        else:
            pass
            
        # print(json.dumps(total_products, indent=4, sort_keys=True))
        json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    # def parse_size_urls(self, response):
    #     mother_url = response.meta['mother_url']
    #     title = response.meta['title']
    #
    #     size_comp = response.css('.fUBI-_')[1]
    #     size_urls = size_comp.css('._2UBURg a ::attr("href")').extract()
    #
    #     print(len(size_urls))
    #     for size_url in size_urls:
    #         print("csb:", filpcart+str(size_url))
