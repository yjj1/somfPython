# #encoding=utf-8
# import _csv
# from ftplib import FTP
# import os
# import win32ui
# import Tkinter
# from Tkinter import *
#
# #初始变量
# # global targetFileName
# # targetFileName = ''
# #浏览文件，获取要上传的CSV文件
# def openTargetFileFolder():
#     dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
#     dlg.SetOFNInitialDir('D:\\')  # 设置打开文件对话框中的初始显示目录
#     dlg.DoModal()
#
#     global targetFileName
#     targetFileName = dlg.GetPathName()  # 获取选择的文件名称
#     label['text']=targetFileName
#
# # def openErrorDialog(error):
# #     dlg = win32ui.
# #     messagebox.askokcancel('Python Tkinter', 'askokcancel')
# #     buttontext.set('askquestion')
#
# #读取CSV文件，重新写入新文件
# def readFile(oldPath):
#     # oldPath = 'D:\\test.csv'
#     try :
#         if 'csv' not in oldPath:
#             resultLabel['fg'] = 'red'
#             resultLabel['text'] = '文件格式错误'
#             return 'false'
#         newPath = oldPath.replace('.csv','')
#
#         oldFile = open(oldPath,'rb')
#         reader = _csv.reader(oldFile)
#         newFile = open(newPath, 'wb')
#         for a,b,c,d,e,f,g,h,i in reader:
#             strLine = a+'|'+b+'|'+c+'|'+d+'|'+e+'|'+f+'|'+g+"|"+h+'|'+i+'\n'
#             print a+'|'+b+'|'+c+'|'+d+'|'+e+'|'+f+'|'+g+"|"+h+'|'+i+'\n'
#             newFile.writelines(strLine)
#         oldFile.close()
#         newFile.close()
#         return newPath
#
#     except :
#         resultLabel['fg'] = 'red'
#         resultLabel['text'] = '文件格式错误'
#
# #上传至FTP服务器
# def ftpUpload(fileName):
#     ftp = FTP()
#     ftp.set_debuglevel(2)
#     ftp.connect('127.0.0.1', '21')
#     ftp.login('Y','x')
#     bufsize = 1024
#     fileHandler = open(fileName, 'rb')
#     ftp.storbinary('STOR %s' % os.path.basename(fileName), fileHandler, bufsize)
#     ftp.set_debuglevel(0)
#     fileHandler.close()
#     ftp.quit()
#     print 'ftp successfully'
#     resultLabel['fg'] = 'green'
#     resultLabel['text']='操作成功'
#
# def doUpload():
#     print targetFileName
#     filePath = readFile(targetFileName)
#     if 'false' not in filePath:
#         ftpUpload(filePath)
# #打开窗口
# top = Tkinter.Tk()
# top.title('CSV转化上传')
# global label
# label = Tkinter.Label(top)
# label.pack()
#
# global resultLabel
# resultLabel = Tkinter.Label(fg='green')
# resultLabel.pack()
#
# browseBtn = Tkinter.Button(top, text='浏览', command=openTargetFileFolder)
# browseBtn.pack()
# uploadBtn = Tkinter.Button(top, text='上传', command=doUpload)
# uploadBtn.pack()
#
# # quitBtn = Tkinter.Button(top, text='退出', command=top.quit)
# # quitBtn.pack()
#
# top.mainloop()
#
# # newPath = readFile(targertFileName)
# # ftpUpload(newPath)
