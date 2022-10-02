from random import randint


def mk_table(min_size, max_size):  # makes random table of booleans
    n = randint(min_size, max_size)
    m = randint(min_size, max_size)
    table = []

    for i in range(n):
        table.append([])
        for j in range(m):
            if randint(0, 1):
                table[i].append(True)
            else:
                table[i].append(False)

    return table

def find_sqr(min_size, max_size):  # finds the biggest square of Trues in random table of booleans
    # min_size = int(input('Minimum size of table: '))
    # max_size = int(input('Maximum size of table: '))
    table = mk_table(min_size, max_size)
    pot_sqrs = []  # potential_squares: pot_sqrs[length of one side][n] = list of m = start of potential peace of a square
    sqrs = [[0, 0]]  # squares: index = length of one side; n, m = table[n][m] (coordinates of top left corners)

    for n in range(len(table)):
        row = table[n]
        length = 0
        print(row)

        for m in range(len(row)):
            cell = row[m]
            print(cell)

            if cell:
                length += 1
                while (len(sqrs) - 1) < length:
                    print('1')
                    sqrs.append([])
                while (len(pot_sqrs) - 1) < length:
                    print('2')
                    pot_sqrs.append([])
                for k in range(len(pot_sqrs)):
                    print(3)
                    cur_list = pot_sqrs[k]
                    while (len(cur_list) - 1) < n:
                        print(4, len(cur_list), cur_list, pot_sqrs[k])
                        if not sqrs[k]:
                            cur_list.append([])
                        else:
                            break
                not_len = length
                while not_len:
                    print('5')
                    if not sqrs[not_len]:
                        pot_sqrs[not_len][n].append(m - (not_len - 1))
                    not_len -= 1
            else:
                print('0')
                length = 0

    print(table, '\n', pot_sqrs, sqrs)

find_sqr(5, 5)