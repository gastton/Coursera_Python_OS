import csv
import os

curPath = os.getcwd() + "/csv/"
"""
f = open(curPath + "cities.csv", "r")
csv_f = csv.reader(f)
for row in csv_f:
    LatD, LatM, LatS, NS, LonD, LonM, LonS, EW, City, State = row
    print ("City:  {}, State: {}".format(City, State))
f.close()
"""
host = [["workstation.local","192.102.33.251"],["webserver.cloud", "33.102.231.1"]]
with open(curPath + "host_file.csv","w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(host)