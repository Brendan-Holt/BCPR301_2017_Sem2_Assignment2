import matplotlib.pyplot as plt
import getopt
import time


# design kris, coded by Brendan

class Graph:

    def __init__(self, database):
        self.data1 = []
        self.database = database
        # NEW Brendan
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.title = None
        self.type = None
        self.option = None
        self.labels = None
        self.angle = None
        self.time = None

    # Brendan Holt
    # Outputs and graph loaded in the iterpretors graph list that has been passed into the input parameters
    @staticmethod
    def print_graph(graph):
        colours = ['c', 'm', 'r', 'k']
        # If the graph is a pie graphs
        if graph.type == 'pie':
            plt.pie(graph.data1, labels=graph.labels, colors=colours, startangle=90)
        # If the graph is a bar graph
        else:
            # Load additional information used in a bar graph
            if graph.option == 'salary-by-gender':
                mx = [1, 3, 5, 7]
                wx = [2, 4, 6, 8]
                xl = [1.5, 3.5, 5.5, 7.5]
                plt.bar(mx, graph.data1, color='blue')
                plt.bar(wx, graph.data2, color='red')
                plt.xticks(xl, graph.labels, rotation='vertical')
            else:
                aa = [1, 6, 11, 16]
                ab = [2, 7, 12, 17]
                ac = [3, 8, 13, 18]
                ad = [4, 9, 14, 19]
                xl = [2.5, 7.5, 12.5, 17.5]
                plt.bar(aa, graph.data1, color='blue')
                plt.bar(ab, graph.data2, color='red')
                plt.bar(ac, graph.data3, color='green')
                plt.bar(ad, graph.data4, color='yellow')
                plt.xticks(xl, graph.labels, rotation='horizontal')
        plt.title(graph.title)
        plt.show()

    def attach(self, sql):
        self.database.execute_sql(sql)
        return self.database.cursor.fetchall()

    def get_gender_data(self, g):
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE gender = 'M'""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE gender = 'F'""")))
        g.labels = ['Male', 'Female']
        g.title = "Employees by sex"
        g.type = "pie"
        g.option = "gender"

    def get_bmi_data(self, g):
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE BMI = 'Underweight'""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE BMI = 'Normal'""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE BMI = 'Overweight'""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE BMI = 'Obesity'""")))
        g.labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
        g.title = "Employees by BMI"
        g.type = "pie"
        g.option = "bmi"

    def get_age_data(self, g):
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE age < 25""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE age BETWEEN 26 AND 40""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE age BETWEEN 41 AND 50""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE age > 51""")))
        g.labels = ['Under 25', '25 to 40', '41 to 50', 'Over 51']
        g.title = "Employees by age"
        g.type = "pie"
        g.option = "age"

    def get_salary_by_gender_data(self, g):
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'm' AND Salary<125""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 126 AND 150""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 151 AND 175""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 176 AND 200""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'f' AND Salary<125""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 126 AND 150""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 151 AND 175""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 176 AND 200""")))
        g.labels = ['<125K', '126-150K', '151-175K', '176-200K']
        g.title = "Salary by Gender"
        g.type = "bar"
        g.option = "salary-by-gender"

    def get_salary_by_age_data(self, g):
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary<125""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 126 AND 150""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 151 AND 175""")))
        g.data1.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 176 AND 200""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary<125""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 126 AND 150""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 151 AND 175""")))
        g.data2.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 176 AND 200""")))
        g.data3.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary<125""")))
        g.data3.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 126 AND 150""")))
        g.data3.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 151 AND 175""")))
        g.data3.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 176 AND 200""")))
        g.data4.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary<125""")))
        g.data4.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 126 AND 150""")))
        g.data4.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 151 AND 175""")))
        g.data4.append(len(self.attach("""SELECT * FROM employee WHERE Age < 26 AND Salary BETWEEN 176 AND 200""")))
        g.labels = ['<25', '26-40K', '40-50', '>50']
        g.title = "Salaries by Age"
        g.type = "bar"
        g.option = "salary-by-age"

    # Brendan Holt
    # Builds a graph, called from create_graph in the interpreter
    def build_graph(self, args):
        try:
            argss = []
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            # If new graph is none then create argss as regular else append args from create_graph
            argss.append(args[1][0])
            argss.append(args[1][1])
            # Raised exception if args are typed incorrectly
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' and argss[1] != 'age' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender' and argss[1] != 'salary-by-age':
                raise ValueError
        except ValueError:
            print('Ensure Graph Value Option Parameter is correctly spelt')
            return

        database = self.database
        new_graph = Graph(database)
        # The following called the database to build the graph
        if argss[0] == 'pie':
            if argss[1] == 'gender':
                self.get_gender_data(new_graph)
            elif argss[1] == 'bmi':
                self.get_bmi_data(new_graph)
            else:
                self.get_age_data(new_graph)
        elif argss[0] == 'bar':
            if argss[1] == 'salary-by-gender':
                self.get_salary_by_gender_data(new_graph)
            if argss[1] == 'salary-by-age':
                self.get_salary_by_age_data(new_graph)

        new_graph.angle = None
        # Time is used when calling do_list_graphs from interpreter
        new_graph.time = time.strftime(": Create at %H:%M - Date %d/%m/%y")
        return new_graph
