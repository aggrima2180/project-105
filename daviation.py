import csv
import math
with open("c104.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
    data=file_data[0]

def mean(data):
    a=len(data)
    total=0
    for i in data:
        total += int(i)
    mean=total/a
    return mean


squared_list=[]
for number in data:
    b=int(number)-mean(data)
    b=b**2
    squared_list.append(b)

sum=0 
for x in squared_list:
    sum=sum+x

result=sum/(len(data)-1)
daviation=math.sqrt(result)
print("standerd daviation:",daviation)

    











