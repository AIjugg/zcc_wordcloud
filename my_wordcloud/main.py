import my_wordcloud
import my_spider

def main():
    # 输入boss直聘中相应岗位的url
    job_url = "https://www.zhipin.com/c101210100/?query=Java&industry=&position=&ka=hot-position-1"
    # 输入记录的txt文件名
    txt_file = "job_java.txt"
    my_spider.create_record(job_url,txt_file)
    # 生成词云图
    bg_file = 'bg_java.png'
    wc_file = 'job_java.png'
    my_wordcloud.create_wordcloud(txt_file,bg_file,wc_file)
    
if __name__ == '__main__':
    main()