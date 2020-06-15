def linear_search(the_values, item):
    """
    Implementation of the linear search on an unsorted sequence
    :param the_values: list/array
    :param item: string/number
    :return: Bool (True/False)
    """
    list_size = len(the_values)
    for index in range(list_size):
        # If the target is found in the ith element, return True
        if the_values[index] == item:
            return True

    return False  # the item is not in the sequence


def sorted_linear_search(the_values, item):
    """
    Implementation of the linear search on a sorted sequence
    :param the_values: list/array
    :param item: string/number
    :return: Bool (True/False)
    """
    list_size = len(the_values)
    for index in range(list_size):
        # If the target is found in the ith element, return True
        if the_values[index] == item:
            return True
        # If target is larger than the ith element, it's not in the sequence.
        elif the_values[index] > item:
            return False

    return False  # the item is not in the sequence


def find_smallest(the_values):
    """
    Searching for the smallest values in an unsorted sequence
    :param the_values: list
    :return: smallest value
    """
    list_size = len(the_values)
    # Assume the first item is the smallest value
    smallest = the_values[0]
    # Determine if any other item in the sequence is smaller
    for index in range(1, list_size):
        if the_values[index] < smallest:
            smallest = the_values[index]

    return smallest  # return the smallest found


def binary_search(the_values, target):
    """
    Implementation of the binary search algorithm
    :param the_values: list
    :param target: item
    :return: bool
    """
    # Start with the entire sequence of elements. Defining indexes here of low and high
    # Let's suppose the target is 2 and the list is [1, 2, 3, 4, 5, 6]
    low = 0
    high = len(the_values) - 1

    # Repeatedl subdivide the sequence in half until the target is found
    while low <= high:  # while the indexes are in their supposed places (always low is equal or lower than high)
        # Find the midpoint of the sequence (capture the integer using //)
        # from a ex. list = [1, 2, 3(mid), 4, 5, 6], mid will be 2, or value 3 in the ex. list
        mid = (high + low) // 2

        # Does the midpoint contain the target?
        # ex. [1, 2, 3(mid), 4, 5, 6] 3 is equal to 2 (target)?
        if the_values[mid] == target:
            return True

        # Or does te target precede the midpoint?
        # Ex. 2 is less than 3? yes, it is in this case, so high now receives mid(2) - 1 = 1
        elif target < the_values[mid]:
            high = mid - 1

        # or does it follow the midpoint?
        # Ex. if 2 is greater than 3, than low(0) would received mid(2) + 1 = 3
        else:
            low = mid + 1

    return False


def bubble_sort(the_sequence):
    """
    Implementation of the bubble sort alorithm
    Sorts a sequence in ascending order using the bubble sort algorithm
    :param the_sequence: list
    :return: list sorted
    """
    seq_size = len(the_sequence)
    # perform n-1 bubble operation on the sequence
    for i in range(seq_size - 1):
        # bubble the largest item to the end
        end_range = seq_size - i - 1
        for j in range(0, end_range):
            if the_sequence[j] > the_sequence[j + 1]:  # swap the j and j + 1 items
                the_sequence[j], the_sequence[j + 1] = the_sequence[j + 1], the_sequence[j]


def selection_sort(the_sequence):
    """
    Implementation of the selection sort alogrithm
    Sorts a sequence in ascending order using the selection sort algorithm.
    :param the_sequence: list
    :return: change the list
    """
    size = len(the_sequence)
    for i in range(size - 1):
        # Assume the ith element is the smallest
        smallest = i
        # Determine if any other element contains a smaller value
        for j in range(i + 1, size):
            if the_sequence[j] < the_sequence[smallest]:
                smallest = j

        if smallest != i:
            the_sequence[i], the_sequence[smallest] = the_sequence[smallest], the_sequence[i]





# Driver program
list_strings = ['ef', 'ab', 'cd']
list_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 'cd'
target_number = 0
print(find_smallest(list_numbers))
print(find_smallest(list_strings))

print(binary_search(sorted(list_numbers), target_number))

bubble_sort(list_strings)
print(list_strings)

selection_sort(list_numbers)
print(list_numbers)
