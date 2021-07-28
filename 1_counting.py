


import numpy as np


if __name__ == "__main__":
    #size
    N = int(input())
    str = ''
    for i in range(N):
        str += input()


    elements = list(str)

    count = 0
    for ele in elements:
        if ele == 'G':
            count += 1

    print(count)





