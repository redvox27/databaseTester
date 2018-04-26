import csv
from matplotlib import pyplot as plt
from matplotlib import ticker
from dataObject import DataObject

class Plotter:

    def __init__(self):
        self.data_object = DataObject()

    def get_arrays(self, file_name):
        postgre_data_dict = self.data_object.get_dict_from_file(file_name)
        key_list = list(postgre_data_dict.keys())
        print(key_list)
        limit_1_array = postgre_data_dict[key_list[0]]
        limit_5000_array = postgre_data_dict[key_list[1]]
        limit_10000_array = postgre_data_dict[key_list[2]]
        limit_15000_array = postgre_data_dict[key_list[3]]
        limit_20000_array = postgre_data_dict[key_list[4]]
        limit_25000_array = postgre_data_dict[key_list[5]]
        limit_30000_array = postgre_data_dict[key_list[6]]
        limit_35000_array = postgre_data_dict[key_list[7]]

        limit_1_array = [float(i) for i in limit_1_array]
        limit_5000_array = [float(i) for i in limit_5000_array]
        limit_10000_array = [float(i) for i in limit_10000_array]
        limit_15000_array = [float(i) for i in limit_15000_array]
        limit_20000_array = [float(i) for i in limit_20000_array]
        limit_25000_array = [float(i) for i in limit_25000_array]
        limit_30000_array = [float(i) for i in limit_30000_array]
        limit_35000_array = [float(i) for i in limit_35000_array]

        print(limit_1_array)
        print(limit_5000_array)
        print(limit_10000_array)
        print(limit_15000_array)
        print(limit_20000_array)
        print(limit_25000_array)
        print(limit_30000_array)
        print(limit_35000_array)

        return limit_1_array, limit_5000_array, limit_10000_array, limit_15000_array, limit_20000_array, limit_25000_array, limit_30000_array, limit_35000_array

    def get_average_list(self, file_name):
        limit_1_array, limit_5000_array, limit_10000_array, limit_15000_array, limit_20000_array, limit_25000_array, limit_30000_array, limit_35000_array = self.get_arrays(file_name)

        limit_1_average = sum(limit_1_array) / len(limit_1_array)
        limit_5000_average = sum(limit_5000_array) / len(limit_5000_array)
        limit_10000_average = sum(limit_10000_array) / len(limit_10000_array)
        limit_15000_average = sum(limit_15000_array) / len(limit_15000_array)
        limit_25000_average = sum(limit_25000_array) / len(limit_25000_array)
        limit_30000_average = sum(limit_30000_array) / len(limit_30000_array)
        limit_20000_average = sum(limit_20000_array) / len(limit_20000_array)
        limit_35000_average = sum(limit_35000_array) / len(limit_35000_array)

        return [limit_1_average, limit_5000_average, limit_10000_average, limit_15000_average, limit_20000_average, limit_25000_average, limit_30000_average, limit_35000_average]


    def plot(self):
        average_of_postgre_list = self.get_average_list('postgre_where_test.csv')
        average_of_mysql_list = self.get_average_list('mysql_where_test3.csv')

        keys = self.data_object.get_keys('mysql_test2.csv')
        print('keys: ', str(keys))

        fig, ax = plt.subplots()


        ax.grid(True) #set grid

        plt.xlabel('query limit')
        plt.ylabel('execution time')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], average_of_postgre_list, color='r', label='postgre')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], average_of_mysql_list, color='b', label='mysql')

        ax.legend()
        plt.show()

p = Plotter()
p.plot()
#p.get_arrays('mysql_test3.csv')

