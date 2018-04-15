import pymysql
import time
import csv

class MySqlDatabase:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Vtl54711', db='innovatiespotter')
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        #self.limit = 5000 * 4
        self.limit = 1
        self.iteration_range = 100

    def append_data_to_csv(self):
        data_list = []
        for i in range(0, self.iteration_range):
            query = "SELECT * FROM innovatiespotter.companies limit %s;"
            start = time.time()
            self.cursor.execute(query, self.limit)
            stop = time.time()
            elapsed_time = stop - start
            data_list.append(elapsed_time)
            print(elapsed_time)

        with open('mysql_limit_{}.csv'.format(self.limit), 'a') as f:
            writer = csv.writer(f)
            for element in data_list:
                temp_list = [element]
                writer.writerow(temp_list)

    def read_csv(self):
        with open('test.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    print(row)

db = MySqlDatabase()
db.append_data_to_csv()
#db.read_csv()