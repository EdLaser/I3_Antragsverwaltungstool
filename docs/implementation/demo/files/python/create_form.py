import csv
import sys

print('Variable count: ', len(sys.argv))
if len(sys.argv) == 0:
    print('failure')

with open('new_form.txt', 'w') as write_file:
    writer = csv.writer(write_file, delimiter=';')
    for arg in sys.argv:
        writer.writerow(arg)
