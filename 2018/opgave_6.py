"""
Nummering van de vierkantjes is als volgt, diagnonaal van linksonder naar rechtsboven
- bovenste deel gevuld is nummer 1
- onderste deel gevuld is nummer 2
Diagnonaal van linksboven naar rechtsonder:
- bovenste deel gevuld is nummer 3
- onderste deel gevuld is nummer 4
Volledig gevuld is nummer 5 (komt niet voor?)
Volledig leeg is nummer 6 (komt niet voor?)

De rechthoek lijkt te bestaan uit 21 rijen en 55 kolommen
"""
"         1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  1  2  3  4  5"
"---------------------------------------------------------------------------------------------"
ROW_01 = [1, 2, 3, 1, 2, 3, 2, 1, 3, 2, 2, 1, 3, 1, 3, 2, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1, 4, 2, 1, 1, 3, 1, 4, 2, 1, 1, 3, 1, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 2, 3, 1, 1, 3, 1]
ROW_02 = [2, 2, 2, 3, 2, 2, 1, 1, 3, 1, 3, 2, 1, 4, 1, 1, 1, 2, 3, 1, 2, 3, 2, 1, 4, 2, 2, 3, 1, 3, 2, 1, 3, 1, 1, 1, 3, 1, 3, 2, 1, 4, 1, 1, 1, 2, 3, 1, 3, 1, 2, 1, 3, 1, 1]
ROW_03 = [1, 3, 2, 1, 2, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 2, 1, 1, 3, 1, 2, 1, 1, 3, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 2, 4, 2, 2, 1, 1, 3, 2, 2, 2, 3, 2, 1, 1, 3, 1, 2, 3, 2, 1]
ROW_04 = [3, 1, 1, 3, 2, 2, 1, 4, 2, 1, 1, 3, 1, 2, 3, 2, 4, 1, 1, 1, 3, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 1, 3, 2, 2, 1, 3, 1, 3, 2, 1, 4, 2, 2, 1, 3, 1, 3, 2, 2, 3, 1, 2, 3]
ROW_05 = [2, 1, 2, 3, 2, 1, 2, 3, 1, 3, 1, 2, 1, 1, 3, 1, 1, 3, 1, 2, 2, 2, 3, 2, 1, 2, 3, 1, 3, 1, 2, 1, 4, 2, 1, 1, 3, 1, 2, 3, 2, 1, 4, 1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 1, 3]
ROW_06 = [1, 2, 1, 3, 1, 3, 2, 1, 4, 2, 1, 1, 3, 1, 4, 1, 3, 1, 3, 2, 1, 4, 2, 2, 2, 3, 1, 1, 2, 1, 4, 1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 1, 3, 1, 2, 1, 3, 1, 4, 1, 1, 1, 2, 3, 2]
ROW_07 = [2, 2, 3, 1, 2, 1, 3, 2, 2, 4, 1, 1, 1, 2, 3, 1, 2, 3, 2, 1, 4, 2, 2, 1, 3, 1, 3, 1, 2, 1, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 1, 2, 1, 4, 2, 2, 2, 3, 2, 2, 3, 1, 2, 3]
ROW_08 = [1, 2, 1, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 2, 4, 1, 2, 2, 3, 1, 2, 3, 2, 1, 3, 2, 4, 1, 2, 2, 3, 1, 2, 3, 2, 4, 2, 1, 1, 3, 1, 4, 1, 3, 1, 3, 2, 1, 4, 1, 2]
ROW_09 = [1, 1, 3, 1, 3, 1, 1, 3, 2, 1, 1, 3, 2, 4, 2, 3, 2, 2, 2, 3, 2, 4, 2, 2, 1, 3, 1, 3, 2, 1, 1, 1, 3, 1, 3, 2, 1, 1, 4, 2, 1, 2, 3, 1, 2, 3, 2, 1, 4, 2, 1, 1, 3, 1, 4]
ROW_10 = [1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 1, 3, 1, 2, 1, 4, 2, 3, 2, 2, 2, 3, 2, 4, 1, 1, 1, 3, 1, 2, 2, 1, 3, 2, 2, 2, 3, 2, 3, 2, 3, 1, 3, 1, 2, 1, 3, 2, 1, 3, 1, 1, 3, 1, 2]
ROW_11 = [2, 2, 4, 1, 2, 1, 1, 3, 1, 3, 1, 1, 3, 2, 1, 1, 3, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 2, 4, 2, 1, 2, 1, 3, 2, 2, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 1, 2, 1, 1, 3, 1, 1, 2, 3]
ROW_12 = [2, 1, 1, 3, 1, 3, 1, 3, 1, 2, 1, 4, 1, 1, 3, 2, 1, 2, 3, 2, 2, 1, 1, 2, 2, 4, 2, 1, 1, 3, 1, 2, 3, 2, 4, 1, 1, 3, 1, 3, 2, 1, 1, 3, 1, 3, 1, 2, 1, 3, 1, 3, 1, 3, 2]
ROW_13 = [1, 2, 1, 1, 1, 2, 3, 1, 2, 1, 3, 1, 1, 3, 1, 2, 2, 2, 4, 2, 2, 1, 1, 3, 2, 2, 2, 3, 1, 1, 2, 4, 2, 2, 3, 2, 2, 2, 3, 1, 3, 2, 3, 1, 3, 2, 1, 4, 2, 2, 1, 1, 3, 1, 1]
ROW_14 = [3, 1, 2, 2, 2, 3, 2, 1, 4, 2, 2, 2, 3, 2, 2, 4, 1, 1, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 4, 2, 2, 1, 1, 3, 1, 1, 3, 2, 1, 2, 1, 3, 1, 1, 1, 1, 3, 2, 2, 1, 1]
ROW_15 = [3, 1, 3, 1, 2, 1, 1, 3, 1, 1, 2, 1, 4, 2, 1, 1, 3, 1, 4, 2, 1, 1, 1, 3, 1, 2, 3, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 2, 3, 1, 2, 3, 2, 1, 4, 2, 2, 1, 1, 3, 1]
ROW_16 = [1, 3, 1, 2, 2, 2, 3, 2, 1, 4, 2, 2, 2, 3, 1, 1, 1, 2, 3, 1, 3, 1, 2, 1, 3, 2, 3, 1, 1, 2, 3, 1, 1, 3, 2, 2, 1, 3, 1, 2, 3, 2, 1, 3, 2, 2, 1, 4, 2, 3, 1, 4, 2, 1, 2]
ROW_17 = [3, 1, 1, 3, 1, 3, 2, 2, 1, 1, 3, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 2, 4, 1, 2, 2, 1, 4, 2, 1, 1, 3, 1, 2, 3, 2, 4, 2, 2, 1, 3, 1, 3, 1, 2, 1, 1, 3, 2, 2, 2, 3, 2, 2, 2]
ROW_18 = [3, 1, 1, 2, 1, 4, 1, 2, 3, 1, 2, 1, 1, 3, 1, 2, 1, 1, 3, 1, 3, 1, 3, 2, 1, 4, 2, 2, 1, 1, 3, 2, 2, 2, 3, 1, 1, 2, 4, 2, 2, 3, 2, 2, 2, 3, 1, 3, 2, 3, 1, 3, 2, 1, 4]
ROW_19 = [1, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 3, 2, 1, 1, 3, 1, 3, 2, 1, 4, 2, 1, 1, 1, 3, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 3, 2, 1, 1, 3, 1, 3, 1, 3, 1, 2, 1, 1, 3, 2, 1]
ROW_20 = [1, 4, 2, 2, 2, 3, 1, 2, 2, 1, 4, 2, 1, 1, 3, 1, 4, 1, 1, 1, 2, 3, 1, 2, 1, 3, 1, 1, 2, 3, 2, 1, 2, 1, 3, 1, 1, 1, 1, 3, 2, 3, 1, 3, 2, 1, 4, 2, 1, 1, 3, 1, 1, 3, 1]
ROW_21 = [4, 1, 1, 1, 1, 3, 1, 3, 2, 4, 1, 1, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 3, 2, 3, 2, 1, 1, 1, 3, 1, 2, 1, 3, 2, 3, 2, 1, 3, 2, 2, 1, 3, 2, 3, 1, 2, 1, 2, 1, 2]

