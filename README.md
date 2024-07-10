# Data Manipulation
For this project I wanted to showcase different data manipulation skills using Python.
This project contains four (4) Python files: `generate.py`, `main.py`, `organize.py`, `upload.py`.
The project is also split into two parts. The first part covers creating the data and the second part
is an example of sending the data to Oracle's Object Storage in the cloud and retrieving that data. 

In an attempt to show additional proficiencies, in part 2, I also retrieve the data from the cloud on
a virtual machine (VM) running Red Hat. I initially planned on hosting the VM on Oracle's Cloud as well, however,
the free tier does not support importing the `.iso` file containing an image of Red Hat. (Unfortunately I uploaded the 10gb file before I realized this :))
Therefore I hosted the VM using Oracle's VirtualBox Manager on my Windows 11 machine.

## Part 1

We can think of this data as being manipulated in order to prepare a mailing list.
I tried to leave many comments in the files to explain how everything works. Here is a basic overview:
`generate.py` creates a large data set -> `main.py` formats the large dataset for reporting or analysis -> `organize.py` uses the large dataset to create a database table to showcase more Pandas and SQL skills.

NOTE* If interested, all print statements from where I obtained the screenshots herein are still inside of their respective files.

### File: `generate.py`
This file was created in order to generate fake information that I could subsequently manipulate.
Primarily using the random libary in Python I created a large data set with randomness. The data
includes an ID, Name, Address, Age, and Gender. The final dataset was made to be one million (1,000,000) entries long with twenty-five thousand (25,000) 
intentional errors. These errors were designed to add another layer of randomness. During generation a number is rolled, if the number is a specific value,
and we have yet to reach our intentional error count, we create a new error. This can be verified once the code is executed.

#### Name
Name was created by choosing five (5) random lowercase letters (chars) and concatenating them together. This was done for both
the first and last name. A title (Mr., Ms., Mrs., etc.) was also added to the name, randomly chosen from a predefined list (see `class generator`).
These names were saved to a .csv file with the corresponding ID

#### Address, Age, and Gender
Address was created from selecting a random integer from 1 and 9999 and converting it to a string. Then a random street and steet extension (Rd., St., Ln., etc.) were chosen
from a predefined list and concatenated together.

Age and Gender were added to better showcase some SQL skills

Age was selected as a random number from 18 and 99

Gender was picked based on a random number that was either 1 or 2

Address, Age, and Gender were all stored to a separate .csv file, also with their corresponding ID.

### File: `main.py`
Main is home of the manipulator class. This class is used to reformat the randomly generated and selected data for consistency. In main we join both of the other
.csv files on ID, their primary key, and create a new dataset. Then we clean the data and begin reformatting for consistency. To reformat, we drop the title from the name, and reorganize the name as Lastname, Firstname.
Notice that now the first letter is capital as well. We also reformat the address by changing the street name and extension to all capital letters. We then save our fixed data to a new .csv file.

Here is a screenshot showing the console output from printing the data length before and after cleaning, remember, we should have 25,000 errors:

![project1](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/fbd2cda7-8606-4171-8deb-de70931e96db)

This is a screenshot showing the console output before and after reformatting:

![project2](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/afd22dfc-6c8a-46bf-b6c8-25d061881560)


### File `organize.py`
This file was created primary to show SQL skills. In this file I import sqlite3 and use it to create an in-memory database. Once the database is created, using Pandas I use our previously created and
corrected .csv file to create a table in the aforementioned database. Then, using a sqlite3 cursor object I execute a simple SQL query. Then I execute a more complicated SQL query, still using sqlite3 but
directly saving the result as a Pandas DataFrame Object, using Pandas. Finally, I show a much simpler way to perform the more difficult query just by indexing using Pandas.

This is a screenshot showing the console output from the simple query (without Pandas):
![project3](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/59fd16b9-c14f-45c2-8f35-9044b0e55f97)

This is a screenshot of the console output using the `Pandas.read_sql()` method and comparing it the console output of the much simpler method using Pandas indexing:

![project4](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/54ee29f0-b9df-4eb3-b0f7-8cae410539b7)

We can see, we achieved the same results.

## Part 2
### File: `upload.py`
This file was created to upload the data that was created and manipulated to Oracle's Object Storage in the cloud. I accomplished this with the help of the Pandas library and the OCI library.
The first step in connecting to Oracle's Cloud is building out the necessary information for configuration. This can be done in a couple of different ways, however, I chose the dictionary method. Once I gathered
The necessary information I was able to validate my configuration and create a client using methods from the OCI library. Using Pandas I read in the `.csv` file containing the corrected information from earlier. I then learned
the file was too large to upload for the free tier so I created a smaller version of it, also as a Pandas DataFrame. Then, using another method from the OCI library I was able to save the information into the designated bucket on the cloud.

Additional Note: In the final version of this file I changed the configuration information to "REDACTED" as it makes the code look cleaner. As mentioned, I was using the free tier of Oracle Cloud and everything will be deleted anyway.

This is a screenshot showing the file in Oracle's Cloud:

![project5](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/7cd282cb-73b9-40b7-a05e-4154a73c97dc)


### Red Hat VM
Next I wanted to utilize Red Hat and create a file to pull the information back from the cloud. I navigated to Red Hat's website and began my free trial, then I was able to download the `.iso` file. Next, using Oracle's VirtualBox I was able
to start a VM using the downloaded image. I needed to configure a couple of settings, like screen size and host key. -- The host key returns your mouse and keyboard inputs back to the host machine instead of the VM. This is initally set to Right Control,
but my laptop does not have a Right Control key. I also installed pip on the machine to easily add necessary Python libraries.

Once those minor configurations were set I was able to sign into Oracle's Cloud on the VM and add a new API Key. Once this was complete I created a new Python file called `download.py` using the Nano text editor. This file used the same libraries as `upload.py`
and a part of the io library (StringIO). I once again setup the configurations and was able to connect to the cloud and retrieve the object using a method from the OCI library. Once the object was successfully retrieved I was able to use StringIO to format the
data for Pandas. Then I was able to return it to a Pandas DataFrame Object.

This is a screenshot of the `download.py` file:

![Screenshot (410)](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/6914ce79-ab10-466e-bb68-db04587b8d17)

This is a screenshot of the console output from the above file:

![Screenshot (409)](https://github.com/MooreNick/ExampleDataManipulation/assets/123336257/079f3c57-28b7-48ed-89f3-57df3f7e603d)
