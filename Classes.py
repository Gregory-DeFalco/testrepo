

class Student:

    #default constructor
    def __init__(self, name, year, id):

        self.name = name
        self.year = year
        self.id = id

    def setname(self):
        self.name = input('Enter the Name of Student')

    def setyear(self):
        self.year = input('Enter Year of Student')

    def setid(self):
        self.id = input('Enter Student id')

    def PrintInfo(self):
        print('Name: %s \nYear: %s \n ID: %d \n' % (self.name, self.year, self.id))


class Engineer(Student):
        def __init__(self, name, year, id):
            super().__init__(name, year, id)

            self.testscores = []

        def setscores(self):
            list = []
            i = 0.0
            while i != -1:
                i = float(input('Enter Grade, or -1 to finish'))
                if i >= 0:
                    list.append(i)
            self.testscores = list


        def PrintEng(self):
            print('Name: %s \nYear: %s \n ID: %d \n ' % (self.name, self.year, self.id))
            print('Grades : ', self.testscores)




Dillon = Engineer("Dillon", "Sophomore", 123)

Dillon.setscores()

Dillon.PrintEng()
