import tkinter
import os
from tkinter.messagebox import *
cwd=os.getcwd()
dspl=cwd+'\pluginloader.exe'
cfg=cwd+'\launch.cfg'
dta=cwd+'\data.dsp'

def changeversion():
    newver=e1.get()
    with open('launch.cfg','w') as f:
        f.write(newver)
        f.close()
    showwarning('DSPL管理器','成功修改植入的目标版本为 '+newver+' 。\n重新启动此程序来查看详情。')
    root.destroy()

root=tkinter.Tk()
root.title('DSPL管理器')
root.geometry('500x600')
tkinter.Label(root,text='————————————————DSPL状态————————————————').pack()
tkinter.Label(root,text='DSPL管理器: Made by Darkstar, version 1.1').pack()
tkinter.Label(root,text='当前DSPL: '+dspl).pack()
tkinter.Label(root,text='当前launch.cfg文件: '+cfg).pack()
tkinter.Label(root,text='当前data.dsp文件: '+dta).pack()
tkinter.Label(root,text='————————————————插件状态————————————————').pack()
try:
    with open(cwd+'/plugins.dsl','r') as f:
        lines=f.read().split(',')
except FileNotFoundError:
    showerror('DSPL管理器','未找到插件配置文件。')
for line in lines:
    tkinter.Label(root,text=line+'.dsp 已就绪').pack()
try:
    with open(cwd+'/launch.cfg','r') as f:
        vername=f.read()
        f.close()
except FileNotFoundError:
    showerror('DSPL管理器','未找到launch.cfg文件。')
tkinter.Label(root,text='————————————————更新选项————————————————').pack()
tkinter.Label(root,text='整合包功能更新直接用新的data.dsp替换旧的;\n新插件放入版本目录下update文件夹,点击下面的[更新]').pack()
tkinter.Button(root,text='     更新...     ').pack()
tkinter.Label(root,text='————————————————加载选项————————————————').pack()
tkinter.Label(root,text='当前要渗透并植入插件的目标版本: versions/'+vername+'/').pack()
e1=tkinter.Entry(root)
e1.pack()
tkinter.Button(root,text='     修改...     ',command=changeversion).pack()

root.mainloop()