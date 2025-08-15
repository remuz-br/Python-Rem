#there is a function max for finding the max of a list but this is a good exercise
def find_max(number_list):
    maxs = number_list[0]
    for number in number_list:
        if number > maxs:
            maxs = number
    return maxs