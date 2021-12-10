f = open('/home/dipesh/amazatic/pyschool/io_files/dob.csv', 'w')
f.write('"1 Jan, 2010",John\n')
f.write('"23 May, 2001",Mary\n')
f.close()

# Write a function to read a CSV file with ',' as delimiter and returns a list of records.
# The function must be able to ignore ',' that are within a pair of double quotes '"'.
def csvReader(filename):
    filename = "/home/dipesh/amazatic/pyschool/io_files/"+filename
    records = []
    for line in open(filename):
        line = line.rstrip()  # strip '\n'
        if line=='':
           continue           # ignore empty line
        else:
            records.append([line])


    return records 

print(csvReader('dob.csv'))