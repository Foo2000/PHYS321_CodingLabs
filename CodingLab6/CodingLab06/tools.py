import numpy as np

def square(arr):
    return arr**2

def get_pi():
    return np.pi

def picky(num):
    if not isinstance(num, (np.float, float, np.int, int)):
        raise TypeError("Must input a number")

def reading_HT_data():
    # read the data
    HT_data = np.genfromtxt('HT.dat',delimiter=',').T
    # recenter the time coordinates assuming that observations started in  1973
    HT_data[0] = HT_data[0] - 1973
    # convert solar year into sidereal days
    HT_data[0] = HT_data[0] * 366.242
    # convert seconds into sidereal days
    HT_data[1] = HT_data[1] / 86164.1
    HT_data[2] = HT_data[2] / 86164.1
    return HT_data
