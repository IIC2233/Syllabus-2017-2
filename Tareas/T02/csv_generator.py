from random import randint

path1 = "pieces_name.csv"
path2 = "pieces.csv"
min1 = 0
max1 = 20


with open(path1, "r") as file:
	names = [f.strip() for f in file]

with open(path2, "w") as file:
	while len(names) > 0:
		file.write("{0},{1}\n".format(names.pop(0), randint(min1, max1)))