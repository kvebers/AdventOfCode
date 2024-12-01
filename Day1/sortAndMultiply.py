from Utils.utils import getData
import json

data = getData('https://adventofcode.com/2024/day/1/input')
numbers = data.split()
numbers = [int(number) for number in numbers]
collum1 = numbers[::2]
collum2 = numbers[1::2]
collum1.sort()
collum2.sort()
diff = [abs(collum1[i] - collum2[i]) for i in range(len(collum1))]
collumCount = [collum2.count(collum1[i]) for i in range(len(collum1))]
table = [collum1[i] * collumCount[i] for i in range(len(collum1))]
tableSum = sum(table)
print(tableSum)
    