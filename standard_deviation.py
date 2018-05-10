from dataObject import DataObject

mysql = DataObject('mysql_select_test.csv')
postgre = DataObject('postgre_test3.csv')

print(mysql.get_q1_q3())
print(postgre.get_q1_q3())