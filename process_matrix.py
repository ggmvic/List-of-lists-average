import numpy as np
import pandas as pd


def process_matrix(matrix):
    """
    It calls to _process_matrix in matrix is correct
    """
    if matrix == []:
        average = []
    else:
        result = and_all(check_matrix(matrix))
        if result:
            average = _process_matrix(matrix)
        else:
            average = print("The list must be a list of lists the numbers with same lenght")
    return average


def _process_matrix(matrix):
    """
    It receives a matrix and
    returns the average of the sum of each element with its neighbours
    """
    sm_nbh = sum_neighbourhood(matrix)
    average = get_average(sm_nbh)
    average = round_up(average)
    average = draw_matrix(average)
    return average


def transpose(matrix):
    """
    It receives a matrix and it returs its transposed
    """
    return list(map(list, zip(*matrix)))


def sum_row(seq):
    index = 0
    accum = []
    for element in seq:
        index += 1
        if len(seq) == 1:
            element = element
        elif element == seq[0]:
            element = (element + seq[1])
        elif element == seq[-1]:
            element = (element + seq[-2])
        else:
            element = (element + seq[index] + seq[index - 2])
        accum.append(element)
    return accum


def sum_row_neighbours(matrix):
    """
    It sums the value of its elements in the rows
    depending on the kind of neighbour
    """
    filas = list(map(sum_row, matrix))
    return filas


def sum_column_neighbours(matrix):
    """
    It sums the value of its elements in the columns
    depending on the kind of neighbour
    """
    new_rows = transpose(matrix)
    columns = sum_row_neighbours(new_rows)
    return transpose(columns)


def sum_neighbourhood(matrix):
    """
    It transforms lists into arrays
    Then it sums the elements with the same index
    and returns a matrix with the new values
    """
    row = np.array(sum_row_neighbours(matrix))
    column = np.array(sum_column_neighbours(matrix))
    sum_neigh = np.subtract(np.add(row, column), matrix)
    return sum_neigh


def get_divisor(matrix):
    """
    It determines what divisor each element
    will have and inserts them into a matrix
    """
    outside_divisors = []
    inside_divisors = []
    divisors = []
    n = len(matrix)
    for i in matrix:
        m = len(i)

    while len(outside_divisors) != m - 2:
        outside_divisors.append(4)
    outside_divisors.insert(0, 3)
    outside_divisors.append(3)

    while len(inside_divisors) != m - 2:
        inside_divisors.append(5)
    inside_divisors.insert(0, 4)
    inside_divisors.append(4)

    while len(divisors) != n - 2:
        divisors.append(inside_divisors)
    divisors.insert(0, outside_divisors)
    divisors.append(outside_divisors)

    return divisors


def get_average(matrix):
    """
    It places the sum matrix and divides it by its divisor
    """
    n = len(matrix)
    for i in matrix:
        m = len(i)
    dividend = matrix
    divisor = np.array(get_divisor(matrix))
    average = dividend / divisor.reshape(n, m)
    average = average.tolist()

    return average


def round_up(matrix):
    """
    It rounds up the elements in order to make them visually more pleasant
    """
    new_list = []
    for i in matrix:
        for j in i:
            j = map(lambda a: round(a, 2), i)
            j = list(j)
        new_list.append(j)
    return new_list


def draw_matrix(matrix):
    """
    It returns the matrix in rows and columns
    """
    l1, l2 = len(matrix), len(matrix[0])
    matrix = pd.DataFrame(matrix, index=['']*l1, columns=['']*l2)
    print(matrix)


def check_matrix(matrix):
    result = []
    result.append(list_of_lists(matrix))
    result.append(lenght_matrix(matrix))
    result.append(is_numerical_matrix(matrix))
    return result


def and_all(bools):
    total_so_far = True
    for element in bools:
        total_so_far = total_so_far and element
    return total_so_far


def is_numerical_matrix(matrix):
    result = None
    for i in matrix:
        if not isinstance(i, list):
            result = False
        else:
            for j in i:
                if isinstance(j, (int, float)):
                    result = True
                else:
                    result = False
    return result


def lenght_matrix(matrix):
    result = None
    if not list_of_lists(matrix):
        result = False
    else:
        it = iter(matrix)
        the_len = len(next(it))
        if not all(len(lenght) == the_len for lenght in it):
            result = False
        else:
            result = True
    return result


def list_of_lists(matrix):
    result = None
    for i in matrix:
        if isinstance(i, list):
            result = True
        else:
            result = False
    return result


if __name__ == "__main__":
    process_matrix([[1, 2, 3], [4, 5, 6]])
