import csv

class DataObject:

    def get_dict_from_file(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            keys = next(reader)[0].split('\t')
            postgre_dict = {}
            one_limit_list = []
            limit_5k_list = []
            limit_10k_list = []
            limit_15k_list = []
            limit_20k_list = []
            limit_25k_list = []
            limit_30k_list = []
            limit_35k_list = []



            for row in reader:
                if row:
                    temp_list = row[0].split('\t')
                    one_limit_list.append(temp_list[0])
                    limit_5k_list.append(temp_list[1])
                    limit_10k_list.append(temp_list[2])
                    limit_15k_list.append(temp_list[3])
                    limit_20k_list.append(temp_list[4])
                    limit_25k_list.append(temp_list[5])
                    limit_30k_list.append(temp_list[6])
                    limit_35k_list.append(temp_list[7])

            postgre_dict[keys[0]] = one_limit_list
            postgre_dict[keys[1]] = limit_5k_list
            postgre_dict[keys[2]] = limit_10k_list
            postgre_dict[keys[3]] = limit_15k_list
            postgre_dict[keys[4]] = limit_20k_list
            postgre_dict[keys[5]] = limit_25k_list
            postgre_dict[keys[6]] = limit_30k_list
            postgre_dict[keys[7]] = limit_35k_list

        return postgre_dict

    def get_keys(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            keys = next(reader)[0].split('\t')
            print((keys))
            return (keys)
