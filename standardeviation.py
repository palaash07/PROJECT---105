import math
import csv

with open("data.csv",newline = "")as f:
    df = csv.reader(f)
    filedata = list(df)

data = filedata[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)

    mean = total/n
    return mean

squarelist = []
for i in data:
    a = int(i)-mean(data)
    a = a**2
    squarelist.append(a)

sum = 0
for i in squarelist:
    sum = sum + i

result = sum/(len(data)-1) 
standarddeviation = math.sqrt(result)  
print(standarddeviation) 



