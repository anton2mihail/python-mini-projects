# Reading and writing text files
infile = open("file.txt", "r") # "r" means read only, "W" means read & write only
line = infile.readline()

infile.close()
filename = input("Please enter the filename: ")
file = open(filename, "r")
file2 = open("Outfile.txt", "w")
