import pymysql
import datetime


class JobspidersPipeline(object):
    def __init__(self):
        # 职位数据爬虫 start
        # self.connect = pymysql.connect('106.14.169.0', 'testAdmin', '123456', 'X_test')
        # 职位数据爬虫 end

        # simplyhired start
        # todo: simplyhired database connection
        self.connect = pymysql.connect('106.14.169.0', 'testAdmin', '123456', 'X_test')
        # simplyhired end
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 51job sql operation start
        # self.cursor.execute('''insert into 51job (company_detail_url,company_location,company_name,job_detail_url,job_name,
        # post_time,wage,job_requirements,category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
        #                     (item['company_detail_url'], item['company_location'], item['company_name'],
        #                      item['job_detail_url'], item['job_name'], item['post_time'], item['wage'],
        #                      item['job_requirements'], item['category']))
        # 51job sql operation end

        # indeed sql operation start
        # self.cursor.execute('''insert into indeed (company_location,company_name,job_detail_url,job_name,
        # post_time,wage,job_requirements,category,crawl_time,source_website) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
        #                     (item['company_location'], item['company_name'],
        #                      item['job_detail_url'], item['job_name'], item['post_time'], item['wage'],
        #                      item['job_requirements'], item['category'],
        #                      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'indeed'))
        # indeed sql operation end

        # simplyhired sql operation start
        # todo: simplyhired sql statement
        self.cursor.execute('''insert into simplyhired (job_name, job_detail_url, company_location, wage, post_time,
        key_words, category) values (%s, %s, %s, %s, %s, %s, %s)''', (item['job_name'], item['job_detail_url'],
                                                                      item['company_location'], item['wage'],
                                                                      item['post_time'], item['key_words'],
                                                                      item['category']))
        # simplyhired sql operation end

        self.connect.commit()
        return item
