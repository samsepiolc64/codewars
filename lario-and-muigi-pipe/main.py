import numpy as np

def pipe_fix(nums):
    arr = np.arange(start=np.amin(nums), stop=np.amax(nums)+1)
    return arr



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr=pipe_fix([3,4,1,5,6])
    print(list(arr))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
