import unittest
from conversions import *


class TestConversion(unittest.TestCase):


    def test_octal_to_decimal_after_coma(self):
        #self.assertAlmostEqual(octal_to_decimal_after_coma("123"), 0.162109375)
        ##self.assertAlmostEqual(octal_to_decimal_before_coma("123"),83)
        #self.assertAlmostEqual(octal_to_decimal("123.567"), "83.732")
        #self.assertAlmostEqual(decimal_to_hexa_before_coma(19232), "4B20")
        #self.assertAlmostEqual(decimal_to_binary_before_coma("156423"), "100110001100000111")

        self.assertAlmostEqual(convertir(12321.32121), ["5329.408", "1010011010001.011", "14D1.68A" ])


