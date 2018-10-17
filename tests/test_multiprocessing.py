#!/usr/bin/env python
#coding:utf-8

import multiprocessing
import setproctitle
from multiprocessing import Manager
import time

def echo():
    time.sleep(2)
    print("caca")

def worker(procnum, return_dict):
    '''worker function'''
    print(str(procnum) + ' represent!')
    return_dict[procnum] = procnum
    
def add(m,n):
    return m+n


def foo(a):
    return a

from multiprocessing import Pool

#result = p.apply_async(foo, args=(a, ))
# foo和a分别是你的方法和参数，这行可以写多个，执行多个进程，返回不同结果
##p.close()
#p.join()
#result.get()


#===============================================================================

from multiprocessing import Process, Pool, Queue
import time
import setproctitle


class MainExitException(Exception):
    @staticmethod
    def sigterm_handler(signum, frame):
        raise MainExitException()

def run_domain_task(plugin_name, domain=None, port=None):
    """
    运行网站扫描任务,获取扫描结果
    :param plugin_name:
    :param domain http://xxx or https://xxx
    :param port 80
    :return:
    """
    # module = importlib.import_module('.' + plugin_name, package='risk_manage.scan_tasks')
    # plugin = module.Plugin(f"{domain}:{port}")
    # response = plugin.run_task()
    # return response
    return "hehe"


class TaskProcess(Process):
    def __init__(self, func, args=(),q=None):
        super(TaskProcess, self).__init__()

        self.func = func
        self.args = args

    def run(self):
        print('stock process started, now set process name...')
        setproctitle.setproctitle('[TASK->%s]' % task.args[0])
        # 获取主进程发送的信号,得到信号status置为2,在拉取策略更新任务时会执行
        #signal.signal(signal.SIGINT, MainExitException.sigterm_handler)
        # 获取KILL信号/ 用于捕获ctrl+c信息
        #signal.signal(signal.SIGTERM, ExitException.sigterm_handler)
        self.result = self.func(*self.args)
        #print(self.result)
        #print(self.result)
        time.sleep(5)
        q.put(self.result)
       
if __name__ == '__main__':
    """
    #result_list = []
    #jobs = []
    #p = Pool(4)
    #for i in range(5):
        result = p.apply_async(foo, args=(i,))
        result_list.append(result.get())
    p.close()
    p.join()
    #print(result.get())
    #print(result.values())
    # 最后的结果是多个进程返回值的集合
    #print return_dict
    #print return_dict.values()
    #print(result_list)
    +++++++++++
    """
    threads = []
    results = []
    have_done_list = []
    current_task_name = ''
    q = multiprocessing.Queue()
    plugin_list = [{"plugin_name":"66","ip":2,"port":80},{"plugin_name":"2","ip":2,"port":80},{"plugin_name":"3","ip":2,"port":80}]
    for plugin_info in plugin_list:
        threads.append(TaskProcess(run_domain_task, args=(plugin_info['plugin_name'], plugin_info['ip'], plugin_info['port']),q=q))
    for task in threads:
        
        task.start()
        print(task.is_alive())
        print(task.name)
        have_done_list.append(task.name)
        print(have_done_list)
        task.join()
        current_task_name = task.name
        #print(task.is_alive())
        #print(task.pid)
        if q.qsize>0:
            results.append(q.get())
    print(results)
   