try:
    with open('/Users/sevakyapujyan/Desktop/Python/homework-2/reaganomics.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IsADirectoryError:
    print("Provided path is a directory.")
except PermissionError:
    print("Insufficient permissions to access the file.")



