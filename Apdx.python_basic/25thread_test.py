import thread, time

thread_status = [True] * 5

def counter(id, cnt):
    for i in range(cnt):
        print 'id %s --> %s' %(id, i)
    thread_status[id] = False
    print 'Thread %d is dead.' % id
    
for i in range(5):
    thread.start_new_thread(counter, (i, 5))


#time.sleep(2)
while True in thread_status:
    pass

print 'all threads died, main exiting.'