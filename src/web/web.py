#coding:utf-8
'''
Created on 2018��9��29��

@author: Tony
'''

from urllib import request
from bs4 import BeautifulSoup as BS
import re
from astroid.__pkginfo__ import description
from astroid.util import limit_inference

Web_Addr = "https://www.alldatasheet.com/view.jsp?Searchword="
Headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":    "pdf1.alldatasheet.com",
    "Referer": "",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
}

unit_dev_info={'name':None,'brand':None,'description':None,'url':"None",'Original_url':'None','num':'None'}
dev_info =[]

class Dev_Info:
    
    def __init__(self):
        self.name= None
        self.brand = None
        self.description= None
    
    def check(self):
        print("check datasheet")
        
    def download(self):
        print("downloading...")
    

class Web_Search(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        
    
    def Get_addr(self,web,key_word='lm1117'):
        URL_list = []
        page = request.urlopen(web+key_word)
        html = page.read()
        html = html.decode("utf-8")
        bs = BS(html,'html.parser')
        
        reg = r'www.alldatasheet.com/datasheet-pdf/pdf/.+?\.html'#正则表达式
        reg_addr = re.compile(reg)#编译一下，运行更快
        
        tb = bs.findAll(src=re.compile(r'//other.alldatasheet.com/etc/electronic_parts_datasheet.gif'),limit=10)
        desc=[]
        #del desc[0:]
        for des in tb:
            tem=des.find_parent().find_parent().find_next_sibling().stripped_strings
            for str in tem: 
                desc.append(str)
                #print(str)
        #print(tb)       
        addr_list = reg_addr.findall(html)#进行匹配
        addr_list = list(set(addr_list))
        del dev_info[0:]
        for addr,des in zip(addr_list,desc):
            print(addr)
            par = addr.split('/')
            unit_dev_info["brand"] = par[4]
            unit_dev_info['num'] = par[3]
            unit_dev_info["name"] = par[5][0:-5]
            unit_dev_info["description"] = des
            Headers["Referer"] = addr
            URL1 = "http://pdf1.alldatasheet.com/datasheet-pdf/view/" + addr[39:]
            rqt = request.Request(URL1,headers=Headers)
            unit_dev_info['Original_url'] = URL1
            res = request.urlopen(rqt)
            html1 = res.read()
            html1 = html1.decode("utf-8")
            reg1 = r'datasheet-pdf/.+?\.pdf'#正则表达式
            reg_addr1 = re.compile(reg1)#编译一下，运行更快
            addr_list1 = reg_addr1.findall(html1)
            unit_dev_info['url'] = "http://pdf1.alldatasheet.com/" + addr_list1[0]
            com_info = "Brand is:" + unit_dev_info["brand"] + '\n' "Name:" + unit_dev_info["name"] + '\nWeb Address:' + unit_dev_info['url'] + '\n'\
            +"des:" + unit_dev_info["description"]
            URL_list.append(com_info)
            dev_info.append(unit_dev_info.copy())
            #print(unit_dev_info['url'])
        #print(dev_info)
        return URL_list

if __name__ == "__main__":
    act1 = Web_Search()
    act1.Get_addr(Web_Addr)
#     URL1 = 'https://pdf1.alldatasheet.com/datasheet-pdf/view/660132/ETC2/1117.html'
#     rqt = request.Request(URL1,headers=Headers)
#     res = request.urlopen(rqt)
#     html = res.read()
#     html = html.decode("utf-8")
#     print(html)


        

        
        
