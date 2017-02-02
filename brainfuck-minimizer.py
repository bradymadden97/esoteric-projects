import re
filename = input("Enter brainfuck filename: ")
file = open(filename, 'r+')
f = file.readlines()
file.seek(0)
file.truncate()
file.close()
nf = open(filename, 'a')
line = ""
counter = 0
for each in f:
    for char in each:
        line += re.sub('[^.,\[\]<>\-+]+', "", char).replace(" ", "").replace("\n", "")
        counter += 1
        if counter % 75 == 0:
            line += '\n'
nf.write(line)
