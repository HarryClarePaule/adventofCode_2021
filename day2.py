import pandas as pd

data = pd.read_csv("csv/day2data.csv")
data_list = data.command.to_list()
#print(data_list)

new_list = []
for i in data_list:
    new_list.append(i.split())

#print(new_list)

horiz_pos = 0
depth = 0
aim = 0

for n in range(0, len(new_list)):
    direction = new_list[n][0].lower()
    move = int(new_list[n][1])
    # print(direction)
    # print(move)
    if direction == "forward":
        horiz_pos += move
        new_depth = depth + (move * aim)
        depth = new_depth
    elif direction == "down":
        #depth += move
        aim += move
    else:
        #depth -= move
        aim -= move

print(horiz_pos)
print(depth)
position = horiz_pos * depth
print(position)
