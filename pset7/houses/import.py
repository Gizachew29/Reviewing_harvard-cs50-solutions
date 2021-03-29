import csv
from sys import argv, exit
from cs50 import SQL


if len(argv) != 2:
    exit()

db = SQL("sqlite:///students.db")

with open(argv[1], "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name_arr = row['name'].split(" ")
        
        

        if len(name_arr) < 3:
            first_name = name_arr[0]
            last_name = name_arr[1]
            middle_name = None
            
            
        else:
            first_name = name_arr[0]
            last_name = name_arr[2]
            middle_name = name_arr[1]
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first_name, middle_name, last_name, row['house'], row['birth'])
        

# CREATE TABLE students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first VARCHAR(255),
#     middle VARCHAR(255),
#     last VARCHAR(255),
#     house VARCHAR(10),
#     birth INTEGER
# );

# OrderedDict([('name', 'Vincent Crabbe'), ('house', 'Slytherin'), ('birth', '1979')])
