import logging
import csv
from collections import namedtuple
from trie import Trie


logging.basicConfig(level=logging.DEBUG,
                    format="%(funcName)s:%(lineno)d:%(message)s")


def main():
    csv_filename = r"./Data/load_employees_dump.txt"
    emp_trie = Trie()
    emp_dict = {}
    with open(csv_filename, "r") as fd:
        dict_reader = csv.DictReader(fd, ['employee_id', 'birth_date', 'first_name',
                                          'last_name', 'gender', 'joining_date',
                                          'manager_id'])
        for record in dict_reader:
            emp_id = record['employee_id']
            name = record['first_name'] + '.' + record['last_name']
            mgr_id = record['manager_id']
            emp_dict[emp_id] = (emp_id, name, mgr_id)
            emp_trie.insert(name, emp_id)

    status, emp_id = emp_trie.search('Cristinel.Bouloucos')
    print(emp_dict[emp_id])
    emp_id, name, mgr_id = emp_dict[emp_id]
    print('Employee Name: {} and Manager Name: {}'.format(name,
                                                          emp_dict[mgr_id][1]))


if __name__ == '__main__':
    main()
