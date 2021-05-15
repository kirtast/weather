import app_test

vars = app_test.create_home_loc()
url_main = app_test.create_url_API(vars['lan'],vars['API_KEY'],vars['location'])
response = app_test.get_response_API(url_main)
data = response.json()

# print(data['information'])
# for key in data:
#     print(key)
#
print(data['hour_hour'])
# print(data['day1'])
