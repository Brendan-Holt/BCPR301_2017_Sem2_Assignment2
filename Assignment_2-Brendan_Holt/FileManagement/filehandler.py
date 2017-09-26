from FileManagement.interface_filehandler import *
# Brendan
import pickle
import os
import sys
import math
# kate
import re
from datetime import *


# Kris Little design
class FileHandler(IFileHandler):
    def __init__(self):
        self.valid = True

    # Kris
    def load_file(self, file):
        # put error handling here
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)
            the_file.close()
            return contents

    # Kris
    def write_file(self, file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for i in range(len(new_data)):
                string += str(new_data[i])
                # prevent a space at the end of a line
                if i != len(new_data) - 1:
                    string += ','

            string += "\n"
        the_file.write(string)
        the_file.close()


    # Validate file data
    def validate_format(self, person, feedback):
        validationcondition = True
        # check the format is a letter and 3 digit e.g A002 or a002
        if re.match(r'[a-z][0-9]{2}', person[0].lower()):
            # Kris
            if len(str(person[0])) >= 5:
                validationcondition = False
        else:
            # Kris
            feedback += "ID is incorrect; must contain a letter and 3 digits e.g. a001.\n"
            validationcondition = False
        return validationcondition

    def validate_gender(self, person, feedback):
        validationcondition = True
        if person[1].upper() == "M" or (person[1]).upper() == "F":
            print(person[1])
        else:
            # Kris
            feedback += "Incorect Gender; must be M or F.\n"
            validationcondition = False
        return validationcondition

    def validate_age(self, person, feedback):
        validationcondition = True
        date_correct = True

        try:
            datetime.strptime(person[6], "%d-%m-%Y")
        except ValueError:
            date_correct = False
            feedback += "Date is not corrent format! " + str(person[6])
            validationcondition = False

        if date_correct:
            the_date = datetime.strptime(person[6], "%d-%m-%Y")
            test_age = math.floor(((datetime.today() - the_date).days / 365))
            if test_age == int(person[2]):
                pass
            else:
                validationcondition = False
                feedback += "Age and birthday does not match. " + str(test_age) + ":" + str(int(person[2]))
        return validationcondition

    def validate_sales(self, person, feedback):
        validationcondition = True
        if re.match(r'^[0-9]{2,3}$', person[3]):
            print("ccc " + person[3])
        else:
            feedback += "Incorrect sales number; must be a 3 digit whole number. \n"
            validationcondition = False
        return validationcondition

    def validate_bmi(self, person, feedback):
        validationcondition = True
        if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (person[4]).upper()):
            print(person[4])
        else:
            feedback += "Incorrect BMI value; Choose from Normal, Overweight, Obesity or Underweight. \n"
            validationcondition = False
        return validationcondition

    def validate_income(self, person, feedback):
        validationcondition = True
        # check Income is float
        try:

            if int(person[5]):
                if len(str(int(person[5]))) > 3:
                    feedback += "Income is too large."
                    validationcondition = False
                else:
                    pass
            else:
                feedback += "Incorrect income; must be an integer number. \n" + str(person[5])
                validationcondition = False
        except ValueError:
            validationcondition = False
        return validationcondition

    def validate(self, data):
        """ TestCase for validate
        >>> aFileHandler = FileHandler()
        >>> aFileHandler.validate([("e01","m","20","20","Normal","200","12-06-1998")])
        invalidate data: e01
        invalidate data: m
        invalidate data: 20
        invalidate data: 20
        invalidate data: Normal
        invalidate data: 200
        invalidate data: 12-06-1998

        """
        add_to = []
        feedback = ""
        for person in data:
            feedback += "Feedback for data at: " + str(data.index(person) + 1) + "\n"
            self.valid = True
            print(person)
            # check the format is a letter and 3 digit e.g A002 or a002
            self.valid = self.validate_format(person, feedback)
            # check the format is either M/F/Male/Female
            if self.valid:
                self.valid = self.validate_gender(person, feedback)
            if self.valid:
                self.valid = self.validate_age(person, feedback)
            if self.valid:
                self.valid = self.validate_sales(person, feedback)
            if self.valid:
                self.valid = self.validate_bmi(person, feedback)
            if self.valid:
                self.valid = self.validate_income(person, feedback)
            if self.valid:
                add_to.append(person)
                feedback += "Passed and added to database.\n"
            else:
                feedback += '\n\n'
        print(feedback)
        return add_to

    # Brendan Holt
    # Used to pickle the loaded graphs to default pickle file
    def pack_pickle(self, graphs):
        # Raises exception if for some reason the default folder has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if not os.path.exists(realfiledirectory):
                raise IOError
        except IOError:
            print("Directory Created")
            os.makedirs(os.path.dirname(realfiledirectory))
            pass
        # The pickle process
        pickleout = open(realfiledirectory + "\\pickle.dat", "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

    # Brendan Holt
    # Used to unpickle graphs in the pickle file and return them to the interpreters graph list
    def unpack_pickle(self, filepath):
        # Raises exception if for some reason the file does not exist
        try:
            if os.path.exists(filepath) is False:
                raise IOError
        except IOError:
            print('File does not exits')
            return
        # The unpickle process
        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()
        # Return the graphs to the interpreter
        return graphs

    # Brendan Holt
    # Used to pickle the entire database to default pickle file
    def pickle_all(self, data):
        # Raises exception if for some reason the default file has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError
        except IOError:
            print('Directory Created')
            os.makedirs(os.path.dirname(realfiledirectory))
            return
        # The pickle process
        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()
