# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:33:42 2020

@author: RAM PARAM
"""


import csv
from datetime import datetime

csv_file=open("./datatest.txt","r")
csv_reader = csv.reader(csv_file, delimiter=',')
writer = csv.writer(open('inno.txt', 'w', newline=''))
for row in csv_reader:
   sensor = int(row[0])%7
   writer.writerow([sensor, row[2]])

csv_file=open("./datatset1 - copy.txt","r")
csv_reader = csv.reader(csv_file, delimiter=',')
writer = csv.writer(open('inno.txt', 'a', newline=''))
for row in csv_reader:
   sensor = int(row[0])%7
   writer.writerow([sensor, row[2]])
   

csv_file=open("./datatest2 - Copy.txt","r")
csv_reader = csv.reader(csv_file, delimiter=',')
writer = csv.writer(open('inno.txt', 'a', newline=''))
for row in csv_reader:
   sensor = int(row[0])%7
   writer.writerow([sensor, row[2]])