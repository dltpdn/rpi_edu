import threading

class MyThread(threading.Thread):
    def __init__(self, cnt):
        threading.Thread.__init__(self)
        self.cnt = cnt
        
    def run(self):
        for i in range(self.cnt):
            print 'id %s --> %s' %(self.getName(), i)
        print 'Thread %s is dead.' % self.getName()

    
for i in range(5):
    th = MyThread(5)
    th.start()
    th.join()
    

print 'all threads died, main exiting.'