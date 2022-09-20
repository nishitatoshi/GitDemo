file = open('text.txt')
print(file.read()) #read all the contents
print(file.read(7)) #read limited chars contents

#read 1 line at a time
print(file.readline())

file.close()

#print line by line using readline
file = open('text.txt')

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

file.close()

#print line by line using readlines
file = open('text.txt')

for lines in file.readlines():
    print(lines)


file.close()