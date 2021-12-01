import os, sys
from socket import gethostbyname

# DOMAIN= "G:/PycharmProject/fullstack2/week1/domain.txt"

def main():
    # domain.txt里面存储的是需要批量解析的域名列表，一行一个
    with open("domain.txt", 'r') as f:
        for line in f.readlines():
            try:
                host = gethostbyname(line.strip('\n'))
            except Exception as e:
                print(e)
            else:
                # result.txt里面存储的是批量解析后的结果，不用提前创建
                with open('result.txt', 'a+') as r:
                    #要域名的时候就不注释这行代码 r.write(line.strip('\n') + ' ')
                    r.write(host + '\n')

if __name__ == '__main__':
    main()

