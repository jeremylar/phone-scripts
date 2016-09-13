import csv
import os
import sys
i=0
csvin = sys.argv[1]
xmlFile = sys.argv[2]
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<YealinkIPPhoneDirectory>' + "\n")

with open(csvin, newline='') as csvFile: 
    csvData = csv.reader(csvFile, delimiter=',', skipinitialspace=True)
    for row in csvData:
        xmlData.write('<DirectoryEntry>' + "\n")
        xmlData.write('<Name>' + row[i] + '</Name>'+ "\n")
        xmlData.write('<Telephone>' + row[i+1] + '</Telephone>'+ "\n")
        xmlData.write('</DirectoryEntry>' + "\n")
xmlData.write('</YealinkIPPhoneDirectory>' + "\n")
xmlData.close()