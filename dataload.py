import match
import random

all_route_numbers = []
all_route_lengths = []

def load():
    with open("./routes.pfx2as",'r') as file:
        for line in file.readlines():
            args = line.split("\t")
            if args[0].__contains__("."):
                number = match.string2prefix(args[0])
                length = int(args[1])
                all_route_numbers.append(number)
                all_route_lengths.append(length)

def get_with_random(count):
    get_numbers = []
    get_lengths = []

    list = random.sample(range(1,len(all_route_numbers)), count)
    for i in list:
        get_numbers.append(all_route_numbers[i])
        get_lengths.append(all_route_lengths[i])
    return get_numbers,get_lengths




