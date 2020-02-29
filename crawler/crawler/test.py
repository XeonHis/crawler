start_urls = [
    # 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4%25E7%25BB%258F%25E7%2590%2586,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    'https://www.indeed.hk/jobs?q=web+developer&l='

]

print(start_urls[0][0:int(start_urls[0].find('/', 10))+1])
