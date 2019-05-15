# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import urllib.request

job_url_list = []

def domain_split(url):
    url_array = url.strip().split('/')
    if url[:4] == "http":
        domain = url_array[0] + "//" + url_array[2]
    else:
        domain = url_array[0]
    return domain

def get_main_msg(domain,my_url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=my_url,headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")  #html.parser表示解析使用的解析器
    job_list = soup.body.find('div',attrs={'class':'job-list'})
    jobs = job_list.ul.find_all('li')
    for job in jobs:
        job_detail = job.div.find('div',attrs={'class':'info-primary'})
        job_detail_url = domain + job_detail.h3.a["href"]
        print(job_detail_url)
        job_url_list.append(job_detail_url)
    return next_page(domain,soup)
   
#get next page
def next_page(domain,soup):
    nodes = soup.body.find('div',attrs={'class':'page'})
    next_a = nodes.find('a',attrs={'class':'next'})
    next = next_a["href"]
    #print(next)
    next_url = domain + next
    return next_url
   
def get_job_detail(job_detail_url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=job_detail_url,headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")
    #print(soup)
    main = soup.body.div.find('div',attrs={'id':'main'})
    job = main.find('div',attrs={'class':'job-box'})
    job_detail = job.find('div',attrs={'class':'job-detail'})
    detail_content = job_detail.find('div',attrs={'class':'detail-content'})
    job_sec = detail_content.find('div',attrs={'class':'job-sec'})
    job_detail_content = job_sec.div
    #print(job_detail_content.text)
    return job_detail_content.text
    
def create_record(job_url,txt_file):
    txt_file = "text/" + txt_file
    domain = domain_split(job_url)
    # 这里我只爬取了三页的招聘信息，可以根据自己需求更改
    for i in range(3):
        job_url = get_main_msg(domain,job_url)
    with open(txt_file,'w',encoding='utf-8') as f:
        for job_detail_url in job_url_list:
            try:
                job_detail_content = get_job_detail(job_detail_url)
                f.write(job_detail_content)
                print(job_detail_url+":successful!")
            except Exception as e:
                print(e)
                break

'''
if __name__ == '__main__':
    # 输入boss直聘中相应岗位的url
    job_url = "https://www.zhipin.com/c101210100/?query=Java&industry=&position=&ka=hot-position-1"
    # 输入记录的txt文件名
    txt_file = "job_java.txt"
    create_record(job_url,txt_file)
'''