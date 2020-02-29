import pymysql
import datetime


class JobspidersPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect('106.14.169.0', 'testAdmin', '123456', 'X_test')
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
        self.cursor.execute('''insert into indeed (company_location,company_name,job_detail_url,job_name,
        post_time,wage,job_requirements,category,crawl_time,source_website) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                            (item['company_location'], item['company_name'],
                             item['job_detail_url'], item['job_name'], item['post_time'], item['wage'],
                             item['job_requirements'], item['category'],
                             datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'indeed'))
        # indeed sql operation stop

        self.connect.commit()
        return item
