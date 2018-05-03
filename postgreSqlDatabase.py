import psycopg2
import time
import csv
from dummyData import DummyDataGenerator

class MySqlDatabase:

    def __init__(self):
        self.postgre = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='vtl54711')
        self.cursor = self.postgre.cursor()
        self.limit = 5000 * 3
        # self.limit = 1
        self.iteration_range = 100
        self.dummy = DummyDataGenerator()

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
        keys = sorted(data_dict.keys())

        with open('postgre_test3.csv'.format(self.limit), 'a') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(keys)
            writer.writerows(zip(*[data_dict[key] for key in keys]))

    def test_insert_statements(self):
        limit = 8
        data_dict = {}
        interval_list = [1, 5000, 10000, 15000, 20000, 25000, 30000, 35000]
        # interval_list = [15000]
        index = 0
        for interval in interval_list:
            print(interval)
            string = "insert into innovatiespotter.companies(subsidie, status, rijksbijdrage, projectpartner, projectnummer, locatie, jaar, id , aanvrager, projectomschrijving) VALUES "
            date_list = []
            for i in range(0, interval):
                index +=1
                index_string = str(index)
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
                string += "'{}'".format(subsidie) + ',' + "'{}'".format(status) + ',' + "'{}'".format(
                    rijksbijdrage) + ',' + "'{}'".format(project_partner) + ',' + "'{}'".format(projectnummer) + ',' + "'{}'".format(
                    location) + ',' + "'{}'".format(jaar) + ',' + "'{}'".format(
                    index_string) + ',' + "'{}'".format(aanvrager) + ',' + "'{}'".format(project_omschrijving)
                string += ')'
                # todo kijk naar i of naar interval
                # todo komma die komt of niet op de juiste plek(error zit bij meer dan 1)
                if interval != 1:
                    string += ','

            if interval > 1:
                query = string[:len(string) - 1]
            else:
                query = string
            print(query)
            print('\n')
            while len(date_list) != 100:
                print(len(date_list))
                start = time.time()
                #self.cursor.execute('set global max_allowed_packet=268435456')  # 32mb(in bits)
                self.cursor.execute(query)
                self.postgre.commit()
                stop = time.time()
                elapsed_time = stop - start
                if elapsed_time != 0.0:
                    date_list.append(elapsed_time)
                self.cursor.execute('truncate innovatiespotter.companies')

            data_dict[interval] = date_list

        keys = sorted(data_dict.keys())

        with open('postgre_insert_test.csv', 'a') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(keys)
            writer.writerows(zip(*[data_dict[key] for key in keys]))

db = MySqlDatabase()
#db.append_data_to_csv()
# db.read_csv()
db.test()
#db.test_insert_statements()