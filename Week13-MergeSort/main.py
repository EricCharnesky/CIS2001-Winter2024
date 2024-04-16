def merge(first_half, second_half, some_list):
    first_half_index = 0
    second_half_index = 0

    while first_half_index < len(first_half) and second_half_index < len(second_half):
        if first_half[first_half_index] < second_half[second_half_index]:
            some_list[first_half_index+second_half_index] = first_half[first_half_index]
            first_half_index += 1
        else:
            some_list[first_half_index + second_half_index] = second_half[second_half_index]
            second_half_index += 1

    while first_half_index < len(first_half):
        some_list[first_half_index+second_half_index] = first_half[first_half_index]
        first_half_index += 1

    while second_half_index < len(second_half):
        some_list[first_half_index+second_half_index] = second_half[second_half_index]
        second_half_index += 1

def merge_sort(some_list):

    if len(some_list) < 2:
        return

    middle_index = len(some_list) // 2

    first_half = some_list[:middle_index]
    second_half = some_list[middle_index:]

    merge_sort(first_half)
    merge_sort(second_half)

    merge(first_half, second_half, some_list)


some_values = [ 7, 3, 5, 8, 12, 15, 21, 9, 2]

merge_sort(some_values)

print(some_values)