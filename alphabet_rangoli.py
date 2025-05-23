# Exercise: Alphabet Rangoli
# URL: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Description: Print an alphabet rangoli of size of a given integer N

def print_rangoli(size):
    rows = []
    for i in range(size):
        s = '-'.join(chr(97 + size - 1 - j) for j in range(i + 1))
        rows.append(s.center(4 * size - 3, '-'))
    print('\n'.join(rows + rows[-2::-1]))
