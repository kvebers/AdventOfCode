from Utils.utils import getData
import json

data = getData()
numbers = data.split()
numbers = [int(number) for number in numbers]
collum1 = numbers[::2]
collum2 = numbers[1::2]
collum1.sort()
collum2.sort()
diff = [abs(collum1[i] - collum2[i]) for i in range(len(collum1))]
sumDiff = sum(diff)
print(sumDiff)