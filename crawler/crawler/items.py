import scrapy


class JobspidersItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_detail_url = scrapy.Field()
    company_name = scrapy.Field()
    company_detail_url = scrapy.Field()
    company_location = scrapy.Field()
    wage = scrapy.Field()
    post_time = scrapy.Field()
    job_requirements = scrapy.Field()
    category = scrapy.Field()
    key_word = scrapy.Field()
    pass
