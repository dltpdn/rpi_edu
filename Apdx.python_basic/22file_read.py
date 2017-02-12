file_name = "file.txt"
#file_name = "no_file.txt"
try:
    f = open(file_name)
    lines = f.read()
    f.close()
    words = lines.splitlines()
    print words
except IOError:
    print 'Can not open the file.'
