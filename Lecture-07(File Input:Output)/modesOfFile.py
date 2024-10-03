f = open("input.txt", "r+")
f.write("Helloo")
print(f.read()) # read from file from the pointer pointed
f.close()

f = open("input1.txt", "w+") # truncated(override the data)
print(f.read())
f.write("Hello there!")
f.close()

f = open("input2.txt", "a+") 
print(f.read())
f.write(" Hello there!")
f.close()

f = open("input3.txt", "x") 
f.write("Hello there!")
f.close()

# Create and write to a file
with open("example.txt", "w+") as file:
    file.write("This is a test file.....")
    file.seek(0)  # Move to the beginning
    print("Content after writing:", file.read())
    file.seek(5)  # Move to the 5th byte
    print("Current file position:", file.tell())
    file.truncate(10)  # Truncate the file to 10 bytes
    file.seek(0)
    print("Content after truncating:", file.read())
