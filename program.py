# Import class from file
from app.files_and_exception_handling import OpenFile

# Get file name to open
file_name = input("Please enter the file name:  ")
# Create class object
mng_file = OpenFile()
# Output open function of OpenFile class
print(mng_file.open(file_name))
print(mng_file.write(file_name))
