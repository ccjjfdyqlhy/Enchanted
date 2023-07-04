# Made by Darkstar, 2023/7/3

import os
import zipfile
import tkinter.messagebox as tkms
import psutil
import datetime
import time

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

cwd=os.getcwd()
print('DSPL 230703\nlooking for files...')
print('working directory: '+cwd)
compress_dir=cwd+'/plugins/'
compress_dir2=cwd+'/data.dsp'
print('getting plugin list...')
try:
    with open(cwd+'/plugins.dsl','r') as f:
        lines=f.read().split(',')
except FileNotFoundError:
    input('缺失插件配置文件,回车退出.')
    quit()
for line in lines:
    print('find plugin: '+line+'.dsp')
    try:
        f=zipfile.ZipFile(compress_dir+line+'.dsp','r')
    except:
        input('缺少插件文件,请确认游戏文件完整.回车退出')
        quit()
    for file in f.namelist():
        f.extract(file,cwd+'/mods/')
    f.close()
    print('loaded.')
print('all the plugins has been loaded.')
try:
    fd=open(cwd+'/plugins.cfg','r')
    first=str(fd.read())
    fd.close()
except FileNotFoundError:
    input('缺少程序配置文件，请确认游戏文件完整.回车退出')
    quit()
if first == '0':
    print('installing plugins configurlation..')
    #tkms.showinfo('DSPL','检测到首次启动，欢迎！\n我们将为你加载默认的插件配置，你可以以后修改.')
    try:
        f=zipfile.ZipFile(compress_dir2,'r')
    except FileNotFoundError:
        print('缺少插件配置包,请确认游戏文件完整.回车退出')
        quit()
    for file in f.namelist():
        f.extract(file,cwd+'/')
    f.close()
    fd=open(cwd+'/plugins.cfg','w')
    fd.write('114514')
else:
    pass
#tkms.showinfo('DSPL','全部插件和配置加载完成。\n关闭该窗口来继续启动MC...')
print('WAITING FOR THE GAME START...')
time.sleep(10)
while True:
    try:
        if isinstance(checkprocess("javaw.exe"),int) == True:
            today = str(datetime.datetime.today())
            print ("["+today+"] MC还活着.")
            time.sleep(3)
        else:
            today = str(datetime.datetime.today())
            print('['+today+'] MC被关闭了!执行预备方案...')
            cmd='del /F /Q '+cwd+'\mods\*'
            print('done,EXIT')
            os.system(cmd)
            quit()
    except psutil.NoSuchProcess:
        pass
