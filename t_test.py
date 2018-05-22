from dataObject import DataObject
import scipy.stats as stats
import numpy as np

class Ttest:

    def __init__(self):
        self.mysql_data_object = DataObject('mysql_where_test3.csv')
        self.postgre_data_object = DataObject('postgre_where_test.csv')

    def get_arrays(self, index=0):
        print('retrieving lists....')
        mysql_array_list = self.mysql_data_object.get_arrays(in_array=True)
        postgre_sql_list = self.postgre_data_object.get_arrays(in_array=True)

        return mysql_array_list[index], postgre_sql_list[index]

    def get_t_value(self):

        mysql_array, postgre_array = self.get_arrays(7)
        print(mysql_array)
        t_statistics, p_value = stats.ttest_ind(mysql_array, postgre_array)

        p_value = np.asscalar(p_value)
        p_value = format(p_value, '.15f')
        print('p-value: {}'.format(p_value))

        print(t_statistics)

        if float(p_value) > 0.05 or float(p_value) > 0.1:
            return False #null hypothese kan niet verworpen worden
        else:
            return True #null hypothese kan verworpen worden

    def calculate_average_of_database(self):
        mysql_array_list = self.mysql_data_object.get_arrays()
        postgre_array_list = self.postgre_data_object.get_arrays()
        mysql_average_list = []
        postgre_average_list = []

        for array in mysql_array_list:
            avg = sum(array) / len(array)
            mysql_average_list.append(avg)

        for array in postgre_array_list:
            avg = sum(array) / len(array)
            postgre_average_list.append(avg)

        mysql_average_of_average_list = sum(mysql_average_list) / len(mysql_average_list)
        postgre_average_of_average_list = sum(postgre_average_list) / len(postgre_average_list)
        print(mysql_average_of_average_list)
        print(postgre_average_of_average_list)

t = Ttest()
t.calculate_average_of_database()
#t.get_t_value()