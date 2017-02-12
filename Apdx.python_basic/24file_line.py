file_name = 'file.txt'

try:
    f = open(file_name)
    cnt = 0
    while True:
        cnt += 1
        line = f.readline()
        if line == '':
            break
        print "%d : %s" %(cnt, line),
except IOError:
    print 'Can not open the file'
