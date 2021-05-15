import sqlite3
import app_test
import json

conn=sqlite3.connect('DB_weather.sqlite')
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Daily;
DROP TABLE IF EXISTS Hour_Data;
DROP TABLE IF EXISTS InfoMeasures;
DROP TABLE IF EXISTS Daily_Info;
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

#data_daily = json.loads(data_daily)
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

print(data_info)
str='CREATE TABLE InfoMeasures(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Measure TEXT UNIQUE, Unit TEXT UNIQUE)'
cur.execute(str)

# for key in data_info:
#     print(data_info[key],key)
# row = data_info[0]
# header_info=list()
#
# for key in row:
#     header_info.append(key)
#
# print(header_info)

# cur.executescript('''
# CREATE TABLE Daily(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,prio TEXT UNIQUE);
# CREATE TABLE Hour_Data(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT UNIQUE);
# CREATE TABLE Null_essay(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,EType TEXT UNIQUE);
# CREATE TABLE Project(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,project TEXT UNIQUE);
# CREATE TABLE State(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,state TEXT UNIQUE);
# CREATE TABLE CodError(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Code TEXT UNIQUE,Description TEXT);
# CREATE TABLE Category(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,category TEXT UNIQUE);
# CREATE TABLE Device(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,device TEXT UNIQUE,category_id INTEGER);
# CREATE TABLE SerialNumber(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,serialnumber TEXT UNIQUE,device_id INTEGER,category_id INTEGER);
# '''
# )
# #cur.execute('SELECT Track.title, Album.title, Artist.name, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id=Genre.id AND Track.album_id=Album.id AND Album.artist_id=Artist.id')
#
# root = tk.Tk()
# root.withdraw()
# #Show a dialog to select the database
# file_path = filedialog.askopenfilename()
# xl = pd.ExcelFile(file_path)
# sheet_names=xl.sheet_names
# #Create a DataFrame with the spreadsheet 1
# xlFrame=xl.parse(sheet_names[0])
#
# #Identify the position of each column name
# Heads=xlFrame.head(1).columns.values
# for idx, head in enumerate(Heads):
#     if head=="Operario":
#         col_op=idx
#     if head=="Prios":
#         col_prio=idx
#     if head=="Categoría":
#         col_cat=idx
#     if head=="Equipo":
#         col_eq=idx
#     if head=="Referencia":
#         col_ref=idx
#
# #Get the values of each column name
# operarios_raw=xlFrame.iloc [:,[col_op]]
# prioridades_raw=xlFrame.iloc [:,[col_prio]]
# categorias_raw=xlFrame.iloc [:,[col_cat]]
# equipos_raw=xlFrame.iloc [:,[col_eq]]
# serialnumber_raw=xlFrame.iloc [:,[col_ref]]
#
# #Clean from NaN values and create a list
# operarios=operarios_raw[operarios_raw['Operario'].notnull()].values
# prioridades=prioridades_raw[prioridades_raw['Prios'].notnull()].values
# categorias=categorias_raw[categorias_raw['Categoría'].notnull()].values
# equipos=equipos_raw[equipos_raw['Equipo'].notnull()].values
# serialnumber=serialnumber_raw[serialnumber_raw['Referencia'].notnull()].values
#
#
# cur.execute('INSERT OR IGNORE INTO Null_essay(EType) VALUES (?)',('Sí',))
# cur.execute('INSERT OR IGNORE INTO Null_essay(EType) VALUES (?)',('No',))
# cur.execute('INSERT OR IGNORE INTO Null_essay(EType) VALUES (?)',('--',))
# projects=list()
# for i in range(120):
#     if i+80<100:
#         projects.append('SEA00'+str(i+80))
#     else:
#         projects.append('SEA0'+str(i+80))
#
# for proj in projects:
#     cur.execute('INSERT OR IGNORE INTO Project(project) VALUES (?)',(proj,))
# cur.execute('INSERT OR IGNORE INTO Project(project) VALUES (?)',('--',))
#
# cur.execute('INSERT OR IGNORE INTO State(state) VALUES (?)',('ABIERTO',))
# cur.execute('INSERT OR IGNORE INTO State(state) VALUES (?)',('CERRADO',))
# cur.execute('INSERT OR IGNORE INTO State(state) VALUES (?)',('--',))
#
# for prios in prioridades.tolist():
#     cur.execute('INSERT OR IGNORE INTO Priority(prio) VALUES (?)',(prios[0],))
# cur.execute('INSERT OR IGNORE INTO Priority(prio) VALUES (?)',('--',))
# for operario in operarios.tolist():
#     cur.execute('INSERT OR IGNORE INTO Operator(name) VALUES (?)',(operario[0],))
# cur.execute('INSERT OR IGNORE INTO Operator(name) VALUES (?)',('--',))
#
# for idx,entry in enumerate(serialnumber.tolist()):
#     cur.execute('INSERT OR IGNORE INTO Category(category) VALUES (?)',(categorias[idx][0],))
#     cur.execute('SELECT id FROM Category WHERE category=?',(categorias[idx][0],))
#     category_id=cur.fetchone()[0]
#     cur.execute('INSERT OR IGNORE INTO Device(device,category_id) VALUES (?,?)',(equipos[idx][0],category_id,))
#     cur.execute('SELECT id FROM Device WHERE device=?',(equipos[idx][0],))
#     device_id=cur.fetchone()[0]
#     cur.execute('INSERT OR IGNORE INTO SerialNumber(serialnumber,device_id,category_id) VALUES (?,?,?)',(serialnumber[idx][0],device_id,category_id,))
#
#
# cur.execute('INSERT OR IGNORE INTO Category(category) VALUES (?)',('--',))
# cur.execute('SELECT id FROM Category WHERE category=?',('--',))
# category_id=cur.fetchone()[0]
# cur.execute('INSERT OR IGNORE INTO Device(device,category_id) VALUES (?,?)',('--',category_id,))
# cur.execute('SELECT id FROM Device WHERE device=?',('--',))
# device_id=cur.fetchone()[0]
# cur.execute('INSERT OR IGNORE INTO SerialNumber(serialnumber,device_id,category_id) VALUES (?,?,?)',('--',device_id,category_id,))
#
#
#     #print(idx,categorias[idx][0],equipos[idx][0],serialnumber[idx][0])
# xlFrame=xl.parse(sheet_names[1])
# colCod=0
# colDesc=1
# #Get the values of each column name
# Cod_raw=xlFrame.iloc [:,[colCod]]
# Desc_raw=xlFrame.iloc [:,[colDesc]]
# Cod=Cod_raw[Cod_raw['Código'].notnull()].values
# Desc=Desc_raw[Desc_raw['Descripción'].notnull()].values
#
# for idx,entry in enumerate(Cod.tolist()):
#     cur.execute('INSERT OR IGNORE INTO CodError(Code,Description) VALUES (?,?)',(Cod[idx][0],Desc[idx][0],))
conn.commit()
cur.close()
