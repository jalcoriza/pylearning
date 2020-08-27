#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
#   Unit tests for Feature: "analyse"
#
import unittest
from analyse import testAnalyse
#
#   class that defines the tests
#
class AnalyseTestCase(unittest.TestCase):

    def setUp(self):
        return
        
    def tearDown(self):
        return
        
    def testEmptyList(self):
        result = testAnalyse([])
        self.assertEqual(result,(None,None,0,0))

    def testListOfOne(self):
        result = testAnalyse([1])
        self.assertEqual(result,(1,1,1.0,1.0))

    def testListOfTwo(self):
        result = testAnalyse([1.0,2.0])
        self.assertEqual(result,(1.0,2.0,1.5,3.0))

    def testListOfTen(self):
        result = testAnalyse([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
        self.assertEqual(result,(1.0,10.0,5.5,55.0))
#
#   create a test suite
#
analyseTestSuite = unittest.TestSuite()
#
#   add the tests to this suits
#
analyseTestSuite.addTest(AnalyseTestCase("testEmptyList"))
analyseTestSuite.addTest(AnalyseTestCase("testListOfOne"))
analyseTestSuite.addTest(AnalyseTestCase("testListOfTwo"))
analyseTestSuite.addTest(AnalyseTestCase("testListOfTen"))
#
#   create test runner and run the test suite
#
runner = unittest.TextTestRunner()
runner.run(analyseTestSuite)
