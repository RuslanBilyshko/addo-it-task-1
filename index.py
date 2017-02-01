# 1
print("\n")


def markup(title=""):
    if title:
        print(title)
        print("-" * 55)
    else:
        print("\n")


markup("Задание #1")


def high_and_low(string):
    data = []

    for x in string.split(" "):
        data.append(int(x))

    return str(max(data)) + " " + str(min(data))


input_string = "129 25 555 46 300"
print(high_and_low(input_string))

markup()

# 2

markup("Задание #2")


def names_list(names):
    count_names = len(names)
    result = ''

    if count_names:

        names_list = []

        for d in names:
            names_list.append(d["name"])

        if count_names == 2:
            result = ' & '.join(names_list)

        elif count_names > 2:
            right_section = ' & '.join(names_list[count_names - 2:])
            left_section = ' , '.join(names_list[:-2])
            result = left_section + " , " + right_section

        else:
            result = names_list[0]

    return result

input_names_list = [{'name': 'Petya'}, {'name': 'Vasya'}, {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
#input_names_list = [{'name': 'Petya'}, {'name': 'Vasya'}]
#input_names_list = [{'name': 'Petya'}]

print(names_list(input_names_list))
