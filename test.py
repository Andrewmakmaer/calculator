import unittest
from calcul import main


class TestAddCase(unittest.TestCase):
    def test_1(self):
        res = main("1+3*(4-2)")
        self.assertEqual(res, 7)

    def test_2(self):
        res = main("(5-1)*10/2-(3+4)")
        self.assertEqual(res, 13)

    def test_3(self):
        res = main("(5-5)*10/2-(3+4)")
        self.assertEqual(res, -7)

    def test_4(self):
        res = main("11-10*((3-1)+10/2)")
        self.assertEqual(res, -59)

    def test_5(self):
        res = main("10*0.5+2")
        self.assertEqual(res, 7)

    def test_division_by_zero(self):
        res = main("1/0")
        self.assertEqual(res, "Error, division by zero was formed during execution")

    def test_division_by_zero_second(self):
        res = main("2+3/(5-5)")
        self.assertEqual(res, "Error, division by zero was formed during execution")

    def test_6(self):
        res = main("12+1*-8")
        self.assertEqual(res, "Input Error")

    def test_7(self):
        res = main("2+((1)-2")
        self.assertEqual(res, "Input Error")

    def test_8(self):
        res = main("ab+13*1")
        self.assertEqual(res, "Input Error")

    def test_9(self):
        res = main("12- 56 * (-1)")
        self.assertEqual(res, 68)

    def test_10(self):
        res = main("10 +12(*5)")
        self.assertEqual(res, "Input Error")

    def test_11(self):
        res = main("10 + (-25*10) / 10+11-(+13-11)")
        self.assertEqual(res, -6)

    def test_12(self):
        res = main("+10 - 5")
        self.assertEqual(res, "Input Error")

    def test_13(self):
        res = main("(-(-5+8)+2)")
        self.assertEqual(res, -1)

    def test_14(self):
        res = main("((2*1)+(3+3))")
        self.assertEqual(res, 8)

    def test_15(self):
        res = main("((12*2)*2 + (-10-5)/5)")
        self.assertEqual(res, 45)

    def test_17(self):
        res = main("(*10)-2")
        self.assertEqual(res, "Input Error")

    def test_18(self):
        res = main("2(10)")
        self.assertEqual(res, 20)
    
    def test_19(self):
        res = main("3+2(5+5)")
        self.assertEqual(res, 23)

    def test_20(self):
        res = main("6/2(2+1)")
        self.assertEqual(res, 9)

    def test_21(self):
        res = main("2+(-)")
        self.assertEqual(res, "Input Error")

    def test_22(self):
        res = main("()")
        self.assertEqual(res, 0)

    def test_23(self):
        res = main("3 + ()")
        self.assertEqual(res, 3)

    def test_24(self):
        res = main(")(")
        self.assertEqual(res, "Input Error")

    def test_25(self):
        res = main("3 + )( +1")
        self.assertEqual(res, "Input Error")


if __name__ == '__main__':
    unittest.main()
