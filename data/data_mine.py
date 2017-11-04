from datetime import datetime
import csv
import pickle

d = dict()
with open("atlantic.csv") as file:
    reader = csv.reader(file, delimiter=',')
    # First row
    first_row = reader.__next__()
    print(first_row)
    print(reader.__next__()[0])

    for row in reader:
        ID = row[0]

        year = int(row[2][:4])
        month = int(row[2][4:6])
        day = int(row[2][6:8])
        hour = int(row[3]) // 100
        date = datetime(year=year, month=month, day=day, hour=hour)

        if row[6][-1] == "N":
            lat = float(row[6][:-1])
        elif row[6][-1] == "S":
            lat = float(row[6][:-1]) * -1
        else:
            print("Bad data")

        if row[7][-1] == "W":
            long = float(row[7][:-1])
        elif row[7][-1] == "E":
            long = float(row[7][:-1]) * -1
        else:
            print("Bad data")
        
        wind = int(row[8])

        lst = (date, lat, long, wind)

        if ID in d.keys():
            d[ID].append(lst)
        else:
            d[ID] = [lst]
        
with open("history_data.pickle", "wb") as file:
    pickle.dump(d, file)
    