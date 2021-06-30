# print(1/0)  # ZeroDivisionError - Divide by zero
#
# num = 9
# if num > 8  # SyntaxError - Missing colon
#     print(num)

# # Create a file with required permission and see what exceptions appear
# # Second Iteration
# file = open("order.text")  # Opens a file and returns it as a file object, takes a string arg with the file name
# print(file)  # This would throw a FileNotFoundError

# Second Iteration
# try:
#     file = open("order.txt")
#     print("File found")  # Try block requires except or will throw error
#
# except FileNotFoundError as errmsg:  # Creating an alias for the error
#     print(f"File not found. Panic! {errmsg}")
#
# finally:  # Finally will execute regardless of try and except results
#     print("Thanks for visiting. See you again!")

# If we create the "order.txt" file, the output will be file found

# Let's apply DRY - OOP - Python Packaging
         #     1     2          3

class OpenFile:

    def open(self, name):
        try:
            file = open(name)
            print("File found")  # Try block requires except or will throw error
            print(file.read())

        except FileNotFoundError as errmsg:  # Creating an alias for the error
            print(f"File not found. Panic! {errmsg}")

        finally:  # Finally will execute regardless of try and except results
            return "Thanks for visiting. See you again!"