MATRIX = [ROW_01, ROW_02, ROW_03, ROW_04, ROW_05, ROW_06, ROW_07, ROW_08, ROW_09, ROW_10, ROW_11,
          ROW_12, ROW_13, ROW_14, ROW_15, ROW_16, ROW_17, ROW_18, ROW_19, ROW_20, ROW_21]


def add_pattern(dict, values_list):
    if dict.get(values_list):
        dict[values_list] = dict[values_list] + 1
    else:
        dict[values_list] = 1
    return dict


def count_values():
    distribution = {"1": 0, "2": 0, "3": 0, "4": 0}
    positions = {"1": [], "2": [], "3": [], "4": []}
    for idy in range(len(MATRIX)):
        for idx in range(len(MATRIX[0])):
            value = MATRIX[idy][idx]
            positions[str(value)].append((idx, idy))
            distribution[str(value)] = distribution[str(value)] + 1

    return positions, distribution


def store_pattern(x, y):
    pattern = {}
    for step_y in range(0, len(MATRIX), y):
        for step_x in range(0, len(MATRIX[step_y]), x):
            values = ""
            for idy in range(0, y):
                for idx in range(0, x):
                    x_value = step_x + idx
                    y_value = step_y + idy
                    print(y_value, x_value)
                    values = values + str(MATRIX[y_value][x_value])
            add_pattern(pattern, values)
    return pattern


