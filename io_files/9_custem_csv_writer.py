# Define a function that takes in a list of records and stores the data in csv format.

def csvWriter(records):
    f = open('/home/dipesh/amazatic/pyschool/io_files/{}.csv'.format("csvdata"), 'w')
    f.write(str(records[0])+'\n')
    f.write(str(records[1])+'\n')
    f.close()
    return "records added in .csv file"
records = []
records.append({'x':1, 'y':2, 'z':3})
records.append({'z':6, 'y':5, 'x':4})
print(csvWriter(records))

