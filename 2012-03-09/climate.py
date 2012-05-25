import csv
import sqlite3 as sqlite
import numpy as np
import matplotlib.pyplot as plt

import getfile

csvfile = open(getfile.get_from_strawlab("week1/CTS.csv"),'rb')
con = sqlite.connect(':memory:')

with con and csvfile:
    csv = csv.reader(csvfile)
    cur = con.cursor()
    cur.execute("CREATE TABLE CTS(date INTEGER PRIMARY KEY, co2 FLOAT, temp FLOAT);")

    header = csv.next() #save the csv header row
    idx_date = header.index("yr_mn")
    idx_co2 = header.index("CO2")
    idx_temp = header.index("GISS")
    for row in csv:
        cur.execute("INSERT INTO CTS VALUES (?,?,?)", (row[idx_date],row[idx_co2],row[idx_temp]) )

    cur.execute("SELECT date, co2 FROM cts WHERE co2 != 'NA'")
    data = np.array(cur.fetchall())

    plt.plot(data[:,0],data[:,1])
    plt.xlabel("date"); plt.ylabel("CO2 (ppm)")
    plt.show()

