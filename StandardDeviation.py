import csv
import pandas as pd
import plotly.express as px
import math

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#file_data.pop(0)
data = file_data[0]
print("D: ", data)

def mean(data):
    total = 0
    total_entries = len(data)
    for x in data:
        total = total + int(x)

    mean = total/total_entries
    return(mean)

m = mean(data)
print("M: ", m)

squared_list = []
for number in data:
    a = int(number) - m
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i
print("S: ", sum)

print("L: ", len(data) - 1)

result = sum/(len(data) - 1)
print("R: ", result)
standard_deviations = math.sqrt(result)

print("Standard Deviation: ", standard_deviations)