# The open method returns a file object. Syntax: open(name[, mode]). where mode can be 'r' (read), 'w'(write) or 'a'(append). The default mode is 'r'.
# The close method closes an opened file object.

# Create a file called 'tmp.txt' for writing, and close the file after that.

# open a file
filename = "/home/dipesh/amazatic/pyschool/io_files/"
mode = 'w'
f = open(filename+"tmp.txt", mode)  # replace 'filename' and 'mode' 

# write to file
f.write('hello')

# close a file
f. close()