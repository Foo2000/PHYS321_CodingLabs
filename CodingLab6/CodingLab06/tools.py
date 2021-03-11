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

def test_reading_HT_data(self): 
    #change the size of the array to [self.n][3]
    self.rand_array = np.random.normal(size=(self.n,self.n,self.n))
    # Tests the reading_HT_data array size as compared to the original
    output_arr = tools.reading_HT_data(self.rand_array)
    nt.assert_equal(output_arr.shape, (self.n, self.n, self.n))

    # Tests time correctness of reading_HT_data in the first
    # instance in the array
    test_arr = np.array([[2000, -25, 1], [1973, -23, 3]])
    output_arr = tools.reading_HT_data(test_arr)
    nt.assert_equal(output_arr[0][0], (2000-1973)*366.242)