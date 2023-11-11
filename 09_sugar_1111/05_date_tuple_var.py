dates = ["2023-11-11 GMT3 17:15", "2023-11-10 GMT5 10:01",
        "2023-07-15 GMT11 23:45", "2022-08-11 GMT11 00:15",
        "2017-05-31 11:00"]


for i in range(len(dates)):
        date, time = dates[i][:10], dates[i][-5:]
        dates[i] = date + ' ' + time

print(dates)

