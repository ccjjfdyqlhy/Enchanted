# -*- coding:utf-8 -*-# psutil 模块需另行安装
import psutil
import os
import datetime
import time
cwd=os.getcwd()


def checkprocess(processname):
    # --获取进程信息--
    pl = psutil.pids()  #所有的进程列出来
    #print (pl)
    #p = psutil.Process(8)
    #print ("p:",p)
    #print ("name:",p.name())    # 进程名字
    #print ("exe:",p.exe()) # 进程exe路径
    #print ("cwd:",p.cwd()) # 进程工作目录
    #print ("cmdline:",p.cmdline()) # 进程启动的命令行

    # --获取CPU的信息--
    cpu_count = psutil.cpu_count()  # CPU逻辑数量
    cpu_times = psutil.cpu_times()  # 统计CPU的用户 I 系统 J 空闲时间

    # --获取系统负载--
    getloadavg = psutil.getloadavg()    # 分别表示 1 分钟， 5 分钟， 15 分钟的系统负载情况

    # --获取内存信息--
    virtual_memory = psutil.virtual_memory()   #获取物理内存的大小
    swap_memory = psutil.swap_memory()  #获取交换内存的大小

    # --获取磁盘分区，磁盘使用率和磁率IO信息--
    disk_partitions = psutil.disk_partitions()




    for pid in pl:

        if psutil.Process(pid).name() == processname:
            print (pid)
            p = psutil.Process(pid)
            print ("exe:",p.exe())
            return pid

try:
    if isinstance(checkprocess("javaw.exe"),int) == True:
        print ("检测到运行的MC")
        while True:
            try:
                if isinstance(checkprocess("javaw.exe"),int) == True:
                    today = str(datetime.datetime.today())
                    print ("["+today+"] MC还活着.")
                    time.sleep(5)
                else:
                    today = str(datetime.datetime.today())
                    print('['+today+'] MC被关闭了!执行预备方案...')
                    cmd='del /F /Q '+cwd+'\mods\*'
                    print('done,EXIT')
                    os.system(cmd)
                    quit()
            except psutil.NoSuchProcess:
                pass
    else:
        input('请先启动MC,回车退出')
except psutil.NoSuchProcess:
    pass