# Employee Trie
Python program to insert and search employees in a Trie using a combination of first and last names.
The employee data is taken from [datacharmer testdb](https://github.com/datacharmer/test_db/).

## Diagram
Code:
```
emp_trie = Trie()
emp_trie.insert('johnd', 11111)
emp_trie.insert('a')
```
![Alt text](Employee_Trie/Data/emp_trie.png?raw=true "Employee Trie Objects")

### ToDo
- [ ] Separating functions for constructing employee trie
- [ ] Writing more tests to uncover edge cases
- [ ] Validating employee trie constructed from 300024 employee data
- [ ] Code for constructing unique usernames from employee data