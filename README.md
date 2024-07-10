# Data Manipulation
For this project I wanted to showcase different data manipulation skills using Python.
This project contains three (3) Python files: `generate.py`, `main.py`, `organize.py`.

We can think of this data as being manipulated in order to prepare a mailing list.
I tried to leave many comments in the files to explain how everything works. Here is a basic overview:
`generate.py` creates a large data set -> `main.py` formats the large dataset for reporting or analysis -> `organize.py` uses the large dataset to create a database table to showcase more Pandas and SQL skills.

NOTE* If interested, all print statements from where I obtained the screenshots herein are still inside of their respective files.

## File: `generate.py`
This file was created in order to generate fake information that I could subsequently manipulate.
Primarily using the random libary in Python I created a large data set with randomness. The data
includes an ID, Name, Address, Age, and Gender. The final dataset was made to be one million (1,000,000) entries long with twenty-five thousand (25,000) 
intentional errors. These errors were designed to add another layer of randomness. During generation a number is rolled, if the number is a specific value,
and we have yet to reach our intentional error count, we create a new error. This can be verified once the code is executed.

### Name
Name was created by choosing five (5) random lowercase letters (chars) and concatenating them together. This was done for both
the first and last name. A title (Mr., Ms., Mrs., etc.) was also added to the name, randomly chosen from a predefined list (see `class generator`).
These names were saved to a .csv file with the corresponding ID

### Address, Age, and Gender
Address was created from selecting a random integer from 1 and 9999 and converting it to a string. Then a random street and steet extension (Rd., St., Ln., etc.) were chosen
from a predefined list and concatenated together.

Age and Gender were added to better showcase some SQL skills

Age was selected as a random number from 18 and 99

Gender was picked based on a random number that was either 1 or 2

Address, Age, and Gender were all stored to a separate .csv file, also with their corresponding ID.

## File: `main.py`
Main is home of the manipulator class. This class is used to reformat the randomly generated and selected data for consistency. In main we join both of the other
.csv files on ID, their primary key, and create a new dataset. Then we clean the data and begin reformatting for consistency. To reformat, we drop the title from the name, and reorganize the name as Lastname, Firstname.
Notice that now the first letter is capital as well. We also reformat the address by changing the street name and extension to all capital letters. We then save our fixed data to a new .csv file.

Here is a screenshot showing the console output from printing the data length before and after cleaning, remember, we should have 25,000 errors:

![project1](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/fbd2cda7-8606-4171-8deb-de70931e96db)

This is a screenshot showing the console output before and after reformatting:

![project2](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/afd22dfc-6c8a-46bf-b6c8-25d061881560)


## File `organize.py`
This file was created primary to show SQL skills. In this file I import sqlite3 and use it to create an in-memory database. Once the database is created, using Pandas I use our previously created and
corrected .csv file to create a table in the aforementioned database. Then, using a sqlite3 cursor object I execute a simple SQL query. Then I execute a more complicated SQL query, still using sqlite3 but
directly saving the result as a Pandas DataFrame Object, using Pandas. Finally, I show a much simpler way to perform the more difficult query just by indexing using Pandas.

This is a screenshot showing the console output from the simple query (without Pandas)
![project3](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/59fd16b9-c14f-45c2-8f35-9044b0e55f97)

This is a screenshot of the console output using the `Pandas.read_sql()` method and comparing it the console output of the much simpler method using Pandas indexing:

![project4](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/54ee29f0-b9df-4eb3-b0f7-8cae410539b7)

We can see, we achieved the same results.
