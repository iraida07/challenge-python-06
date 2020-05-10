def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def division(x):
        return int(x / n)
    return division
    


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.results = [6, 20, 3]

        def test_closure_make_division_by(self):
            divisors = [3, 5, 18]
            dividents = [18, 100, 54]

            for result, divisor, divident in zip(self.results, divisors, dividents):
                division_by_divisor = make_division_by(divisor)
                self.assertEqual(result, division_by_divisor(divident))       

        def tearDown(self):
            del(self.results)

    unittest.main()       

    run()
