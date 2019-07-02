#!/usr/bin/env python3
import argparse


def call_bubble_sort(unsort_list):
    """
    Implement Bubble Sort
        - Input:
            + list: list of integer numbers want to sort.
        - Output: Sorted list of integer numbers.
        - Big O Notation:
            + Best case - O(n): List had already sorted
            + Average case - O(n^2)
            + Worst case - O(n^2): List had already sorted in reverse
    """
    # Limit the length of list, always decrease one unit when pass one loop
    for limit in range(len(unsort_list) - 1, 0, -1):
        traverse_list_bubble(unsort_list, limit)


def traverse_list_bubble(unsort_list, limit):
    """
    Use to traverse the list with the limit:
        + Compare to value in index & index + 1
        + If value of index > value of index + 1: swap
    """
    # Linear traverse the list
    for index in range(limit):
        # Check if next value greater than present value: swap
        if unsort_list[index] > unsort_list[index + 1]:
            swap_element(unsort_list, index, index + 1)
            print_sort_list(unsort_list)


def call_insertion_sort(unsort_list):
    """
    Implement Insertion Sort
        - Input:
            + list: list of integer numbers want to sort.
        - Output: Sorted list of integer numbers.
        - Big O Notation:
            + Best case - O(n): List had already sorted
            + Average case - O(n^2)
            + Worst case - O(n^2): List had already sorted in reverse
    """
    for index in range(1, len(unsort_list)):
        # Keep value & position of first element of one loop
        current_value = unsort_list[index]
        position = index
        insert(unsort_list, position, current_value)


def insert(unsort_list, position, current_value):
    """
    Use to check condition: postion > 0 & element[position - 1] ? current_value
    If satisfy: insert
    """
    change = False
    while position > 0 and unsort_list[position - 1] > current_value:
        unsort_list[position] = unsort_list[position - 1]
        change = True
        position -= 1
    unsort_list[position] = current_value

    if change:
        print_sort_list(unsort_list)


def call_merge_sort(unsort_list):
    """
    Implement Merge Sort
        - Input:
            + list: list of integer numbers want to sort.
        - Output: Sorted list of integer numbers.
        - Big O Notation:
            + Best case - O(nlog(n)): List had already sorted.
            + Average case - O(nlog(n))
            + Worst case - O(nlog(n)): merge sort will have to do
                maximum number of comparisons.
    """
    if len(unsort_list) > 1:
        mid = len(unsort_list) // 2
        # Split list to left-list and right-list
        left_list = unsort_list[:mid]
        right_list = unsort_list[mid:]

        # Continue to split left-list, right-list more smaller
        call_merge_sort(left_list)
        call_merge_sort(right_list)

        merge(unsort_list, left_list, right_list)
        print_sort_list(unsort_list)


def merge(unsort_list, left_list, right_list):
    """
    Use to check and merge element to the main-list
    """
    # Initial index of left-list, right-list, merge-list
    l_index = 0
    r_index = 0
    m_index = 0

    while l_index < len(left_list) and r_index < len(right_list):
        if left_list[l_index] < right_list[r_index]:
            unsort_list[m_index] = left_list[l_index]
            l_index += 1
        else:
            unsort_list[m_index] = right_list[r_index]
            r_index += 1
        m_index += 1

    l_index, m_index = sublist_merge(unsort_list, left_list, l_index, m_index)
    r_index, m_index = sublist_merge(unsort_list, right_list, r_index, m_index)


def sublist_merge(unsort_list, sub_list, sub_index, merge_index):
    """
    Use to merge the rest of the sub-list
    """
    while sub_index < len(sub_list):
        unsort_list[merge_index] = sub_list[sub_index]
        sub_index += 1
        merge_index += 1
    return sub_index, merge_index


def call_quick_sort(unsort_list, first, last):
    """
    Implement Quick Sort
        - Input:
            + list: list of integer numbers want to sort.
            + first: Starting index of algorithm.
            + last: Ending index of algorithm.
        - Output: Sorted list of integer numbers.
        - Big O Notation:
            + Best case - O(nlog(n)): partition process always picks
                the middle element as pivot.
            + Average case - O(nlog(n))
            + Worst case - O(n^2): partition process always picks greatest
                or smallest element as pivot
    """
    if first < last:
        pivot_index = partition_quick(unsort_list, first, last)
        call_quick_sort(unsort_list, first, pivot_index - 1)
        call_quick_sort(unsort_list, pivot_index + 1, last)


def partition_quick(unsort_list, first, last):
    """
    Use to partition list of integer numbers :This function takes last element
        as pivot, places the pivot element
        at its correct position in sorted array, and places all smaller than
        pivot to left of pivot and greater than pivot to right of pivot
    """
    pivot = unsort_list[last]
    print("P: ", pivot)
    left = first
    right = last - 1

    while True:
        left, right = traverse_list_quick(unsort_list, left, right, pivot)
        if left >= right:
            break
        swap_element(unsort_list, left, right)
        left += 1
        right -= 1
    swap_element(unsort_list, left, last)

    print_sort_list(unsort_list)
    return left


def traverse_list_quick(unsort_list, left, right, pivot):
    """
    Use to check two side of the with the condition below
    """
    while left <= right and unsort_list[left] < pivot:
        left += 1
    while right >= left and unsort_list[right] > pivot:
        right -= 1
    return left, right


def print_sort_list(unsort_list):
    """
    Print the list after sort in string type
    """
    str_num = " ".join(str(element) for element in unsort_list)
    print(str_num)


def swap_element(unsort_list, index_a, index_b):
    """
    Use to swap two elements
    """
    unsort_list[index_a], unsort_list[index_b] = \
        unsort_list[index_b], unsort_list[index_a]


def analysis_process(gui, sort_option, list_of_numbers):
    if gui:
        if len(list_of_numbers) > 15:
            print("Size of numbers list have to smaller than 15!")
        else:
            choose_algorithm(sort_option, list_of_numbers)
    else:
        choose_algorithm(sort_option, list_of_numbers)


def choose_algorithm(option, numbers):
    """
    Use to setup option for the program
    """
    if option == "bubble":
        call_bubble_sort(numbers)
    elif option == "insert":
        call_insertion_sort(numbers)
    elif option == "merge":
        call_merge_sort(numbers)
    elif option == "quick":
        call_quick_sort(numbers, 0, len(numbers) - 1)


def create_parse():
    """
    Function use to create parse of argument
    """
    parse = argparse.ArgumentParser()
    parse.add_argument(
                        "N", help="an integer for the list to sort",
                        nargs="+", type=int)
    parse.add_argument(
                        "--algo", default="bubble",
                        help="""specify which algorithm to use for sorting
                        among [bubble|insert|quick|merge], default bubble""")
    parse.add_argument(
                        "--gui", action="store_true",
                        help="visualise the algorithm in GUI mode")
    return parse


def main():
    """
    Main function: Use to implement argument parse
    """
    parse = create_parse()
    arg = parse.parse_args()
    list_of_numbers = arg.N
    sort_option = arg.algo
    gui = arg.gui
    analysis_process(gui, sort_option, list_of_numbers)


if __name__ == "__main__":
    main()
