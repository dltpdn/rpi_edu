import threading, time

class MyThread(threading.Thread):
    live = True
    cnt = 0;
    def run(self):
        while True:
            if not self.live:
                print '%s is dead.' % self.getName()
                break;
            print self.getName(), self.cnt
            time.sleep(1)
            self.cnt = self.cnt + 1

    def stop(self):
        self.live = False



th = MyThread()
th.start()
try:
    for i in range(10) :
        print 'Main',  i
        time.sleep(0.5)
finally:
    print 'Main is dead.'
    th.stop()
 
