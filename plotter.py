import csv
from matplotlib import pyplot as plt
from matplotlib import ticker
from dataObject import DataObject

class Plotter:

    def __init__(self):
        self.data_object_mysql = DataObject('mysql_insert_test.csv')
        self.data_object_postgre = DataObject('postgre_insert_test.csv')

    def plot(self):
        # mysql = self.data_object_mysql.get_arrays(True)
        # postgre = self.data_object_postgre.get_arrays(True)

        # average_of_mysql_list = self.data_object_mysql.get_average_list()
        # average_of_postgre_list = self.data_object_postgre.get_average_list()
        #
        # max_list_of_mysql = self.data_object_mysql.get_max_values()
        # max_list_of_postgre = self.data_object_postgre.get_max_values()

        min_list_of_mysql = self.data_object_mysql.get_min_values()
        min_list_of_postgre = self.data_object_postgre.get_min_values()
        fig, ax = plt.subplots()

        plt.grid(True) #set grid
        plt.title('where-like statements/min')
        plt.xlabel('query limit')
        plt.ylabel('execution time(s)')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], min_list_of_postgre, color='r', label='postgre')
        ax.plot([1, 5000, 10000, 15000, 20000, 25000, 30000, 35000], min_list_of_mysql, color='b', label='mysql')
        #
        # ax.legend()
        # plt.title('spreiding insert statements postgre')
        # plt.hist(postgre[0], label='limit 1')
        # plt.hist(postgre[1], label='limit 5k', alpha=0.5)
        # plt.hist(postgre[2], label='limit 10k', alpha=0.5)
        # plt.hist(postgre[3], label='limit 15k', alpha=0.5)
        # plt.hist(postgre[4], label='limit 20k', alpha=0.5)
        # plt.hist(postgre[5], label='limit 25k', alpha=0.5)
        # plt.hist(postgre[6], label='limit 30k', alpha=0.5)
        # plt.hist(postgre[7], label='limit 35k', alpha=0.5)
        # plt.xlabel('executie snelheid')
        # plt.ylabel('aantal metingen')
        # plt.legend()

        # plt.title('spreiding select statements')
        # plt.boxplot(mysql[0], positions=[1,2])
        # plt.boxplot(mysql[1], positions=[4,5])
        # plt.boxplot(mysql[2], positions=[7,8])
        # plt.boxplot(mysql[3], positions=[10,11])
        # plt.boxplot(mysql[4], positions=[12,13])
        # plt.boxplot(mysql[5], positions=[15,16])
        # plt.boxplot(mysql[6], positions=[17,18])
        # plt.boxplot(mysql[7], positions=[19,20])
        # plt.xlabel('executie snelheid')
        # plt.ylabel('aantal metingen')
        # plt.legend()
        plt.show()

p = Plotter()
p.plot()
#print(p.data_object_postgre.get_min_values())
#p.get_arrays('mysql_test3.csv')

