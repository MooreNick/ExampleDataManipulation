import pandas as pd

# I am going to manipulate the data by changing the format
# of the names, and address, pairing the name with the appropriate address, 
# and storing that information to a new .csv file where it
# could be used for further analysis or reporting.

# Using classes helps make code more readable, modular, maintainable, and reusable.
# Object Oriented and Object Based Programming is a key concept in Python.

class manipulator:
    def __init__(self):
        self.data = []

    # name = "" is an example of a default parameter
    # if no argument is given at invocation, the default value is used
    def fixName(self, name = ""):
        if not name:
            return name
        # Get a list of components from the name
        parts = name.split(' ')

        # Capitalize the first letter of the last name and first name
        # We are not interested in the title (Mr. Ms. Mrs. etc) as it makes formatting inconsistent
        # parts[2] == lastName and parts[1] == firstName
        # The str.title() method is used to capitalize the first letter of each word (like a title)
        return parts[2].title() + ', ' + parts[1].title()


    def fixAddress(self, address = ""):
        if not address:
            return address
        # Capitalize the address for formatting and more manipulation
        # str.upper() method capitalizes all letters in a string
        return address.upper()

    def insertData(self, id, name, address, gender, age):
        self.data.append([id, name, address, gender, age])


def main():
    # Create an object of the new class
    Manipulator = manipulator()

    # Read the data from the .csv files
    names = pd.read_csv('names.csv')
    addresses = pd.read_csv('addresses.csv')

    # Join the data using Pandas
    joinedData = pd.merge(names, addresses, on='ID')
    print("Data before cleaning: ", len(joinedData))

    # Clean data by dropping any rows with missing values
    joinedData.dropna(inplace = True)
    print("Data after cleaning: ", len(joinedData))
    print("Entries before data was reformatted:", "\n", joinedData.head())

    # Iterate through each row, fix the name and address, and insert the data
    for idx in joinedData.index:
        Manipulator.insertData(joinedData['ID'][idx], 
                               Manipulator.fixName(joinedData['Name'][idx]), 
                               Manipulator.fixAddress(joinedData['Address'][idx]),
                               joinedData['Gender'][idx],
                               joinedData['Age'][idx])

    # Create our new Pandas DataFrame Object
    newData = pd.DataFrame(Manipulator.data, columns=['ID', 'Name', 'Address', 'Gender', 'Age'])

    # Use that object to create our new .csv file
    newData.to_csv('fixedData.csv', index=False)
    print("Entries after data was reformatted:", "\n", newData.head())


if __name__ == '__main__':
    main()