

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printFullName(self):
        '''Return full name of person
        '''
        print(str(self.firstname) + ' ' + str(self. lastname))
        return None

