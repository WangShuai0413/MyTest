# -*- coding:utf-8 -*-
import redis

r=redis.Redis(host="127.0.0.1",port=6379,db=0)

def sent(key,value):
        r.set(key,value)
        return 1
def printValue(key):
        value=r.get(key)
        print 'value:'+value
        return 1

if __name__=='__main__':
        while 1:
                print '1.SET key'
                print '2.GET key'
                print '0.输入其他键退出'
                choose=int(input('请输入您的选择:'))
                if choose == 1:
                        print '**********SET*********'
                        key=raw_input("请输入key：")
                        value=raw_input("请输入value:")
                        sent(key,value)
                elif choose == 2:
                        print '**********GET*********'
                        key=raw_input('请输入key:')
                        printValue(key)
                else:
                        exit()
