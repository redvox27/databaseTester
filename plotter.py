import csv

class Plotter:

    def __init__(self):
        pass

    def get_dict_from_file(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            keys = next(reader)[0].split('\t')
            postgre_dict = {}
            one_limit_list = []
            limit_5k_list = []
            limit_10k_list = []
            limit_15k_list = []

            for row in reader:
                if row:
                    temp_list = row[0].split('\t')
                    print(temp_list)
                    one_limit_list.append(temp_list[0])
                    limit_5k_list.append(temp_list[1])
                    limit_10k_list.append(temp_list[2])
                    limit_15k_list.append(temp_list[3])
            postgre_dict[keys[0]] = one_limit_list
            postgre_dict[keys[1]] = limit_5k_list
            postgre_dict[keys[2]] = limit_10k_list
            postgre_dict[keys[3]] = limit_15k_list
        return
p = Plotter()
p.get_dict_from_file('mysql_test.csv')