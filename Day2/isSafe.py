from Utils.utils import getData
from Utils.parser import parser
data = getData('https://adventofcode.com/2024/day/2/input')

def countSafeReportsPart1(data):
    reports = parser(data)
    counter = sum(1 for report in reports if isSafeReport(report))
    return counter

def isSafeReport(report):
    increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def canBeSafe(report):
    for i in range(len(report)):
        result = report[:i] + report[i+1:]
        if isSafeReport(result):
            return True
    return False

def countSafeReportsPart2(data):
    reports = parser(data)
    counter = 0
    for report in reports:
        if isSafeReport(report) or canBeSafe(report):
            counter += 1
    return counter

safereport = countSafeReportsPart1(data)
print(f"Task 1: {safereport}")
result = countSafeReportsPart2(data)
print(f"Task 2: {result}")