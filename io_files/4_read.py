
# read([size]). Read size bytes from the file, unless EOF is hit. If size is omitted or negative, the full data
#  is returned.

# Write a function that open a file for reading and returns the number of bytes and newlines('\n').
def readFile(filename):
    filename = "/home/dipesh/amazatic/pyschool/io_files/"+filename
    f = open(filename)
    size = 0
    lines = 0
    buf = f.read(1)      # fill in byte to read
    print(buf)
    while buf!="":
        size+=1
        buf = f.read(1)
        if(buf=='\n'):
            lines+=1
        # fill in byte to read
    f.close()               # close file

    return (size, lines) 

print(readFile('tmp.txt'))