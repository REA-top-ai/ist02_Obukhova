#Задание
from abc import ABC, abstractmethod
class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class Employee(AbstractEmployee):
    def __init__(self, _name = None):
        super().__init__()
        self.__id = 0
        if isinstance(_name, str):
            self._name = _name
        self._name = None
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

    def say_id(self):
        print(f'My id is {self.id}')


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f'My username is {self.username} and I am an {self.role}')


class Admin(Employee, User):
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()


class Manager(Admin):
    def __init__(self):
        super().__init__()

    def say_id(self):
        super().say_id()

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, emp):
        self.attendees.append(emp)

    def __len__(self):
        for emp in self.attendees:
            emp.say_id()

        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
m1 = Meeting()

m1 + e1
m1 + e2
m1 + e3
print(len(m1))


# e1.say_id()
# e2.say_id()
# e3.say_id()
# e3.say_user_info()
# e4.say_id()

e = Employee()
print(dir(e))
