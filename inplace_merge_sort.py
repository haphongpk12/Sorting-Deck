#!/usr/bin/env python3
import argparse


def call_inplace_merge_sort(unsort_list, left, right):
    """
    Implement Merge Sort
        - Input:
            + list: list of integer numbers want to sort.
            + left: start index of the list.
            + right: end index of the list.
        - Output: Sorted list of integer numbers.
        - Big O Notation:
            + Best case - O(n): List had already sorted.
            + Average case - O(n^2)
            + Worst case - O(n^2): List had already sorted in reverse
    """
    if left < right:
        mid = left + (right - left) // 2
        call_inplace_merge_sort(unsort_list, left, mid)
        call_inplace_merge_sort(unsort_list, mid + 1, right)
        compare_merge(unsort_list, left, mid, right)
        print_sort_list(unsort_list)


def compare_merge(unsort_list, start, mid, end):
    """
    Use to compare value of two sides of list
    """
    index = mid + 1
    if unsort_list[mid] <= unsort_list[index]:
        return
    while start <= mid and index <= end:
        start, mid, index = traverse_merge(unsort_list, start, mid, index)


def traverse_merge(unsort_list, start, mid, index):
    """
    Use to traverse and compare one by one value of
    """
    if unsort_list[start] <= unsort_list[index]:
        start += 1
    else:
        position = insert_merge(unsort_list, index, start)
        start += 1
        mid += 1
        index += 1
    return start, mid, index


def insert_merge(unsort_list, index, start):
    """
    Use to swap element of the list using method like insert
    """
    current_value = unsort_list[index]
    position = index
    while position is not start:
        unsort_list[position] = unsort_list[position - 1]
        position -= 1
    unsort_list[start] = current_value
    return position


def print_sort_list(unsort_list):
    """
    Print the list after sort in string type
    """
    str_num = " ".join(str(element) for element in unsort_list)
    print(str_num)


def create_parse():
    """
    Function use to create parse of argument
    """
    parse = argparse.ArgumentParser()
    parse.add_argument(
                        "N", help="an integer for the list to sort",
                        nargs="+", type=int)
    parse.add_argument(
                        "--algo", default="inplace",
                        help="""specify which algorithm to use for sorting
                        among in-place merge sort""")
    return parse


def main():
    """
    Main function: Use to implement argument parse
    """
    parse = create_parse()
    arg = parse.parse_args()
    list_of_numbers = arg.N
    call_inplace_merge_sort(list_of_numbers, 0, len(list_of_numbers) - 1)


if __name__ == "__main__":
    main()
