# The two unit tests are inside this function
def test_reading_HT_data(self):
        # change the size of the array to [self.n][3]
        self.rand_array = np.random.normal(size=(self.n,self.n,self.n))
        # Tests the reading_HT_data array size as compared to the original
        output_arr = tools.reading_HT_data(self.rand_array)
        nt.assert_equal(output_arr.shape, (self.n, self.n, self.n))

        # Tests time correctness of reading_HT_data in the first
        # instance in the array
        test_arr = np.array([[2000, -25, 1], [1973, -23, 3]])
        output_arr = tools.reading_HT_data(test_arr)
        nt.assert_equal(output_arr[0][0], (2000-1973)*366.242)