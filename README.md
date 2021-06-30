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