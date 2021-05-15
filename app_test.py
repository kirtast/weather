import requests
import json
import hidden


def create_home_loc():
    data = dict()
    key_dict = hidden.oauth()
    data['location'] = "6999"               #Rubí
    data['lan'] = "es"                      #Español
    data['API_KEY'] = key_dict["API_KEY"]   #Clave usuario
    return data

def create_url_API(lan,API_KEY,location):
    return "https://api.tutiempo.net/json/?lan=" + lan + "&apid=" + API_KEY + "&lid=" + location

def get_response_API(url_main):
    return requests.get(url_main)

def create_dataDict_from_API():
    vars = create_home_loc()
    url_main = create_url_API(vars['lan'],vars['API_KEY'],vars['location'])
    response = get_response_API(url_main)
    data = response.json()

    data_daily = list()
    data_hour = list()
    data_info = list()
    data_daily_info = list()

    data_dict=dict()

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

    data_dict['data_info'] = data_info
    data_dict['data_daily'] = data_daily
    data_dict['data_hour'] = data_hour

    return data_dict

def create_header_daily(data_dict):
    data_daily = data_dict['data_daily']

    row = data_daily[0]
    header_daily=list()

    for key in row:
        header_daily.append(key)

    return header_daily

def create_header_hour(data_dict):
    data_hour = data_dict['data_hour']
    data_hour_test=data_hour['hour1']

    header_hour=list()
    for key in data_hour_test:
        header_hour.append(key)

    return header_hour

def pull_data_daily_API(data_daily):
    row_list = list()
    data_row = list()

    for row in data_daily:
        for var in row:
            row_list.append(row[var])
        data_row.append(row_list)
        row_list = list()

    return data_row

def create_str_pull_daily_data(header_daily):
    strInsert1 = 'INSERT OR IGNORE INTO Daily('
    strInsert2 = 'VALUES ('
    data_daily_row = 'row'
    count = 1

    for head in header_daily:
        if count < len(header_daily):
            strInsert1 = strInsert1 + head + ', '
            strInsert2 = strInsert2 + '?,'
        else:
            strInsert1 = strInsert1 + head + ') '
            strInsert2 = strInsert2 + '?)'
        count = count + 1

    strExe = strInsert1+strInsert2

    return strExe

if __name__ == '__main__':
    main()
