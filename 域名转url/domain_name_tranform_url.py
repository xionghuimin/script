#!/usr/bin/env python
# conding:utf-8

with open('a.txt','r',encoding='utf-8') as readlist:
    for dirs in readlist.readlines(): 
         with open('http.txt','a',encoding='utf-8') as writelist:
                    writelist.write('http://'+dirs)

#备注:这个脚本可以在将txt文件中的域名加上http://或https://后转化为url，然后写入到指定文件中