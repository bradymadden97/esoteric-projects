import re
file = open('bf.txt', 'r')
nf = open('bfnew.txt', 'a')
f = file.readlines()
for each in f:
    line = re.sub('[^.,\[\]<>\-+]+', "", each).replace(" ", "").replace("\n", "")
    nf.write(line)
