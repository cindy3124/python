# -*- coding: utf-8 -*-

import time
import random
import logging


# 二、测试工作相关作业
# 1.通过当前时间和函数名生成测试报告名称，随机字符串（大小写字母和数字）生成测试数据
def test_report_name():
    now_time = time.strftime('%Y%m%d %H%M%S', time.localtime())
    report_name = now_time+'_TestReport.xml'
    return report_name


def test_data():
    data = ''
    for i in range(100):
        data += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:,.!')
    return data


def save_file(filename, test_data):
    with open('resource/'+filename, 'w') as f:
        f.write(test_data)
        f.close()


save_file(test_report_name(), test_data())

# 2.使用logger设置日志，将日志保存到文件。
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
now_time = time.strftime('%Y%m%d %H%M%S', time.localtime())
handler = logging.FileHandler("resource/"+now_time+"_log.txt")
formatter = logging.Formatter('[%(asctime)s][%(levelname)s]:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print report")
logger.debug("Do something")
logger.warning("Something maybe fail")
logger.info("Finish")

# 3.查找/tomcat/report/ 目录下的log文件，如果文件最后修改时间是在1小时之前
#   把次文件打包压缩，备份到/home/back/report 目录下
import os
import datetime
import tarfile


def get_file(path):
    file_list = []
    for file in os.walk(path):
        for filename in file[2]:
         if 'report' in filename:
            mtime = os.stat(path+filename).st_mtime
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
            d1 = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            d2 = datetime.datetime.now()
            xc = d2-d1
            print(xc)
            hour = str(xc).split(':')[0]
            if xc.days < 1 and int(hour) > 0:
                file_list.append(filename)
            else:
                continue
    return file_list


def create_tarfile(path, filename_list, save_path):
    now_time = time.strftime('%Y%m%d %H%M%S', time.localtime())
    with tarfile.open(save_path+now_time+".tar.gz", "w:gz") as tar:
        for filename in filename_list:
            tar.add(path+filename)
    tar.close()


path = '/scipt/python/testerhome_pratice/resource/'
filename_list = get_file(path)
save_path = '/scipt/python/testerhome_pratice/resource/'
create_tarfile(path, filename_list, save_path)


# 4.在Linux下每隔1分钟检查一下tomcat进程是不是在运行，如果tomcat进程退出了，立即启动tomcat进程
import os
import time


def detect_process(process, start_command):
    while True:
        rets = os.popen('ps -ef| grep '+process+' | grep -v grep').readlines()
        if rets:
            for ret in rets:
                if process in ret:
                    print("程序运行正常")
                else:
                    print("程序运行异常，需重启")
                    os.system(start_command)
        else:
            print("程序运行异常，需重启")
            os.system(start_command)
        time.sleep(60)


# detect_process('tomcat', '/usr/local/tomcat/bin/startup.sh')
detect_process('tomcat', "echo 'restarting tomcat......'")



# 5.搜索目录/home/tools/下所有已test开头，py结尾的文件(包括子目录的),
#   把文件全路径输出到一个列表里面打印出来
# -*- coding: utf-8 -*-
import os


def get_file(path, head, tail):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath,filenames)
        for filename in filenames:
            if filename.startswith(head) and filename.endswith(tail):
                file_list.append(os.path.join(dirpath, filename))
    print(file_list)
    return file_list


path = "/scipt/python/testerhome_pratice"
get_file(path, '20190428', '.xml')