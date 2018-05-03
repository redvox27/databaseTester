import csv

class DataObject:

    def __init__(self, file_name):
        self.file = open(file_name)

    def get_dict_from_file(self):

        reader = csv.reader(self.file)
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

    def get_arrays(self, in_array=False):
        postgre_data_dict = self.get_dict_from_file()
        key_list = list(postgre_data_dict.keys())
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

        if in_array:
            return [limit_1_array, limit_5000_array, limit_10000_array, limit_15000_array, limit_20000_array, limit_25000_array, limit_30000_array, limit_35000_array]
        else:
            return limit_1_array, limit_5000_array, limit_10000_array, limit_15000_array, limit_20000_array, limit_25000_array, limit_30000_array, limit_35000_array

    def get_average_list(self):
        limit_1_array, limit_5000_array, limit_10000_array, limit_15000_array, limit_20000_array, limit_25000_array, limit_30000_array, limit_35000_array = self.get_arrays()

        limit_1_average = sum(limit_1_array) / len(limit_1_array)
        limit_5000_average = sum(limit_5000_array) / len(limit_5000_array)
        limit_10000_average = sum(limit_10000_array) / len(limit_10000_array)
        limit_15000_average = sum(limit_15000_array) / len(limit_15000_array)
        limit_25000_average = sum(limit_25000_array) / len(limit_25000_array)
        limit_30000_average = sum(limit_30000_array) / len(limit_30000_array)
        limit_20000_average = sum(limit_20000_array) / len(limit_20000_array)
        limit_35000_average = sum(limit_35000_array) / len(limit_35000_array)

        return [limit_1_average, limit_5000_average, limit_10000_average, limit_15000_average, limit_20000_average,
                limit_25000_average, limit_30000_average, limit_35000_average]

    def get_keys(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            keys = next(reader)[0].split('\t')
            return (keys)

    def get_max_values(self):
        arrays = self.get_arrays(True)
        max_array = []

        for array in arrays:
            max_array.append(max(array))
        return max_array

    def get_min_values(self):
        arrays = self.get_arrays(True)
        min_array = []

        for array in arrays:
            min_array.append(min(array))
        return min_array