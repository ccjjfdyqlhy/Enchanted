import tkinter
from tkinter.messagebox import *
from tkinter.messagebox import *
from tkinter.ttk import *
import tkinter.ttk
import os
import zipfile
import subprocess
import requests

ver='4'
cwd=os.getcwd()

root=tkinter.Tk()
root.title('MCVM '+ver)
root.geometry('300x400')
root.resizable(False,False)
os.system('mkdir MCVM')

try:
    verreadf=open(cwd+'/MCVM.cfg')
    verread=verreadf.read()
    contents=verread.split('\n')
    vername=contents[0]
    verver=contents[1]
    key=contents[2]
    print('[INFO]version feched: '+vername+' '+verver)
    print('[INFO]key fetched: '+key)
except:
    print('[FETAL]未安装许可证，无法启动')
    showerror('错误','你还没有安装你的版本许可证,请联系你的版本提供商。')
    root.destroy()
notebook = tkinter.ttk.Notebook(root)
versiontab = tkinter.Frame()
updatetab = tkinter.Frame()
accounttab = tkinter.Frame()
notebook.add(versiontab, text='    版本信息    ')
notebook.add(updatetab,text='    获取更新    ')
notebook.add(accounttab, text='    账户/选项    ')
notebook.pack()

def unpack(targetfile,targetdir):
    with zipfile.ZipFile(targetfile) as zf:
        try:
            zf.extractall(targetdir)
            print('[WARN]Unpack Successfully.')
        except zipfile.BadZipFile:
            print('[ERROR]Failed when unpacking')

def login():
    showinfo('提示','请到控制台操作.')
    print('[INFO]launching login process')
    unpack('launcher.dll',cwd+'/MCVM/launcher/')
    os.system(cwd+'/MCVM/launcher/cmcl.exe account --login=authlib --address=https://littleskin.cn/api/yggdrasil')
    os.system('del /q "'+cwd+'\MCVM\launcher\cmcl.exe"')

def loginoffline():
    showinfo('提示','请到控制台操作.')
    username=unin.get()
    print('[INFO]launching login process')
    unpack('launcher.dll',cwd+'/MCVM/launcher/')
    os.system(cwd+'/MCVM/launcher/cmcl.exe account --login=offline --name='+username)
    os.system('del /q "'+cwd+'\MCVM\launcher\cmcl.exe"')

def register():
    print('[INFO]launching browser')
    os.system('start https://littleskin.cn/')

def chkupdate():
    print('[INFO]checking update from the server...')

def launch():
    try:
        f=open(cwd+'/MCVM/launcher/cmcl.json','r')
        f.close()
        unpack('launcher.dll',cwd+'/MCVM/launcher/')
        root.withdraw()
        os.system(cwd+'/MCVM/launcher/cmcl.exe --list='+cwd+'/.minecraft')
        os.system(cwd+'/MCVM/launcher/cmcl.exe config checkAccountBeforeStart false')
        if chkvar.get():
            print('[INFO]completing assets...')
            os.system(cwd+'/MCVM/launcher/cmcl.exe version "'+vername+'" --complete assets')
            print('\n[INFO]completing libraries...')
            os.system(cwd+'/MCVM/launcher/cmcl.exe version "'+vername+'" --complete libraries')
            print('\n[INFO]completing natives...')
            os.system(cwd+'/MCVM/launcher/cmcl.exe version "'+vername+'" --complete natives')
            print('[INFO]done completing files.')
        os.system('del /q "'+cwd+'\MCVM\latestlaunch.ps1"')
        os.system(cwd+'/MCVM/launcher/cmcl.exe version "'+vername+'" --export-script-ps='+cwd+'/MCVM/latestlaunch.ps1')
        print('[INFO]launching Script Generated!')
        os.system('powershell Set-ExecutionPolicy -Scope CurrentUser ByPass')
        print('[INFO]powershell script unlocked!')
        subprocess.run('powershell "'+cwd+'/MCVM/latestlaunch.ps1"')
        print('[INFO]progress started.')
        os.system('del /q "'+cwd+'\MCVM\launcher\cmcl.exe"')
        root.deiconify()
    except FileNotFoundError:
        showinfo('启动失败','你还没有登录到Minecraft.')

#versiontab design
Label(versiontab,text=vername+' '+verver+'的开发者通行证').pack()
Label(versiontab,text='序列号: '+key).pack()
Button(versiontab,text='\n 启动 '+vername+'\n',command=launch).pack()
chkvar = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(versiontab,text='启动时补全文件(可能会多花些时间)',variable=chkvar)
check1.pack()

#updatetab design
Label(updatetab,text='获取 '+vername+' 测试渠道的更新').pack()
Button(updatetab,text='    检查更新    ',command=chkupdate).pack()

#accounttab design
Label(accounttab,text='登录到Minecraft').pack()
Button(accounttab,text='  使用Littleskin登录通行证(推荐)  ',command=login).pack()
Button(accounttab,text='  注册Littleskin账号  ',command=register).pack()
Label(accounttab,text='——————————————————————').pack()
Label(accounttab,text='离线登录').pack()
unin=Entry(accounttab)
unin.pack()
Button(accounttab,text='  设定用户名  ',command=loginoffline).pack()

root.mainloop()