# Import class from file
from app.files_and_exception_handling import OpenFile

# Get file name to open
file_name = input("Please enter the file name:  ")
# Create class object
opn_file = OpenFile()
# Output open function of OpenFile class
print(opn_file.open(file_name))
