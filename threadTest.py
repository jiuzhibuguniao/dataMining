import time
import threading

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.name=name
        self.threadID=threadID
        self.counter=counter

    def run(self):
        print("Begin : "+self.name)
        print_time(self.name,self.counter,5)
        print("End : "+self.name)




def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s"%(threadName,time.ctime(time.time())))
        counter-=1



Thread1=myThread(1,"Thread-1",10)
Thread2=myThread(2,"Thread-2",20)

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print("ALL IA OVERE.")




