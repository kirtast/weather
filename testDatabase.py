import unittest
import hidden
import app_test

class TestDataBase(unittest.TestCase):

    def test_type_input(self):
        data_dict = app_test.create_dataDict_from_API()
        self.assertTrue(isinstance(data_dict, dict), 'message')

    def test_len_dict_data(self):
        data_dict = app_test.create_dataDict_from_API()
        self.assertTrue(len(data_dict) == 3, 'message')

    def test_dict_data_daily_exist(self):
        data_dict = app_test.create_dataDict_from_API()
        self.assertTrue('data_daily' in data_dict, 'message')

    def test_dict_data_hour_exist(self):
        data_dict = app_test.create_dataDict_from_API()
        self.assertTrue('data_hour' in data_dict, 'message')

    def test_dict_data_info_exist(self):
        data_dict = app_test.create_dataDict_from_API()
        self.assertTrue('data_info' in data_dict, 'message')

    def test_header_daily_columns(self):
        data_dict = app_test.create_dataDict_from_API()
        header_daily = app_test.create_header_daily(data_dict)
        self.assertTrue(len(header_daily) == 14, 'message')

    def test_data_daily_columns(self):
        data_dict = app_test.create_dataDict_from_API()
        data_daily_raw = data_dict['data_daily']
        data_daily = app_test.pull_data_daily_API(data_daily_raw)
        for row in data_daily:
            self.assertTrue(len(row) == 14, 'message')

if __name__ == '__main__':
    unittest.main()
