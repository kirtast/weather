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

if __name__ == '__main__':
    main()
