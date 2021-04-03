# class 예제 
class Company:
    def __init__(self, name, location, salary, employee):
        self.name = name
        self.location = location
        self.salary = salary
        self.employee = 0

    def hire(self):
        self.salary += 1000
        self.employee += 500


