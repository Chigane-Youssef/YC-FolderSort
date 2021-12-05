# -*- coding: utf-8 -*-
""" @author : CHIGANE Youssef"""

from tkinter import *
from tkinterdnd2 import *
from tkinter import filedialog
import os
import sys
import shutil
import copy

folders1 = []
folders2 = []
all_files = []

def mover(folders,path,k=0):
    
    for i in range(len(folders)):
        for j in range(len(folders[i])):
            if k == 0:
                files = os.listdir(folders[i][j])
            for e in files:
                if e.endswith(".exe"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Exe")
                    except:
                        None
                elif e.endswith(".pdf"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Pdf")
                    except:
                        None
                elif e.endswith(".html") or e.endswith(".htm"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Html")
                    except:
                        None
                elif e.endswith(".txt"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Txt")
                    except:
                        None
                elif e.endswith(".rar"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Rar")
                    except:
                        None
                elif e.endswith(".xls"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Xls")
                    except:
                        None
                elif e.endswith(".xlsx"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Xls")
                    except:
                        None
                elif e.endswith(".zip"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Zip")
                    except:
                        None
                elif e.endswith(".ppt"):
                    try:
                        shutil.move(folders[i][j]+"/"+e,path+"/Ppt")
                    except:
                        None
                elif e.find(".") != -1 and ref.get() == "1":
                     isExist = os.path.exists(path+"/"+e[e.find(".")+1:])
                     if not isExist:
                         os.makedirs(path+"/"+e[e.find(".")+1:])
                     shutil.move(folders[i][j]+"/"+e,path+"/"+e[e.find(".")+1:])

def add_it1(event):
    global folders1
    texto1.config(state='normal')
    exec("texto1.insert(END,"+'"'+str(event.data)+'\\n"' +")")
    texto1.config(state='disabled')

    folders1.append(event.data.split(" "))

def add_it2(event):
    global folders2
    texto2.config(state='normal')
    exec("texto2.insert(END,"+'"'+str(event.data)+'\\n"' +")")
    texto2.config(state='disabled')
    
    folders2.append(event.data.split(" "))

def sort_it():
    global folders1
    global folders2
    all_files = []
    path = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
    
    x = ["Exe", "Pdf", "Txt", "Xls", "Zip", "Rar","Ppt","Html"]
    for e in x:
        isExist = os.path.exists(path+"/"+e)
        if not isExist:
            os.makedirs(path+"/"+e)
        mover(folders1,path)
        
    for e in folders2:
        print(folders2)
        for j in range(len(e)):
            for path, subdirs, files in os.walk(e[j]):
                for name in files:
                    file = os.path.join(path, name)
                    file.replace("\\", "/")
                    all_files.append(file)
    mover(all_files,path,k=1)
    
    
def sort_it_by():
    global foders
    
    window = Tk()
    window.geometry('100x150')
    window.maxsize(160,170)
    liste = Listbox(window, selectmode = "multiple")
    liste.pack(expand = YES, fill = "both")
    x = ["Exe", "Pdf", "Txt", "xls", "xlsx","", "Zip", "Rar","Ppt","Html"]
    
    for i in range(len(x)):
        liste.insert(END, x[i])
        liste.itemconfig(i, bg = "silver" if i % 2 == 0 else "gold")
        
    sorter = Button(window,text="done",fg="white",bg="#d77337",font=("times new roman",13),command=None)
    sorter.pack(fill=X,pady=0, padx=10)
    window.mainloop()
    return copy.copy(liste)
    
root = Tk()
root.title("YC-Folder_sortApp")
root.geometry("1000x600")
root.maxsize(360,1000)
root.minsize(360,240)
root.configure(background='pink')

label = Label(root,text="Put all your folders1 to be sorted by extension",relief=RIDGE).pack(fill=X,pady=10, padx=10)

ref = StringVar()
checker1 = Radiobutton(root, text="activate all types sorter",variable=ref,value=True,bg="yellow")
checker2 = Radiobutton(root, text="activate standard file sorter",variable=ref,value=False,bg="yellow")
checker2.pack()
checker1.pack()

sort_by = Button(root,text="Sort_by",fg="white",bg="#d77317",font=("times new roman",13),command=sort_it_by).\
                    pack(side=BOTTOM,fill=X,pady=5, padx=10)
                    
sort = Button(root,text="Sort_All",fg="white",bg="#d77337",font=("times new roman",13),command=sort_it).\
                    pack(side=BOTTOM,fill=X,pady=0, padx=10)
                    
v1 = Scrollbar(root)
v1.pack(side=RIGHT,fill=Y)
v2 = Scrollbar(root)
v2.pack(side=LEFT,fill=Y)

texto1 = Text(root,relief=SOLID,borderwidth=2,height=12)
texto1.pack(fill=X,pady=3, padx=1)
texto1.config(state='disabled')

labelo = Label(root,text="Put all your folders1 to be sorted all by extension",relief=RIDGE).pack(fill=X,pady=10, padx=10)

texto2 = Text(root,relief=SOLID,borderwidth=2,height=12)
texto2.pack(fill=X,pady=3, padx=1)
texto2.config(state='disabled')

v1.config(command=texto1.yview)
v2.config(command=texto2.yview)

texto1.drop_target_register(DND_FILES)
texto1.dnd_bind('<<Drop>>', add_it1)

texto2.drop_target_register(DND_FILES)
texto2.dnd_bind('<<Drop>>', add_it2)
root.mainloop()
