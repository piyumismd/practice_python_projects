
# nameslist.txt file


count_dict = {}

with open("nameslist", "r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in count_dict:
            count_dict[line] += 1
        else:
            count_dict[line] = 1
        line = f.readline()

print(count_dict)


# Training_01.txt file

counter_dict = {}

with open("Training_01", "r") as open_file:
    line = open_file.readline()
    while line:
        line = line[3:-26]
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = open_file.readline()

print(counter_dict)
