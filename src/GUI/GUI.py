#coding:utf-8
'''
Created on 2018��9��29��

@author: Tony
'''
import os
import sys
from textwrap import fill
from test.test_heapq import SideEffectLT
from tkinter.constants import RAISED, FLAT
from msilib.schema import Font
from _ctypes_test import func
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
import tkinter.messagebox as mb
from tkinter import *
from web import web 
class Application(Frame):
    def Search(self):
        act1 = web.Web_Search()
        act1.Get_addr(web.Web_Addr,key_word = self.input.get())
#         self.show.delete(0.0, END)
#         self.show.insert(0.0, act1.Get_addr(web.Web_Addr,key_word = self.input.get()))

        self.j=0
        for i in web.dev_info:
            self.lb[self.j][0]['width']=20
            self.lb[self.j][0]["text"] = i["brand"]
            self.lb[self.j][0].grid(row=self.j, column=0, sticky="nsew")
            self.lb[self.j][1]['width']=20
            self.lb[self.j][1]["text"] = i['name']
            self.lb[self.j][1].grid(row=self.j, column=1, sticky="nsew")
            self.lb[self.j][2]['width']=60
            self.lb[self.j][2]["text"] = i['description']
            self.lb[self.j][2]["justify"] ='left'
            self.lb[self.j][2].grid(row=self.j, column=2, sticky="nsew")
            self.lb[self.j][3]['width']=20
            self.lb[self.j][3]['fg'] = "brown"
            self.lb[self.j][3]["text"] = "Download"
            self.lb[self.j][3].bind("<ButtonPress-1>", self.handlerAdaptor(self.download,url=i['url']))
#             self.lb.bind("<Enter>", self.c1)
            self.lb[self.j][3].grid(row=self.j, column=3, sticky="nsew")
            self.j+=1
        #print(self.lb)
        

        
    def createMenus(self):
        self.menubar = Menu(self)
        #self.menubar.add_command(label="File")
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.About)
        filemenu.add_command(label="Save", command=self.Save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu= filemenu)
        
        self.menubar.add_command(label="About",command=self.About)

    def createWidgets(self):
        self.var = StringVar()
        self.input = Entry(self, textvariable = self.var)
        #self.input.grid(row=0, column=0, sticky="nsew")
        self.input.pack(fill = X)
        
        self.search = Button(self,bg="grey")
        self.search["text"] = "Search",
#         self.search.bind("<Enter>",self.Search)
#         self.search.focus_set() 
        self.search["command"] = self.Search
        #self.search.grid(row=0, column=1, sticky="nsew")
        self.search.pack(fill = X)
        
        frm_head = Frame(self,width=120, height=10)
        
        lb_1 = Label(frm_head,fg='red',width=20)
        lb_1["text"] = "Brand"
        lb_1.grid(row=0, column=0, sticky="nsew")
        lb_2 = Label(frm_head,fg='red',width=20)
        lb_2["text"] = "Component"
        lb_2.grid(row=0, column=1, sticky="nsew")
        lb_3 = Label(frm_head,fg='red',width=60)
        lb_3["text"] = "Description"
        lb_3.grid(row=0, column=2, sticky="nsew")
        lb_4 = Label(frm_head,fg='red',width=20)
        lb_4["text"] = "Operation"
        lb_4.grid(row=0, column=3, sticky="nsew")
        frm_head.pack(fill=X)
        
        self.frm_content = Frame(self,width=100, height=10)
        self.lb  = [[Label(self.frm_content) for i in range(4)] for i in range(20)]
        self.frm_content.pack(fill = BOTH, expand=1)

#         self.show = Text(self, width=100, height=10)
#         self.show.insert(INSERT, "debug info...")
        
#         self.scrl = Scrollbar(self)
#         self.scrl.pack(side=RIGHT, fill=Y)
#         self.show.configure(yscrollcommand = self.scrl.set)
#         self.show.pack(fill = BOTH, expand=1)
#         self.scrl['command'] = self.show.yview

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill = BOTH)
        self.createMenus()
        self.createWidgets()
        self.j = 0
        
    def About(self):
        mb.showinfo("Info","Datasheet Searcher\nAuthor:Dongdong\nCreated on 2018.09.29\nVersion:V00")
    
    def Save(self):
        try:
            fd = open("../../Search_Records.txt","w")
            fd.write(self.show.get(0.0,END))
            fd.close()
            mb.showinfo("Info","Save success!")
        except:
            #print("File open error")
            mb.showinfo("Error","Save failure!")
            
    def download(self,event,url='error'):
        mb.showinfo("Info", url)
    def handlerAdaptor(self,fun, **kwds):
        return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
        
    def c1(self):
        self.lb.config(Font='bold')

if __name__ == '__main__':
    root = Tk()
    root.title("Datasheet Searcher")
    #root.geometry('300x200')
    #root.propagate(False)
    app = Application(master=root)
    root.config(menu=app.menubar)
    app.mainloop()
    root.destroy()