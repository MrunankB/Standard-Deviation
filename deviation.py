import math 
import csv

with open('data.csv', newline = '') as f:
  reader = csv.reader(f)
  file_data = list(reader)

data = file_data[0]

#finding mean
def mean(data):
  n = len(data)
  total = 0

  for x in data:
    total += int(x)
  
  mean = int(total/n)
  return mean

# squaring and getting the values
squared_list = []
for number in data:
  a = int(number)-mean(data)
  a = a**2 
  squared_list.append(a)

#getting sum
sum = 0
for i in squared_list:
  sum = sum + i

#dividing the sum by total values
result = sum/(len(data)-1)

#getting the division
std_deviation = math.sqrt(result)
q = round(std_deviation, 2)
print('Standard Deviation for the given data is: ', q)
