import unittest
import os.path
import shutil
import io
from interpreter import *
from Database import interface_database
from FileManagement import interface_filehandler, filehandler
from testfixtures import should_raise


class MainTests(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter("testdb")
        data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]

        self.interpreter.database.write_to_database(data)

    def tearDown(self):
        # be executed after each test case
        print('down')

    def test_48(self):
        print("Test 48")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e00001', 'm', 17, 222, 'Normal', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)


    def test_49(self):
        print("Test 49")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('ERROR', 'm', 17, 222, 'Normal', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)


    def test_50(self):
        print("Test 50")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'ERROR', 17, 222, 'Normal', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)


    # Check Date Format (date year is misplaced)
    def test_51(self):
        print("Test 51")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 22, 'Normal', 100, '2000-12-06')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)


    # Check correctly validates age and birthday are in compliance with each other (birthday does not match age)
    def test_52(self):
        print("Test 52")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'Normal', 100, '12-06-2001')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()