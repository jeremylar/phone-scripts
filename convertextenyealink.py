#python script that takes in a csv file as first arg and exports xml as as second arg
#csv first column is name, second column is phone number
import csv
import os
import sys
i=0
csvin = sys.argv[1] #location of csv to import
xmlFile = sys.argv[2] #location and name of xml to create
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<YealinkIPPhoneDirectory>' + "\n")

with open(csvin, newline='') as csvFile: 
    csvData = csv.reader(csvFile, delimiter=',', skipinitialspace=True)
    for row in csvData:
        xmlData.write('<DirectoryEntry>' + "\n")
        xmlData.write('<Name>' + row[i] + '</Name>'+ "\n")
        xmlData.write('<Telephone>' + row[i+1].strip() + '</Telephone>'+ "\n")
        xmlData.write('</DirectoryEntry>' + "\n")
xmlData.write('</YealinkIPPhoneDirectory>' + "\n")
xmlData.close()
