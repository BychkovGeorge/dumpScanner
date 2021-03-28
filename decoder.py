import csv


def file_reader(file_name):
    with open(file_name, encoding='utf-8') as r_file:
        dump = csv.reader(r_file, delimiter=",")
        count = 0
        for row in dump:
            if count > 99:
                times.append(row[1])
            count += 1


times = []
intervals = []
file_reader('dump.csv')

for i in range(len(times)):
    if i != len(times) - 1:
        intervals.append(float(times[i + 1]) - float(times[i]))

covert_message = ''
for i in range(len(intervals)):
    if 2.2 < intervals[i] < 2.3:
        covert_message += '1'
    elif 0.2 < intervals[i] < 0.3:
        covert_message += '0'

print(covert_message)
