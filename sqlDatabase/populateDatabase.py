''' statistics2tablerows.py

    A script for converting the region data in "Baltimore,14,26,47..." form into
    rows that match the statistics table structure "Baltimore,1790,14",
    "Baltimore,1800,26", etc.
'''

import sys
import csv

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

f = open('regions.txt','r')
dict = {'United States' : 0}
i=1
for line in f:
    line2 = line.strip()
    dict[line2] = i
    i+=1



headingRow = reader.next()[1:]

regions = {}
for row in reader:
    row = map(str.strip, row)
    assert len(row) == len(headingRow) + 1
    regions[row[0]] = row[1:]

us_totals = []
for i in range(len(headingRow)):
    us_totals.append(0)

for region in regions:
    for k in range(len(headingRow)):
        regionRow = regions[region]
        yearString = headingRow[k]
        statisticString = regionRow[k].replace(',', '') # if the CSV numbers have commas in them, delete them
        if statisticString == '' or statisticString == '--' or statisticString == '(NA)':
            statisticString = '0'
        writer.writerow([3,dict[region], yearString, statisticString])
        us_totals[k]+=float(statisticString)
for i in range(len(us_totals)):
    writer.writerow([3,0, headingRow[i], us_totals[i]])
