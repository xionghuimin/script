#!/usr/bin/env python
# conding:utf-8

##把同一行的ip换行,然后写进result.txt的文件里
with open('ip.txt','r',encoding='utf-8') as readlist:
    for dirs in readlist.readlines():
         with open('result.txt','a',encoding='utf-8') as writelist:
             b = dirs.replace(",", '\n')
             writelist.write(b)
# 去除重复ip，然后把结果写进only.txt文件里
with open('result.txt','r',encoding='utf-8') as readlist:
    lines_seen = set()
    for line in readlist.readlines():
        if line not in lines_seen:
            lines_seen.add(line)
            with open('only.txt','a',encoding='utf-8') as writelist:
                writelist.write(line)

#参考文章：https://blog.csdn.net/qq_22764813/article/details/73187473?locationNum=1&fps=1