# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:59:41 2020

@author: RAM PARAM
"""


from pymongo import MongoClient
import csv
from datetime import datetime
import time

cluster_client=MongoClient("mongodb+srv://tempdata:tempdata@tempdataset.rttjq.mongodb.net/tempdataset?retryWrites=true&w=majority")
#print(client.list_database_names())
db = cluster_client["tempdataset"]
col = db["tempdata_2015"]


csv_file=open("./inn.txt","r")
csv_reader = csv.reader(csv_file, delimiter=',')
#print(type(csv_reader))
#temp = 0
for row in csv_reader:
    date_time_str = row[1]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    #print(row[0], datetime.now(), row[1])
    sensor_number = row[0]
    temperature = row[1]
    document = {"sensor": sensor_number, "datetime":date_time_obj, "temperature":row[2]}
    col.insert_one(document)
    #print("sending ....")
    #time.sleep(1)
    #temp+=1
    #if temp == 3:
     #   break


#print(db.list_collection_names())
#csv_file=open("./datatset1 - copy.txt","r")
#csv_reader = csv.reader(csv_file, delimiter=',')
#for row in csv_reader:
    
#document = {"name": "ram"}
#col.insert_one(document)
#print(col.find_one())