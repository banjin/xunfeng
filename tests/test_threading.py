#!/usr/bin/env python
#coding:utf-8

"""
获取每个线程的结果
"""
import threading

class TaskThread(threading.Thread):

    def __init__(self, func, args=()):
        super(TaskThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def run_task(domain):
    plugins_list = [1,2,3,4,5,6]
    results = []
    threads = []
    for plugin_name in plugins_list:
        threads.append(TaskThread(run_domain_task, args=(plugin_name, domain)))
    for task in threads:
        task.start()
    for task in threads:
        task.join()
        results.append(task.get_result())
    print(results)

def run_domain_task(plugin_name, domain=None, port=None):
    """
    运行网站扫描任务,获取扫描结果
    :param plugin_name:
    :param domain http://xxx or https://xxx
    :param port 80
    :return:
    """
    #module = importlib.import_module('.' + plugin_name, package='scan_tasks')
    #plugin = module.Plugin("{domain}:{port}".format(domain, port))
    #response = plugin.run_task()
    response = {
        "level": 3,
        "desc": u" hehe",
        "id": plugin_name,
        'domain': domain
    }
    return response

if __name__ == "__main__":
    run_task('www.baidu.com')