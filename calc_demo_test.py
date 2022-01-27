import unittest

from demo.calc_demo import calculator


class testCalculator(unittest.TestCase):
    
    def testAdd(self):
        calci = calculator()
        self.assertEqual(calci.add(3,4),7)
    def testSub(self):
        calci = calculator()
        self.assertEqual(calci.sub(4,3),1)
    def testMult(self):
        calci = calculator()
        self.assertEqual(calci.mult(3,4),12)
    def testDiv(self):
        calci = calculator()
        self.assertEqual(calci.div(6,2),3)
