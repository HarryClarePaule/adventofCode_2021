
import pandas as pd

code = "1832782-20211205-4516c4d1"
url = "https://adventofcode.com/2021/day/1/input"

data = pd.read_csv("csv/day1data.csv")
data_list = data.Number.to_list()
print(data_list)

# Day 1 part A
# num = data_list[0]
# count = 0
#
# for item in data_list:
#     if item > num:
#         num = item
#         count += 1
#     elif item < num:
#         num = item
#
# print(count)

# Day 1 part B
sum_list = []
for n in range(0, 1998):
    sum_sweep = data_list[n] + data_list[n + 1] + data_list[n + 2]
    sum_list.append(sum_sweep)


print(sum_list)
print(len(data_list))
print(len(sum_list))
count = 0
num = sum_list[0]
for item in sum_list:
    if item > num:
        num = item
        count += 1
    elif item < num:
        num = item

print(count)

