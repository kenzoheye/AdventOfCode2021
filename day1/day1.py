from typing import List

def read_data():
    with open("day1/data.txt", "r") as f:
        return f.read()

def parse_data(data: str):
    return list(map(lambda x: int(x), data.split("\n")))

def make_sums(data: List[int]):
    summed_data = []

    for i in range(len(data)):
        try:
            new_value = data[i] + data[i + 1] + data[i + 2]
            summed_data.append(new_value) 
        except IndexError:
            break

    return summed_data

def count_increases(data: List[int]):
    increases = 0
    for i in range(len(data)):
        try:
            if data[i] < data[i + 1]:
                increases += 1
        except IndexError:
            break

    return increases

def run_part_one():
    data = read_data()
    parsed_data = parse_data(data)
    increases = count_increases(parsed_data)
    print(f"Part 1: {increases}")

def run_part_two():
    data = read_data()
    parsed_data = parse_data(data)
    summed_data = make_sums(parsed_data)
    increases = count_increases(summed_data)
    print(f"Part 2: {increases}")

run_part_one()
run_part_two()