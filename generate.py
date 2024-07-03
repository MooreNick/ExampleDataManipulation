import random
import string
import pandas as pd

# In order to show proficiency manipulating data with Python, we first need
# data. I am going to create two .csv files with random data. The first file
# is going to be focused on a list of names and an ID, while the second file
# will be a list of addresses with a matching ID. I am also going to randomly
# generate ID that will need to be removed (cleaned) before manipulation.

class generator:
    def __init__(self):
        self.streetNames = ['Main', 'First', 'Second', 'Third', 'Fourth', 'Park', 'Fifth', 'Maple', 'Elm', 'Sixth']
        self.streetExtensions = ['St', 'Ave', 'Blvd', 'Rd', 'Dr', 'Ct', 'Ln', 'Pkwy', 'Way', 'Pl']
        self.titles = ['Mr', 'Mrs', 'Ms', 'Dr', 'Prof', 'Rev', 'Hon', 'Pres', 'Sen', 'Rep']
        self.names = []
        self.addresses = []

    # Generate a random name of given length
    # The name is a combination of a title, first name, and
    # last name. The title is randomly chosen from a list of titles
    def getName(self, length = 5):
        first = ""
        last = ""
        for i in range(length):
            first += random.choice(string.ascii_lowercase)
            last += random.choice(string.ascii_lowercase)  
        return random.choice(self.titles) + ' ' + first + ' ' + last

    # Generate a random address
    # Number is a random number between 1 and 9999
    # Street is a randomly chosen street name
    # Extension is a randomly chosen street extension

    def getAddress(self):
        number = random.randint(1, 9999)
        street = random.choice(self.streetNames)
        extension = random.choice(self.streetExtensions)
        # Here we are calling the string (str) constructor to convert the integer to a string
        return str(number) + ' ' + street + ' ' + extension
    
    def insertName(self, id, name):
        self.names.append([id, name])

    def insertAddress(self, id, address):
        # I am adding a gender and age this .csv to show SQL proficiency later on
        roll = random.randint(1, 2)
        gender = "M" if roll == 1 else "F"
        age = random.randint(18, 99)
        self.addresses.append([id, address, gender, age])

    

def main():
    # Create an object of the new class
    Generator = generator()
    # Number of fake names and addresses
    size = 1000000
    # Amount of errors we want to introduce
    errors = 25000
    # Starting point for id (primary key)
    id = 1

    # Generate info
    for i in range(size):
        # I do not want the errors to be consecutive but I want to ensure we get all of the errors
        roll = random.randint(1, 5)
        if (roll == 1) & (errors > 0):
            errors -= 1
            roll = random.randint(1, 2)
            # Extra randomness to change which part of the information is missing
            if roll == 1:
                name = ""
                address = Generator.getAddress()
            else:
                name = Generator.getName()
                address = ""
        else:
            name = Generator.getName()
            address = Generator.getAddress()

        # Add our new information
        Generator.insertName(id, name)
        Generator.insertAddress(id, address)
        id += 1

    # Create Pandas DataFrame Objects to store our data
    nameData = pd.DataFrame(Generator.names, columns=['ID', 'Name'])
    addressData = pd.DataFrame(Generator.addresses, columns=['ID', 'Address', 'Gender', 'Age'])

    # Use those objects to create our new .csv files
    nameData.to_csv('names.csv', index=False)
    addressData.to_csv('addresses.csv', index=False)
        

if __name__ == '__main__':
    main()
        

    
