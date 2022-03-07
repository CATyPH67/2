import re


def read_file(filename: str):
    nums = list()
    with open(filename + ".txt") as file_object:
        lines = file_object.readlines()
    lines = filter(lambda x: x.strip(), lines)
    for line in lines:
        nums.append(list(map(int, re.split('; |, | ', line))))

    return nums


def write_file(filename: str, data: list):
    with open(filename + ".txt", 'w') as file_object:
        for row in data:
            file_object.write(' '.join([str(a) for a in row]) + '\n')


def is_less(list1: list, list2: list):
    list1_sum = 0
    list2_sum = 0
    for x in list1:
        list1_sum += x
    for x in list2:
        list2_sum += x

    if list1_sum < list2_sum:
        return True
    else:
        return False


def select_sort(A: list):
    for i in range(len(A) - 1):
        for k in range(i + 1, len(A)):
            if is_less(A[k], A[i]):
                A[k], A[i] = A[i], A[k]


def main():
    nums = read_file("input")
    select_sort(nums)
    write_file("output", nums)


if __name__ == '__main__':
    main()
