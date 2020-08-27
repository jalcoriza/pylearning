#
#   Unit tests for Feature: "Calculator"
#

import unittest
from calculator import calculator

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator("The calculator")
        
    def tearDown(self):
        self.calculator.dispose()
        self.calculator = None

        
        
    def testPerformCalculation0001(self):
        self.calculator.runTest(0,'',0)
        self.assertEqual(str(self.calculator.msg),"Operator must one of be +-/*")


    def testPerformCalculation0002(self):
        self.calculator.runTest(1,'',0)
        self.assertEqual(str(self.calculator.msg),"Operator must one of be +-/*")


    def testPerformCalculation0003(self):
        self.calculator.runTest(1,'+',0)
        self.assertEqual(str(self.calculator.result),"1")


    def testPerformCalculation0004(self):
        self.calculator.runTest('abc','+',1)
        self.assertEqual(str(self.calculator.msg),"TypeError")


    def testPerformCalculation0005(self):
        self.calculator.runTest(1,'+','pqr')
        self.assertEqual(str(self.calculator.msg),"TypeError")


    def testPerformCalculation0006(self):
        self.calculator.runTest(1,'x',1)
        self.assertEqual(str(self.calculator.msg),"Operator must one of be +-/*")


    def testPerformCalculation0007(self):
        self.calculator.runTest(-1000000000.000001,'+',1)
        self.assertEqual(str(self.calculator.result),"-999999999.000001")


    def testPerformCalculation0008(self):
        self.calculator.runTest(1000000000.000001,'+',1)
        self.assertEqual(str(self.calculator.result),"1000000001.000001")


    def testPerformCalculation0009(self):
        self.calculator.runTest(1,'+',-1000000000.000001)
        self.assertEqual(str(self.calculator.result),"-999999999.000001")


    def testPerformCalculation0010(self):
        self.calculator.runTest(1,'+',1000000000.000001)
        self.assertEqual(str(self.calculator.result),"1000000001.000001")


    def testPerformCalculation0011(self):
        self.calculator.runTest(-1000000000.00000,'+',-1000000000.00000)
        self.assertEqual(str(self.calculator.result),"-2000000000.0")


    def testPerformCalculation0012(self):
        self.calculator.runTest(1000000000.00000,'+',1000000000.00000)
        self.assertEqual(str(self.calculator.result),"2000000000.0")


    def testPerformCalculation0013(self):
        self.calculator.runTest(1,'-',1)
        self.assertEqual(str(self.calculator.result),"0")


    def testPerformCalculation0014(self):
        self.calculator.runTest(1,'*',1)
        self.assertEqual(str(self.calculator.result),"1")


    def testPerformCalculation0015(self):
        self.calculator.runTest(1,'/',1)
        self.assertEqual(str(self.calculator.result),"1.0")


calculatorTestSuite = unittest.TestSuite()


calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0001"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0002"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0003"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0004"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0005"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0006"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0007"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0008"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0009"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0010"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0011"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0012"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0013"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0014"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0015"))


runner = unittest.TextTestRunner()
runner.run(calculatorTestSuite)
