class Trees:

    def __init__(self):
        self.possible_solutions = []
        self.total_squares = 144
        self.no_of_trees = 4

    def find_tree_rows(self):
        no_squares = 24
        current_row = [1, 2]
        depth = 0
        self.rec_search(no_squares, current_row, depth)

    def possible_rows(self, current_row):
        poss_row_lengths = []
        if current_row[-1] != current_row[-2]:
            poss_row_lengths.append(current_row[-1])
        poss_row_lengths = poss_row_lengths + [current_row[-1] + 1, current_row[-1] + 2]
        return poss_row_lengths

    def rec_search(self, no_squares, current_row, depth):
        ret_value = None
        depth += 1

        if sum(current_row) == no_squares:

            self.possible_solutions.append(current_row[:])
            return True
        elif sum(current_row) > no_squares:
            return False
        else:
            poss_rows = self.possible_rows(current_row)
            for i in poss_rows:
                current_row.append(i)
                ret_value = self.rec_search(no_squares, current_row, depth)
                del current_row[-1]
        return ret_value


a = Trees()
a.find_tree_rows()
print(a.possible_solutions)
