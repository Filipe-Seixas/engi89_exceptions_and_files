# Exception Handling and Working with Files


### Example of errors/exceptions
- `Value Error`
- `Syntax Error`
- `Out of Bounds`
- `Key Error`
- `Attribute Error`
- `ZeroDivisionError`

## File Permissions
- `r` READ - Default mode. It opens the file and lets you read it.
- `w` WRITE - Allows for modification of data inside file. If the file doesn't exist, create a new file.
- `x` EXECUTE - Creates a new file, if it already exists, operation fails.
- `a` APPEND - Allows for adding data. If file doesn't exist, creates one.
- `t` TEXT - Opens file in text mode.
- `b` BINARY - Opens file in binary mode
- `+` UPDATE - Opens file for reading and writing.

## Exception Handling

**We have `try`, `except` and `finally`.**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, it will execute regardless of `try` and `except` conditions.

### File Task Example
 - files_and_exception_handling.py
```python
class OpenFile:

    def open(self, name):
        try:
            file = open(name)
            print("Here is your order: ")  # Try block requires except or will throw error
            print(file.read())

        except FileNotFoundError as errmsg:  # Creating an alias for the error
            print(f"File not found. Panic! {errmsg}")

        finally:  # Finally will execute regardless of try and except results
            return "----/----/----"

    def write(self, name):
        try:
            file = open(name, "a")
            order = input("What do you want to add to your order?  ")
            write = file.write("\n" + order)
            file = open(name)
            print(file.read())

        except FileNotFoundError as errmsg:
            print(f"File not found. Panic! {errmsg}")

        finally:
            return "Thanks for visiting. See you again!"

```
 - program.py
```python
# Import class from file
from app.files_and_exception_handling import OpenFile

# Get file name to open
file_name = input("Please enter the file name:  ")
# Create class object
mng_file = OpenFile()
# Output open function of OpenFile class
print(mng_file.open(file_name))
print(mng_file.write(file_name))
```