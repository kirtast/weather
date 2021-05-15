import sqlite3
import app_test
import json

conn=sqlite3.connect('DB_weather.sqlite')
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Daily;
DROP TABLE IF EXISTS Hour_Data;
DROP TABLE IF EXISTS InfoMeasures;
DROP TABLE IF EXISTS InfoMeasuresHour;
'''
)

vars = app_test.create_home_loc()
url_main = app_test.create_url_API(vars['lan'],vars['API_KEY'],vars['location'])
response = app_test.get_response_API(url_main)
data = response.json()

data_daily = list()
data_hour = list()
data_info = list()
data_daily_info = list()

keys = list()
for key in data:
    if not key=='copyright' and not key=='web' and not key=='language' and not key=='locality' and not key=='use':
        keys.append(key)
for key in keys:
    if key=='information':
        data_info=data[key]
    elif key=='day1' or key=='day2' or key=='day3' or key=='day4' or key=='day5' or key=='day6' or key=='day7':
        data_daily.append(data[key])
    elif key == 'hour_hour':
        data_hour=data[key]

#===============================================================================
#=================== APARTADO DE DAILY =========================================
#===============================================================================
row = data_daily[0]
header_daily=list()

for key in row:
    header_daily.append(key)

type_header=list()
for head in header_daily:
    if head == 'date':
        type_header.append('DATE')
    elif head.find('temperature')>-1:
        type_header.append('REAL')
    elif head == 'humidity':
        type_header.append('REAL')
    elif head == 'wind':
        type_header.append('REAL')
    else:
        type_header.append('TEXT')

tup_daily = list(zip(header_daily, type_header))
str_daily = 'CREATE TABLE Daily(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, '

count = 1
for pair in tup_daily:
    if count < len(tup_daily):
        str_daily = str_daily + pair[0] + ' ' + pair[1] + ', '
    else:
        str_daily = str_daily + pair[0] + ' ' + pair[1] + ')'
    count = count + 1

#print(str_daily)
cur.execute(str_daily)

#===============================================================================
#=================== APARTADO DE InfoMeasures ==================================
#===============================================================================
str='CREATE TABLE InfoMeasures(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Measure TEXT UNIQUE, Unit TEXT)'
cur.execute(str)
for key in data_info:
    cur.execute(app_test.create_str_pull_info_data(data_info),tuple([key,data_info[key]]))
#===============================================================================
#=================== APARTADO DE HOURS =========================================
#===============================================================================

data_hour_test=data_hour['hour1']

header_hour=list()
for key in data_hour_test:
    header_hour.append(key)

type_header=list()
for head in header_hour:
    if head == 'date':
        type_header.append('DATE')
    elif head.find('temperature')>-1:
        type_header.append('REAL')
    elif head == 'humidity':
        type_header.append('REAL')
    elif head == 'pressure':
        type_header.append('REAL')
    elif head == 'wind':
        type_header.append('REAL')
    else:
        type_header.append('TEXT')

tup_hour = list(zip(header_hour, type_header))
str_hour = 'CREATE TABLE Hour_Data(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, '
count = 1
for pair in tup_hour:
    if count < len(tup_hour):
        str_hour = str_hour + pair[0] + ' ' + pair[1] + ', '
    else:
        str_hour = str_hour + pair[0] + ' ' + pair[1] + ')'
    count = count + 1

cur.execute(str_hour)

#===============================================================================
#=================== APARTADO DE InfoMeasuresHour ==============================
#===============================================================================
str='CREATE TABLE InfoMeasuresHour(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,MeasureName TEXT UNIQUE, IndexMeasure INTEGER)'
cur.execute(str)


conn.commit()
cur.close()
