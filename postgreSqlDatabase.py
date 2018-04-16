import psycopg2
import time
import csv

class MySqlDatabase:

    def __init__(self):
        self.postgre = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='vtl54711')
        self.cursor = self.postgre.cursor()
        self.limit = 5000 * 3
        # self.limit = 1
        self.iteration_range = 100

    def append_data_to_csv(self):
        data_list = []
        while len(data_list) != self.iteration_range :
            query = "SELECT * FROM innovatiespotter.companies limit %s;"
            start = time.time()
            self.cursor.execute(query, [self.limit])
            stop = time.time()
            elapsed_time = stop - start
            if elapsed_time != 0.0:
                data_list.append(elapsed_time)
                print(elapsed_time)
        print(len(data_list))

        with open('postgre_limit_{}.csv'.format(self.limit), 'a') as f:
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

    def test(self):
        data_dict = {}
        for i in range(0, 4):
            data_list = []
            if i == 0:
                limit = 1
            else:
                limit = 5000 * i
            while len(data_list) != 100:
                query = "SELECT * FROM innovatiespotter.companies limit %s;"
                start = time.time()
                self.cursor.execute(query, [limit])
                stop = time.time()
                elapsed_time = stop - start
                if elapsed_time != 0.0:
                    data_list.append(elapsed_time)
                    print(elapsed_time)
            data_dict[limit] = data_list
        keys = sorted(data_dict.keys())

        with open('postgre_test.csv'.format(self.limit), 'a') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(keys)
            writer.writerows(zip(*[data_dict[key] for key in keys]))

db = MySqlDatabase()
#db.append_data_to_csv()
#db.read_csv()
db.test()