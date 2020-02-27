import pymysql


class JobspidersPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect('106.14.169.0', 'testAdmin', '123456', 'X_test')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # print('职位:', item['job_name'])
        # print('职位url:', item['job_detail_url'])
        # print('公司:', item['company_name'])
        # print('公司url:', item['company_detail_url'])
        # print('工作地点:', item['company_location'])
        # print('薪资:', item['wage'])
        # print('发布时间:', item['post_time'])
        # print('职位要求:',item['job_requirement'])
        # print('----------------------------')

        self.cursor.execute('''insert into 51job (company_detail_url,company_location,company_name,job_detail_url,job_name,
        post_time,wage,job_requirements,category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                            (item['company_detail_url'], item['company_location'], item['company_name'],
                             item['job_detail_url'], item['job_name'], item['post_time'], item['wage'],
                             item['job_requirements'], item['category']))
        self.connect.commit()
        return item
