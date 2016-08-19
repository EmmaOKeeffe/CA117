class Employee(object):
    def __init__(self, name, emnum):
        self.name = name
        self.emnum = emnum

    def wages(self):
        return 0

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "Number: {}".format(self.emnum) + "\n" + "Wages: {:.2f}".format(self.wages())

class Manager(Employee):
    
    def __init__(self, name, emnum, salary):
        super().__init__(name, emnum)
        self.salary = salary 
   
    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    
    def __init__(self, name, emnum, hrrate, hours):
        super().__init__(name, emnum)
        self.hrrate = hrrate
        self.hours = hours

    def wages(self):
        return self.hrrate * self.hours

def main():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()
