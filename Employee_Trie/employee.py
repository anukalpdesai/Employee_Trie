import logging
from trie import Trie


logging.basicConfig(level=logging.DEBUG,
                    format="%(funcName)s:%(lineno)d:%(message)s")


class Employee:

    def __init__(self, employee_id, birth_date, first_name, last_name, gender,
                 joining_date, manager_id):

        self.employee_id = employee_id
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.joining_date = joining_date
        self.manager_id = manager_id


def main():
    emp_dict = {}
    emp_trie = Trie()

    try:
        fd = open(r"./Data/load_employees_dump.txt", "r")
    except IOError as e:
        logging.error("Unable to open file: %s", e)
    else:
        for line in fd:
            emp_id, dob, fname, lname, gender, doj, mgr_id = line.rstrip('\r\n').split(',')
            emp_dict[emp_id] = Employee(emp_id, dob, fname, lname, gender, doj, mgr_id)
            emp_trie.insert(fname+'.'+lname, emp_id)

        status, emp_id = emp_trie.search('Cristinel.Bouloucos')
        logging.info('status = %s, id = %s', status, emp_id)
        emp1 = emp_dict[emp_id]
        print('Employee Name : ' + emp1.first_name)
        emp2 = emp_dict[emp1.manager_id]
        print('Manemp2.first_name)


if __name__ == '__main__':
    main()
