from . import person

class Teacher(person.Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course


    def printNameCourse(self):
        """ Print full name and subject
        """
        print(str(self.firstname) + ' ' + str(self.lastname) + ', ' + str(self.course))
        return None
