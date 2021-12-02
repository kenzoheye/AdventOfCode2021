from typing import List

def read_data():
    with open("day1/data.txt", "r") as f:
        return f.read()

def parse_data(data: str):
    return list(map(lambda x: int(x), data.split("\n")))

def count_increases(parsed_data: List[int]):
    increases = 0
    for i in range(len(parsed_data)):
        try:
            if parsed_data[i] < parsed_data[i + 1]:
                increases += 1
        except IndexError:
            pass

    return increases

def run():
    data = read_data()
    parsed_data = parse_data(data)
    increases = count_increases(parsed_data)
    print(increases)

run()