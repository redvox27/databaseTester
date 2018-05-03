import pymysql
import time
import csv
from dummyData import DummyDataGenerator

class MySqlDatabase:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Vtl54711', db='innovatiespotter')
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

        self.test_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Vtl54711', db='test')
        self.test_cursor = self.test_db.cursor(cursor=pymysql.cursors.DictCursor)

        self.limit = 5000 * 3
        # self.limit = 1
        self.iteration_range = 100
        self.dummy = DummyDataGenerator()
        self.max_range = 5

    def append_data_to_csv(self):
        data_list = []
        while len(data_list) != self.iteration_range:
            query = "SELECT * FROM test.companies limit %s;"
            start = time.time()
            self.cursor.execute(query, self.limit)
            stop = time.time()
            elapsed_time = stop - start
            if elapsed_time != 0.0:
                data_list.append(elapsed_time)
                print(elapsed_time)
        print(len(data_list))
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

    def test_select_statements(self):
        data_dict = {}
        for i in range(0, 8):
            data_list = []
            if i == 0:
                limit = 1
            else:
                limit = 5000 * i
            while len(data_list) != 100:
                #query = "SELECT * FROM innovatiespotter.companies where projectomschrijving like '{}' limit {}".format('%is%', limit)
                query = "SELECT * FROM innovatiespotter.companies limit {}".format(limit)
                start = time.time()
                self.cursor.execute(query)
                stop = time.time()
                elapsed_time = stop - start
                if elapsed_time != 0.0:
                    data_list.append(elapsed_time)
                    print(elapsed_time)
            data_dict[limit] = data_list
            print(data_dict)
        keys = sorted(data_dict.keys())

        with open('mysql_select_test.csv', 'a') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(keys)
            writer.writerows(zip(*[data_dict[key] for key in keys]))

    def insert_dummy_data(self):
        for i in range(0, 20000):
            rijksbijdrage = self.dummy.generate_random_string(5)
            subsidie = self.dummy.generate_random_string(6)
            status = self.dummy.generate_random_string(5)
            jaar = self.dummy.generate_random_string(4)
            projectnummer = self.dummy.generate_random_string(10)
            aanvrager = self.dummy.generate_random_string(30)
            project_partner = self.dummy.generate_random_string(30)
            project_omschrijving = self.dummy.generate_random_string(300)
            location = self.dummy.generate_random_string(25)

            query = "insert into innovatiespotter.companies (aanvrager, rijksbijdrage, locatie, subsidie, status, jaar, projectnummer, projectpartner, projectomschrijving)" \
                    "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (
            aanvrager, rijksbijdrage, location, subsidie, status, jaar, projectnummer, project_partner,
            project_omschrijving))
            self.db.commit()
            print(i)


    def test_insert_statements(self):
        limit = 8
        data_dict = {}
        interval_list = [1, 5000, 10000, 15000, 20000, 25000, 30000, 35000]
        #interval_list = [15000]
        for interval in interval_list:
            print(interval)
            string = "insert into test.companies(aanvrager, rijksbijdrage, locatie, subsidie, status, jaar, projectnummer, projectpartner, projectomschrijving) VALUES "
            date_list = []
            for i in range(0, interval):

                rijksbijdrage = self.dummy.generate_random_string(5)
                subsidie = self.dummy.generate_random_string(6)
                status = self.dummy.generate_random_string(5)
                jaar = self.dummy.generate_random_string(4)
                projectnummer = self.dummy.generate_random_string(10)
                aanvrager = self.dummy.generate_random_string(30)
                project_partner = self.dummy.generate_random_string(30)
                project_omschrijving = self.dummy.generate_random_string(300)
                location = self.dummy.generate_random_string(25)

                string += '('
                string += "'{}'".format(aanvrager) + ',' + "'{}'".format(rijksbijdrage) + ',' + "'{}'".format(location) + ',' + "'{}'".format(subsidie) + ',' + "'{}'".format(status) + ',' + "'{}'".format(jaar) + ',' + "'{}'".format(projectnummer) + ',' + "'{}'".format(project_partner) + ',' + "'{}'".format(project_omschrijving)
                string += ')'

                if interval != 1:
                    string += ','

            if interval > 1:
                query = string[:len(string)-1]
            else:
                query = string
            print(query)
            print('\n')
            while len(date_list) != 100:
                print(len(date_list))
                start = time.time()
                self.test_cursor.execute('set global max_allowed_packet=268435456')#32mb(in bits)
                self.test_cursor.execute(query)
                self.test_db.commit()
                stop = time.time()
                elapsed_time = stop - start
                if elapsed_time != 0.0:
                    date_list.append(elapsed_time)
                self.test_cursor.execute('truncate test.companies')

            data_dict[interval] = date_list

        keys = sorted(data_dict.keys())

        with open('mysql_insert_test.csv', 'a') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(keys)
            writer.writerows(zip(*[data_dict[key] for key in keys]))

db = MySqlDatabase()
#db.test_insert_statements()
db.test_select_statements()
#db.insert_dummy_data()
#db.append_data_to_csv()
#db.read_csv()