import matplotlib.pyplot as plt
plt.imshow(MATRIX, interpolation="nearest", cmap='hot')
plt.show()


def flatten_matrix_h():
    matrix_flat_list = []
    for i in MATRIX:
        matrix_flat_list = matrix_flat_list + i
    return matrix_flat_list


def flatten_matrix_v():
    matrix_flat_list = []
    for x in range(len(MATRIX[0])):
        for y in range(len(MATRIX)):
            matrix_flat_list.append(MATRIX[y][x])
    return matrix_flat_list


def words_split_4s():
    a = flatten_matrix_h()
    split_word_dict = {}
    value_list = []
    for i in a:
        if i == 4:
            split_word_dict = add_pattern(split_word_dict, str(value_list))
            value_list = []
        else:
            value_list.append(i)
    split_word_dict = add_pattern(split_word_dict, str(value_list))

    return split_word_dict

def words_split_meta_data():
    dict = words_split_4s()
    for word in dict.keys():
        print(f"Seq: {word}, aantal: {dict[word]} len: {len(word)/3}")

def all_patterns_flat():
    h = flatten_matrix_h()
    v = flatten_matrix_v()
    compl_dict_h = {}
    compl_dict_v = {}
    for l in range(3, 11):
        dict_l = {}
        for b in range((len(h) // l) - 1):
            w = h[b * l: (b + 1) * l]
            dict_l = add_pattern(dict_l, str(w))
        compl_dict_h[l] = dict_l
    for l in range(3, 11):
        dict_l = {}
        for b in range((len(v) // l) - 1):
            w = v[b * l: (b + 1) * l]
            dict_l = add_pattern(dict_l, str(w))
        compl_dict_v[l] = dict_l

    return compl_dict_h, compl_dict_v


# pattern_5_1 = store_pattern(5, 1)
# pattern_5_3 = store_pattern(5, 3)
# pattern_1_3 = store_pattern(1, 3)
# pattern_1_7 = store_pattern(1, 7)
# pattern_5_7 = store_pattern(5, 7)
# pattern_11_1 = store_pattern(11, 1)
# pattern_11_3 = store_pattern(11, 3)
# pattern_11_7 = store_pattern(11, 7)
# print(len(pattern_5_1))
# print(len(pattern_5_3))
# print(len(pattern_1_3))
# print(len(pattern_1_7))
# print(len(pattern_5_7))
# print(len(pattern_11_1))
# print(len(pattern_11_3))
# print(len(pattern_11_7))


def repl_wrapper(matrix, pattern, char):
    for i in range(len(matrix)):
        if matrix[i] == pattern:
            matrix[i] = char
    return matrix


def matrix_in_3s():
    matrix = flatten_matrix_h()
    length = 3
    repl_matrix = []
    for s in range(len(matrix) // 3):
        repl_matrix.append(matrix[s * length: (s + 1) * length])
    return repl_matrix
