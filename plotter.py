import csv
from matplotlib import pyplot as plt
from matplotlib import ticker
from dataObject import DataObject

class Plotter:

    def __init__(self):
        self.data_object_mysql = DataObject('mysql_where_test3.csv')
        self.data_object_postgre = DataObject('postgre_where_test.csv')

    def plot(self):
        #average_of_mysql_list = self.data_object_mysql.get_average_list()
        #average_of_postgre_list = self.data_object_postgre.get_average_list()

        #max_list_of_mysql = self.data_object_mysql.get_max_values()
        # max_list_of_postgre = self.data_object_postgre.get_max_values()

        min_list_of_mysql = self.data_object_mysql.get_min_values()
        min_list_of_postgre = self.data_object_postgre.get_min_values()
        fig, ax = plt.subplots()

        ax.grid(True) #set grid
        plt.title('where-like statements/min')
        plt.xlabel('query limit')
        plt.ylabel('execution time(s)')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], min_list_of_postgre, color='r', label='postgre')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], min_list_of_mysql, color='b', label='mysql')

        ax.legend()
        plt.show()

p = Plotter()
p.plot()
#print(p.data_object_postgre.get_min_values())
#p.get_arrays('mysql_test3.csv')

