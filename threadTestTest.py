import threading
import time

exitFlag=0

class MyThread(threading.Thread):
    def __init__(self,threadID,threadName,delayTime):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.threadName=threadName
        self.delayTime=delayTime

    def run(self):
        print("start : "+self.threadName)
        print_time(self.threadName,self.delayTime,5)
        print("end : "+self.threadName)


def print_time(threadName,delayTime,recycleTime):
    while recycleTime:
        if exitFlag:
            threadName.exit()
        time.sleep(delayTime)
        print("%s : %s"%(threadName,time.ctime(time.time())))
        recycleTime-=1



Thread1=MyThread(1,"Thread--1",5)
Thread2=MyThread(2,"Thread--2",10)

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print("ALL ALL ALL IS OVER!")

