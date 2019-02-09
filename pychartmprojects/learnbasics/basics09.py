# Class and Object

class classPerson(object):
    # PRIVATE is defined by DOUBLE UNDERSCORE
    name = ''
    email = ''
    __job = ''
    __salary = ''

    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Only parameterized constructor is allowed
    # Non-parameterized constructor is useless with parameterized constructor
    # Non-parameterized constructor is valueless without parameterized constructor

    def set_job(self, job):
        self.__job = job

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_job(self):
        return self.__job

    def get_salary(self):
        return self.__salary

    def toString(self):
        return '{} can be contacted at {}'.format(self.name, self.email)


# Inheritance
# To inherit we just need to put the class which we want to inherit in argument of our current class
class classCustomer(classPerson):
    __balance = None

    def __init__(self, name, email, balance):
        super().__init__(name, email)
        # You don't need to do it as below in python 3
        # super(classCustomer, self).__init__(name, email)
        # __name = name
        # __email = email
        self.__balance = balance

        def set_balance(self, balance):
            self.__balance = balance

        def get_balance(self):
            return self.__balance

    def toString(self):
        return '{} has a balance of {} BDT and can be contacted at {}'.format(self.name, self.__balance, self.email)
        # You can only access the
        # public attributes of super/parent class
        # from the sub/child class


# values must be given if there is a parameterized constructor
customer1: classCustomer = classCustomer('Rafi', 'rafi@gmail.com', 20000)
person1: classPerson = classPerson('Mahir', 'mahir@gmail.com')

person1.set_job('Programmer')
person1.set_salary(76000)
name = person1.get_name()
email = person1.get_email()
job = person1.get_job()
salary = person1.get_salary()

customer2 = classCustomer('Jebin', 'JB@gmail.com', 9000)
customer2.set_job('Automation Engineer')
customer2.set_salary(83000)
name = customer2.get_name()
email = customer2.get_email()
job = customer2.get_job()
salary = customer2.get_salary()

print()
print('-' * 20)

print(customer1.toString())
print('Name: ' + name + '\nEmail: ' + email)
print('Job: ' + job + '\nSalary:', salary, 'BDT')
print(person1.toString())
print('Name: ' + name + '\nEmail: ' + email)
print('Job: ' + job + '\nSalary:', salary, 'BDT')
print(customer2.toString())

print('-' * 20)
