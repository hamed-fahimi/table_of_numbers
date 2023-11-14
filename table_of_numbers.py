list_table_of_numbers = []
number = int(input("enter the length:"))


def start():
    for i in range(number):
        list_table_of_numbers.append([])
        for j in range(number):
            list_table_of_numbers[i].append(0)
        # print(list_table_of_numbers[i])


def first_number():
    last_number = 1
    list_table_of_numbers[0][len(list_table_of_numbers) // 2] = last_number


def fill_number():
    i = 0
    j = number // 2
    last_number = 2
    for k in range((number ** 2) - 1):
        if i == 0 or j == 0:
            if i == 0 and j != 0:
                i = number - 1
                j = j - 1

            elif j == 0 and i != 0:
                j = number - 1
                i = i - 1

            elif i == 0 and j == 0:
                i += 1

            list_table_of_numbers[i][j] = last_number

        else:
            if list_table_of_numbers[i - 1][j - 1] == 0:
                list_table_of_numbers[i - 1][j - 1] = last_number
                i = i - 1
                j = j - 1
            else:
                list_table_of_numbers[i + 1][j] = last_number
                i += 1

        last_number += 1


start()
first_number()
fill_number()
for l in range(number):
    print(list_table_of_numbers[l])
