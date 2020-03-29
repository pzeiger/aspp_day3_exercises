from . import person

class Student(person.Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject


    def printNameSubject(self):
        """ Print full name and subject
        """
        print(str(self.firstname) + ' ' + str(self.lastname) + ', ' + str(self.subject))
        return None
