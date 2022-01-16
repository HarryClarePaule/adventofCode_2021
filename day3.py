import pandas as pd

#  Part 1

data = pd.read_csv("csv/day3data.csv", converters={'binary': lambda x: str(x)})
data_list = data.binary.to_list()

new_list = []
for i in data_list:
    string_list = [int(a) for a in str(i)]
    new_list.append(string_list)

column_list = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
df = pd.DataFrame(new_list, columns= column_list)

gamma_rate_bin_list = []
epsilon_rate_bin_list = []

for i in column_list:
    count = df[i].value_counts()
    zero = count.loc[0]
    one = count.loc[1]
    if zero > one:
        gamma_rate_bin_list.append("0")
        epsilon_rate_bin_list.append("1")
    elif one > zero:
        gamma_rate_bin_list.append("1")
        epsilon_rate_bin_list.append("0")


def binary_to_dec(binary_num):
    b_num_str = str(binary_num)
    b_num = list(b_num_str)
    value = 0
    for i in range(len(b_num)):
        digit = b_num.pop() #reverse digits
        if digit == '1':
            value = value + pow(2, i)
    print(f"The decimal value of the number is {value}")
    return value


gamma_rate_bin = ''.join(gamma_rate_bin_list)
gamma_rate_dec = binary_to_dec(gamma_rate_bin)
epsilon_rate_bin = ''.join(epsilon_rate_bin_list)
epsilon_rate_dec = binary_to_dec(epsilon_rate_bin)
power_consumption = gamma_rate_dec * epsilon_rate_dec
print(power_consumption)


#  Part 2

oxygen_generator_rating_list = []

for i in column_list:
    count = df[i].value_counts()
    zero = count.loc[0]
    one = count.loc[1]
    winner = 1
    if zero > one:
        winner = 0
        for x in range(0, len(data_list)-1):
            if winner == new_list[x][0]:
                print(winner)
                print(new_list[x][0])
    else:
        winner = 1
        for x in range(0, len(data_list)-1):
            if winner == new_list[x][0]:
                print(winner)
                print(new_list[x][0])