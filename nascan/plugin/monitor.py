#!/usr/bin/env python
# coding:utf-8

"""
这个脚本只是监控系统的CPU和内存以及磁盘使用率,还有进程
"""
import time
import logging
import psutil

logger = logging.Logger('monitor')
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
log_handler = logging.FileHandler('monitor.log')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


def get_cpu_percent():
    """
    CPU使用率
    """
    cpu_percent = psutil.cpu_percent()
    logger.info(u'CPU使用率:{}'.format(cpu_percent))
    #return cpu_percent

def get_mem_percent():
    """
    内存占用率
    """
    memory_info = psutil.virtual_memory()
    mem_loadavg = round((memory_info.total - memory_info.available) / memory_info.total * 100, 1)
    logging.info(u'内存占用率:{}'.format(mem_loadavg))
    # return mem_loadavg

def get_disk_percent():
    """
    获取磁盘使用情况
    """
    disk_info = psutil.disk_usage('/')
    total = disk_info.total
    used = disk_info.used
    free = disk_info.free
    percent = disk_info.percent
    logging.info(u'磁盘使用率:{}'.format(percent))

def proc_running_bool(proc_name):
    """
    根据进程名检查进程
    """
    proc_list = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username']) if proc_name in proc.info['name']]
    if proc_list:
        logging.info(u'{}服务运行正常'.format(proc_name))
        #return True
    else:
        logging.info(u'{}服务没有运行'.format(proc_name))
        #return False
    

def main():
    while True:
        get_cpu_percent()
        get_mem_percent()
        get_disk_percent()
        for proc_name in ['mysql','redis']
            proc_running_bool(proc_name)
        time.sleep(2*60)

if __name__=="__main__":
    main()