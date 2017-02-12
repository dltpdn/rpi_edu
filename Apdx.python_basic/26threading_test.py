import threading

thread_status = [True] * 5

def counter(id, cnt):
    for i in range(cnt):
        print 'id %s --> %s' %(id, i)
    thread_status[id] = False
    print 'Thread %d is dead.' % id
    
for i in range(5):
    th = threading.Thread(target=counter, args=(i, 5));
    th.start()
    th.join()

print 'all threads died, main exiting.'