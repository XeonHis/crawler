class JobspidersPipeline(object):
    def process_item(self, item, spider):
        # dbu = dbutil.MYSQLdbUtil()
        # dbu.getConnection()  # 开启事物
        #
        # # 1.添加
        # try:
        #     # sql = "insert into jobs (职位名,公司名,工作地点,薪资,发布时间)values(%s,%s,%s,%s,%s)"
        #     sql = "insert into t_job (jobname,jobcompany,jobarea,jobsale,jobdata)values(%s,%s,%s,%s,%s)"
        #     # date = []
        #     # dbu.execute(sql, date, True)
        #     dbu.execute(sql,
        #                 (item['jobPosition'], item['jobCompany'], item['jobArea'], item['jobSale'], item['jobDate']),
        #                 True)
        #     # dbu.execute(sql,True)
        #     dbu.commit()
        #     print('插入数据库成功！！')
        # except:
        #     dbu.rollback()
        #     dbu.commit()  # 回滚后要提交
        # finally:
        #     dbu.close()
        # return item
        print(item)
