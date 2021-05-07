import csv
import sys
import os

print('Variable count: ', len(sys.argv))
if len(sys.argv) == 0:
    print('failure')


#def create_file(filename):
# List of things to write
# open the file
file_write = open(os.path.join('output', "new_form.txt"), 'w')
writer = csv.writer(file_write, delimiter=';')
for arg in sys.argv[1]:
    writer.writerow(arg)


#create_file("new_form.txt")
