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

    def test_01(self):
        self.assertIsInstance(self.interpreter, Interpreter)

    def test_02(self):
        self.assertNotIsInstance(self.interpreter.graphs, Graph)

    def test_03(self):
        self.assertIsNot(self.interpreter.graphs, type(tuple(self.interpreter.graphs)))

    # This test should fail due to issues with "args" interpreter
    # noinspection PyArgumentList
    @unittest.expectedFailure
    def test_04(self):
        try:
            self.interpreter.do_display_data()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_05(self):
        try:
            self.interpreter.do_display_data("")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_06(self):
        try:
            self.interpreter.do_display_data("")
            self.assertTrue(True)
        except AttributeError:
            self.assertFalse(False)

    def test_07(self):
        try:
            self.interpreter.do_backup_database("file.txt")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_08(self):
        try:
            self.interpreter.do_get_data("select * from employee")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_09(self):
        try:
            self.interpreter.database.setup()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_10(self):
        try:
            self.interpreter.database.display_data()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_11(self):
        try:
            self.interpreter.database.commit()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_12(self):
        try:
            self.interpreter.database.write_to_database("")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_13(self):
        try:
            self.interpreter.database.backup_database()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_14(self):
        try:
            self.interpreter.database.commit()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_15(self):
        self.assertIsInstance(self.interpreter.graph, Graph)

    def test_16(self):
        self.assertIsInstance(self.interpreter.database, sql_database.SQLDatabase)

    def test_17(self):
        self.assertIsInstance(self.interpreter.database, interface_database.IDatabase)

    def test_18(self):
        self.assertIsInstance(self.interpreter.file_handler, filehandler.FileHandler)

    def test_19(self):
        self.assertIsInstance(self.interpreter.file_handler, interface_filehandler.IFileHandler)

    def test_20(self):
        self.interpreter.do_backup_database("test.db")
        self.assertFalse(os.path.isfile("default.db"))

    def test_21(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                        ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                        ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                        ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                        ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                        ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                        ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                        ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                        ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'),
                        ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                        ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                        ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                        ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                        ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                        ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                        ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]

        self.assertTrue(data != compare_data)

    def test_22(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                        ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                        ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                        ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                        ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                        ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                        ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                        ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                        ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'),
                        ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                        ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                        ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                        ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                        ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                        ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                        ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertTrue(data[1] == compare_data[1])

    def test_23(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                        ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                        ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                        ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                        ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                        ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                        ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                        ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                        ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'),
                        ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                        ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                        ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                        ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                        ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                        ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                        ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertFalse(data[1] == compare_data[3])

    def test_24(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                        ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                        ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                        ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                        ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                        ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                        ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                        ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                        ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'),
                        ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                        ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                        ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                        ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                        ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                        ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                        ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertIn(data[5], compare_data)

    def test_25(self):
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) == 1)

    def test_26(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) != 1)

    def test_27(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) != 1)

    def test_28(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(self.interpreter.graphs[0] != self.interpreter.graphs[1])

    def test_29(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(data_new != data)

    def test_30(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(len(data_new) != len(data))

    def test_31(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(len(data_new) == 0)

    def test_32(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertIsNot(data[2], data_new)

    def test_33(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(data[2] == data_new[2])

    def test_34(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        print("LENTGH" + str(len(data)))
        print("LENTGH" + str(len(data_new)))
        self.assertTrue(len(data) == 34 and len(data_new) == 0)

    # Assignment 2 Tests
    def test_35(self):
        print("Test 35")
        con1 = self.interpreter.database.connection
        self.interpreter.database.close_connection()
        con2 = self.interpreter.database.connection
        self.assertEqual(con1, con2)

    @should_raise(Exception, "\nFor a list of tables, type help.")
    def test_36(self):
        print("Test 36")
        self.interpreter.database.execute_sql("sss")

    @should_raise(TypeError, "Data is not correctly formatted")
    def test_37(self):
        print("Test 37")
        self.interpreter.database.write_to_database(None)

    @should_raise(IOError, "Directory Created")
    def test_38(self):
        print("Test 38")
        data = ['data1', 'data2']
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        if os.path.exists(realfiledirectory):
            shutil.rmtree(realfiledirectory)
        self.interpreter.file_handler.pickle_all(data)

    def test_39(self):
        print("Test 39")
        data = ['data1', 'data2']
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        self.interpreter.file_handler.pickle_all(data)
        realfilepath = realfiledirectory + "\\db_backup.dat"
        self.assertTrue(os.path.isfile(realfilepath))

    @should_raise(IOError, "Directory Created")
    def test_40(self):
        print("Test 40")
        self.interpreter.file_handler.unpack_pickle("g:\error")

    def test_41(self):
        print("Test 41")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie age")
        self.interpreter.do_create_graph("bar salary-by-gender")
        self.interpreter.do_create_graph("bar salary-by-age")
        print(len(self.interpreter.graphs))
        self.interpreter.file_handler.pack_pickle(self.interpreter.graphs)
        self.interpreter.graphs = []
        self.interpreter.graphs = self.interpreter.file_handler.unpack_pickle(
            os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat")
        print(len(self.interpreter.graphs))
        self.assertTrue(len(self.interpreter.graphs) == 5)

    @should_raise(IOError, "Directory Created")
    def test_42(self):
        print("Test 42")
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        shutil.rmtree(realfiledirectory)
        self.interpreter.file_handler.pack_pickle(self.interpreter.graphs)

    def test_43(self):
        print("Test 43")
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        shutil.rmtree(realfiledirectory)
        realfilepath = realfiledirectory + "\\pickle.dat"
        self.interpreter.file_handler.pack_pickle(self.interpreter.graphs)
        self.assertTrue(os.path.isfile(realfilepath))

    @should_raise(FileNotFoundError, "file does not exist.")
    def test_44(self):
        print("Test 44")
        self.interpreter.file_handler.load_file("g:/ccc")

    def test_45(self):
        print("Test 45")
        realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\file.txt"
        testcontent = self.interpreter.file_handler.load_file(realfilepath)
        self.assertEqual(len(testcontent), 16)

    def test_46(self):
        print("Test 46")
        realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\file.txt"
        realcontent = self.interpreter.file_handler.load_file(realfilepath)
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\file.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        self.interpreter.file_handler.write_file(testfilepath, realcontent)
        testcontent = self.interpreter.file_handler.load_file(testfilepath)
        self.assertEqual(realcontent, testcontent)

    def test_47(self):
        print("Test 47")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'Normal', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 1)

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

    # Check an salary to large is not validated
    def test_53(self):
        print("Test 53")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 2222, 'Normal', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

    # Check an bmi is validatied correctly
    def test_54(self):
        print("Test 54")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'ERROR', 100, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

    # Check an income is being validated as an not to large correctly
    def test_55(self):
        print("Test 55")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'Normal', 11111, '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

    # Check an income is being validated as an integer (not string) correctly
    def test_56(self):
        print("Test 56")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'Normal', 'ERROR', '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

    # Test interpreter.do_load_from_file works correctly for a single file path given
    def test_57(self):
        print("Test 57")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(testfilepath)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(capturedoutput.getvalue()[1:6], "'e01'")

    # Test interpreter.do_load_from_file works correctly for create graph option
    def test_58(self):
        print("Test 58")
        arggs = "-g " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[:14], "creating graph")

    # Test interpreter.do_load_from_file works correctly for load data base option
    def test_59(self):
        print("Test 59")
        arggs = "-d " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[1:6], "'e01'")

    # Test interpreter.do_load_from_file correctly error checks for INVALID option
    def test_60(self):
        print("Test 60")
        arggs = "-INVALID " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[:14], "Invalid option")

    # Test interpreter.do_load_from_file correctly error checks for INVALID option
    def test_61(self):
        print("Test 61")
        arggs = "-0"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])

    # Test interpreter
    def test_62(self):
        print("Test 62")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])

    # Test error check of file already exists in intepreter.do_backup_database works correctly
    def test_63(self):
        print("Test 63")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if not os.path.exists(testfilepath):
            newfile = open(testfilepath, 'w+')
            newfile.close()
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("File already exists", capturedoutput.getvalue())

    # Check of file already exists in intepreter.do_backup_database works correctly if the file does not exist
    def test_64(self):
        print("Test 64")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("True", capturedoutput.getvalue())

    # Test interpter do_back_database for proper option
    def test_65(self):
        print("Test 65")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(testfilepath)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("Incorrect option. Refer to help.", capturedoutput.getvalue())

    @should_raise(NotImplementedError)
    def test_66(self):
        testfilepath = ""
        interface_filehandler.IFileHandler.load_file(self, testfilepath)

    @should_raise(NotImplementedError)
    def test_67(self):
        testfilepath = ""
        data = ""
        interface_filehandler.IFileHandler.write_file(self, testfilepath, data)

    @should_raise(NotImplementedError)
    def test_68(self):
        data = ""
        interface_filehandler.IFileHandler.validate(self, data)

    @should_raise(NotImplementedError)
    def test_69(self):
        graphs = ""
        interface_filehandler.IFileHandler.pack_pickle(self, graphs)

    @should_raise(NotImplementedError)
    def test_70(self):
        file = ""
        interface_filehandler.IFileHandler.unpack_pickle(self, file)

    @should_raise(NotImplementedError)
    def test_71(self):
        data = ""
        interface_filehandler.IFileHandler.pickle_all(self, data)

    @should_raise(NotImplementedError)
    def test_72(self):
        sql = ""
        interface_database.IDatabase.execute_sql(self, sql)

    @should_raise(NotImplementedError)
    def test_73(self):
        interface_database.IDatabase.close_connection(self)

    @should_raise(NotImplementedError)
    def test_74(self):
        interface_database.IDatabase.commit(self)

    @should_raise(NotImplementedError)
    def test_75(self):
        interface_database.IDatabase.setup(self)

    @should_raise(NotImplementedError)
    def test_76(self):
        interface_database.IDatabase.reset(self)

    @should_raise(NotImplementedError)
    def test_77(self):
        interface_database.IDatabase.display_data(self)

    @should_raise(NotImplementedError)
    def test_78(self):
        data = ""
        interface_database.IDatabase.write_to_database(self, data)

    @should_raise(NotImplementedError)
    def test_79(self):
        interface_database.IDatabase.backup_database(self)

    def test_80(self):
        print("Test 80")

        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie age")
        self.interpreter.do_create_graph("bar salary-by-gender")
        self.interpreter.do_create_graph("bar salary-by-age")
        self.assertTrue(len(self.interpreter.graphs) == 5)

    def test_81(self):
        print("Test 81")
        args = "pie bmi"
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.graph.print_graph(self.interpreter.graphs[0])
        self.assertRaises(TypeError, testgraph=self.interpreter.graph.build_graph(args))

    def test_82(self):
        print("Test 82")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.graph.print_graph(self.interpreter.graphs[0])

    def test_83(self):
        print("Test 83")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("bar salary-by-age")
        self.interpreter.graph.print_graph(self.interpreter.graphs[0])

    def test_84(self):
        print("Test 41")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("bar salary-by-gender")
        self.interpreter.graph.print_graph(self.interpreter.graphs[0])

    @should_raise(TypeError, "This functions takes exactly one parameters")
    def test_85(self):
        print("Test 85")
        args = ["pie", "sex", "age"]
        self.interpreter.graph.build_graph(args)

    def test_86(self):
        print("Test 86")
        self.interpreter.graphs = []
        args = ["pie", "error"]
        self.interpreter.graph.build_graph(args)

    # Check an income is being validated as an integer (not string) correctly
    def test_87(self):
        print("Test 87")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        testdata = [('e01', 'm', 17, 222, 'Normal', 'ERROR', '12-06-2000')]
        self.interpreter.file_handler.write_file(testfilepath, testdata)
        testfiledata = self.interpreter.file_handler.load_file(testfilepath)
        testdata = self.interpreter.file_handler.validate(testfiledata)
        print(testdata)
        self.assertEqual(len(testdata), 0)

    # Test interpreter.do_load_from_file works correctly for a single file path given
    def test_88(self):
        print("Test 88")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(testfilepath)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(capturedoutput.getvalue()[1:6], "'e01'")

    # Test interpreter.do_load_from_file works correctly for create graph option
    def test_89(self):
        print("Test 89")
        arggs = "-g " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[:14], "creating graph")

    # Test interpreter.do_load_from_file works correctly for load data base option
    def test_90(self):
        print("Test 90")
        arggs = "-d " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[1:6], "'e01'")

    # Test interpreter.do_load_from_file correctly error checks for INVALID option
    def test_91(self):
        print("Test 91")
        arggs = "-0"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])

    # Test interpreter.do_load_from_file correctly error checks for INVALID option
    def test_92(self):
        print("Test 92")
        arggs = "-INVALID " + os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\validationtestfile.txt"
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_load_from_file(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])
        self.assertEqual(capturedoutput.getvalue()[:14], "Invalid option")

    # Test interpreter
    def test_93(self):
        print("Test 93")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        print(capturedoutput.getvalue()[:14])

    # Test error check of file already exists in intepreter.do_backup_database works correctly
    def test_94(self):
        print("Test 94")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if not os.path.exists(testfilepath):
            newfile = open(testfilepath, 'w+')
            newfile.close()
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("File already exists", capturedoutput.getvalue())

    # Test error check of file already exists in intepreter.do_backup_database
    def test_95(self):
        print("Test 95")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        arggs = "-o " + testfilepath
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(arggs)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("True", capturedoutput.getvalue())

    # Test interpter do_back_database for proper option
    def test_96(self):
        print("Test 96")
        testfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\testfiles\\testbackupfile.txt"
        if os.path.exists(testfilepath):
            os.remove(testfilepath)
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_backup_database(testfilepath)
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("Incorrect option. Refer to help.", capturedoutput.getvalue())

    # Graph args are wrong
    @should_raise(ValueError, 'Ensure Graph Value Option Parameter is correctly spelt')
    def test_97(self):
        print("Test 97")
        args = "pie error"
        self.interpreter.do_display_graph(args, None)

    #  Graph to many args
    @should_raise(TypeError, 'This functions takes exactly one parameters')
    def test_98(self):
        print("Test 98")
        args = "pie age error"
        self.interpreter.do_display_graph(args, None)

    def test_99(self):
        print("Test 99")
        args = "pie age"
        self.interpreter.do_display_graph(args, None)

    def test_100(self):
        print("Test 100")
        args = "pie age"
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.do_display_graph(args, self.interpreter.graphs[0])

    @should_raise(TypeError, 'This functions takes exactly two parameters')
    def test_101(self):
        print("Test 101")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi error")

    @should_raise(ValueError, 'Ensure Parameters are correctly spelt')
    def test_102(self):
        print("Test 102")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie error")

    # Incorrect spelling on input args
    @should_raise(ValueError, 'Ensure Parameters are correctly spelt')
    def test_103(self):
        print("Test 103")
        self.interpreter.graphs = []
        self.interpreter.do_list_graphs("error")

    # Incorrect amount of input args
    @should_raise(TypeError, 'This functions takes exactly one or no parameters')
    def test_104(self):
        print("Test 104")
        self.interpreter.graphs = []
        self.interpreter.do_list_graphs("pie bmi")

    # There are no graphs to list
    @should_raise(IndexError, 'There are currently no graphs loaded')
    def test_105(self):
        print("Test 105")
        self.interpreter.graphs = []
        self.interpreter.do_list_graphs("")

    @should_raise(ValueError, 'There is currently no graphs to be saved')
    def test_106(self):
        print("Test 106")
        self.interpreter.graphs = []
        self.interpreter.do_save_graphs(self.interpreter.graphs)

    def test_107(self):
        print("Test 107")
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        realfilepath = realfiledirectory + "\\pickle.dat"
        os.remove(realfilepath)
        self.interpreter.do_save_graphs(self.interpreter.graphs)
        self.assertTrue(os.path.isfile(realfilepath))

    def test_108(self):
        print("Test 108")
        self.interpreter.graphs = []
        self.interpreter.do_load_graphs("")
        self.assertTrue(len(self.interpreter.graphs) > 0)

    def test_109(self):
        print("Test 109")
        realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
        realfilepath = realfiledirectory + "\\db_backup.dat"
        if os.path.exists(realfilepath):
            os.remove(realfilepath)
        self.interpreter.graphs = []
        self.interpreter.do_create_graph("pie bmi")
        self.interpreter.do_pickle(self.interpreter.graphs)
        self.assertTrue(os.path.isfile(realfilepath))

    @should_raise(SystemExit)
    def test_110(self):
        print("Test 110")
        self.interpreter.do_quit("")

    def test_111(self):
        print("Test 111")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.do_about("")
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Welcome to")

    def test_112(self):
        print("Test 112")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_load_from_file()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Load data ")

    def test_113(self):
        print("Test 113")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_display_data()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Display da")

    def test_114(self):
        print("Test 114")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_load_from_file()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Load data ")

    def test_115(self):
        print("Test 115")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_backup_database()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "This comma")

    def test_116(self):
        print("Test 116")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_create_graph()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Create a b")

    def test_117(self):
        print("Test 117")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_display_graph()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Create a b")

    def test_118(self):
        print("Test 118")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_list_graphs()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Display a ")

    def test_119(self):
        print("Test 119")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_load_graphs()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Load graph")

    def test_120(self):
        print("Test 120")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_save_graphs()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Save exist")

    def test_121(self):
        print("Test 121")
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.interpreter.help_pickle()
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(capturedoutput.getvalue()[:10], "Encrypt da")

    def test_122(self):
        print("Test 122")
        testraise = False
        self.interpreter.emptyline()
        self.assertFalse(testraise)

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
