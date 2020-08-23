# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fhand:
inp = fh.read()
upper = inp.upper()
print(upper)
