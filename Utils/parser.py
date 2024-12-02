
def parser(data):
    return [[int(level) for level in line.split()] for line in data.strip().split("\n")]