
prime_list = []
happy_list = []
overlap_list = []


with open("primenumbers", "r") as prime_file:
    # prime_list = list(map(int, prime_file.readline().strip()))
    line = prime_file.readline()
    while line:
        prime_list.append(int(line))
        line = prime_file.readline()


with open("happynumbers", "r") as happy_file:
    line = happy_file.readline()
    while line:
        happy_list.append(int(line))
        line = happy_file.readline()


overlap_list = list(set(prime_list).intersection(happy_list))
# overlap_list = [i for i in prime_list if (i in happy_list)]
print(overlap_list)
