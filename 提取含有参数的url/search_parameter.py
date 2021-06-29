#!/usr/bin/env python
# conding:utf-8

#字符串中有“？”且不在字符串的结尾的就写入result.txt中
with open('JSurl.txt','r',encoding='utf-8') as readlist:
    for dirs in readlist.readlines():
        # re_result=re.search(r"'?'",dirs)
        # re_result=str(re_result)
        if "?" in dirs :
            re = dirs.find("?") #判断字符中是否有“？”，如果有则返回该字符串的位置，是从坐标0开始算的
            # a=len(dirs)-2是为了判断“？”是不是在最后一个字符，len()与find()不同是从一开始算字符串的长度的，在加上每行字符中\n换行符也占了一个字符，所以要减2
            a=len(dirs)-2
            #判断字符串中“？”是不是在字符的最后
            if re < a :
                with open('result.txt','a',encoding='utf-8') as writelist:
                    writelist.write(dirs)

#去除result.txt中的重复字符串，然后把结果写进only.txt文件里
with open('result.txt','r',encoding='utf-8') as readlist:
    lines_seen = set()
    for line in readlist.readlines():
        if line not in lines_seen:
            lines_seen.add(line)
            with open('only.txt','a',encoding='utf-8') as writelist:
                writelist.write(line)

#参考文章：https://www.cnblogs.com/luguankun/p/11846401.html（判断一个字符是否在一个字符串中）
