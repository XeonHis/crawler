import scrapy
from crawler.items import JobspidersItem


class JobsspiderSpider(scrapy.Spider):
    # global_count = 0

    name = 'jobsspider'
    start_urls = [
        # 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4%25E7%25BB%258F%25E7%2590%2586,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
        'https://www.indeed.com/jobs?q=web+developer',
        # 'https://www.indeed.com/jobs?q=Software+Enginee'
    ]

    # 51job start
    # def parse(self, response):
    #     selectors = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
    #
    #     for each in selectors:
    #         item_object = JobspidersItem()
    #         # 获取工作类别
    #         category = each.xpath('//input[@class="mytxt at"]/@value').get().strip()
    #         item_object['category'] = category
    #
    #         # 获取工作名称
    #         job_name = each.xpath('p[contains(@class,"t1 ")]/span/a/text()').get().strip()
    #         item_object['job_name'] = job_name
    #
    #         # 获取工作详细url
    #         job_detail_url = each.xpath('p[contains(@class,"t1 ")]/span/a/@href').get().strip()
    #         item_object['job_detail_url'] = job_detail_url
    #
    #         # 获取公司名称及url
    #         company_name = each.xpath('span[@class="t2"]/a/text()').get().strip()
    #         item_object['company_name'] = company_name
    #         company_detail_url = each.xpath('span[@class="t2"]/a/@href').get().strip()
    #         item_object['company_detail_url'] = company_detail_url
    #
    #         # 获取工作地点
    #         company_location = each.xpath('span[@class="t3"]/text()').get().strip()
    #         item_object['company_location'] = company_location
    #
    #         # 获取薪资
    #         wage = each.xpath('span[@class="t4"]/text()').get()
    #         if wage:
    #             wage = wage.strip()
    #         item_object['wage'] = wage
    #
    #         # 获取发布时间
    #         post_time = each.xpath('span[@class="t5"]/text()').get().strip()
    #         item_object['post_time'] = post_time
    #
    #         yield scrapy.Request(url=job_detail_url, meta={'item': item_object}, callback=self.parse_requirement,
    #                              encoding='utf-8')
    #         # yield item_object
    #
    #     # 获取下一页的地址
    #     next_page_url = response.xpath('//li[@class="bk"]/a/@href').extract()
    #     # print(next_page_url)
    #     if next_page_url:
    #         url = response.urljoin(next_page_url[-1])
    #         # 发送下一页请求并调用parse()函数继续解析
    #         yield scrapy.Request(url, self.parse, dont_filter=False)
    #         pass
    #     else:
    #         print("退出")

    # def parse_requirement(self, response):
    #     requirement_detail = ""
    #     item_object = response.meta['item']
    #     selectors = response.xpath('//div[contains(@class,"job_msg")]/p/text()').extract()
    #     for each in selectors:
    #         requirement_detail += each.strip()
    #         requirement_detail = ''.join(requirement_detail.split())
    #
    #     item_object['job_requirements'] = requirement_detail
    #
    #     yield item_object
    # 51job end

    # indeed start

    def parse(self, response):
        # self.global_count += 1
        print("\n", self.global_count, "\n")
        selectors = response.xpath('//div[contains(@class,"jobsearch-SerpJobCard unifiedRow")]')

        for each in selectors:
            item_object = JobspidersItem()

            # 获取工作类别
            category = response.xpath('//span[contains(@class,"inwrap") and @id="what_container"]/input/@value') \
                .get().strip()
            item_object['category'] = category

            # 获取工作名称
            job_name = each.xpath('div[@class="title"]/a/@title').get()
            if job_name:
                job_name = job_name.strip()
            item_object['job_name'] = job_name

            # 获取工作详细url
            job_detail_url = each.xpath('div[@class="title"]/a/@href').get().strip()
            job_detail_url = self.start_urls[0][0:int(self.start_urls[0].find('/', 10))] + job_detail_url
            item_object['job_detail_url'] = job_detail_url

            # 获取公司名称及url
            company_name = each.xpath('div[@class="sjcl"]/div/span/text()').get().strip()
            item_object['company_name'] = company_name

            # 获取工作地点
            company_location = each.xpath('div[@class="sjcl"]/*[contains(@class,"location")]/text()').get()
            if company_location:
                company_location = company_location.strip()
            item_object['company_location'] = company_location

            # 获取薪资
            wage = each.xpath(
                'div[@class="salarySnippet salarySnippetDemphasizeholisticSalary"]/span/span/text()').get()
            if wage:
                wage = wage.strip()
            item_object['wage'] = wage

            yield scrapy.Request(url=job_detail_url, meta={'item': item_object}, callback=self.parse_requirement,
                                 encoding='utf-8')
            # yield item_object

        # 获取下一页的地址
        next_page_url = response.xpath('//*[@id="resultsCol"]/div[@class="pagination"]/a[last()]/@href').extract()
        print(self.start_urls[0][0:int(self.start_urls[0].find('/', 10))] + next_page_url[-1])

        if next_page_url:
            url = self.start_urls[0][0:int(self.start_urls[0].find('/', 10))] + next_page_url[-1]
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            # pass
        else:
            print("退出")

    def parse_requirement(self, response):
        item_object = response.meta['item']

        # 获取发布时间
        post_time = response.xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[5]/div[2]/text()') \
            .get()
        if post_time:
            post_time = post_time.strip()[2:]
        item_object['post_time'] = post_time
        # print(post_time)

        requirement_detail = ''
        selectors = response.xpath('//div[@class="jobsearch-jobDescriptionText"]//text()').extract()
        for each in selectors:
            requirement_detail += each.strip()

        item_object['job_requirements'] = requirement_detail

        yield item_object
    # indeed end
