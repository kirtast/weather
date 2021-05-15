import sqlite3
import app_test

# def DB_insert_daily_data():
#     data_dict = app_test.create_dataDict_from_API()
#     data_daily_raw = data_dict['data_daily']
#     data_daily = app_test.pull_data_daily_API(data_daily_raw)
#     header_daily = app_test.create_header_daily(data_dict)
#
#     strExe = app_test.create_str_pull_daily_data(header_daily)
#
#     conn=sqlite3.connect('DB_weather.sqlite')
#     cur=conn.cursor()
#
#     for row in data_daily:
#         cur.execute(strExe,tuple(row))
#
#     conn.commit()
#     cur.close()


data_dict = app_test.create_dataDict_from_API()
data_hour_raw = data_dict['data_hour']
header_hour = app_test.create_header_hour(data_dict)

print(header_hour)
# strExe = app_test.create_str_pull_daily_data(header_daily)
#
# conn=sqlite3.connect('DB_weather.sqlite')
# cur=conn.cursor()
#
# for row in data_daily:
#     cur.execute(strExe,tuple(row))
#
# conn.commit()
# cur.close()

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
