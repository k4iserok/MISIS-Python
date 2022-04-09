class Student:
    def __init__(self, name='Ivan', groupNumber='10A', age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def setNameAge(self, new_name=None, new_age=None):
        self.name = new_name
        self.age = new_age
        return 'Имя и возраст изменены'

    def setGroupNumber(self, new_groupNumber):
        self.groupNumber = new_groupNumber
        return 'Номер группы изменен'

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber


st_1 = Student()
print('1: ', st_1.name, st_1.age, st_1.groupNumber,'\n')

st_2 = Student('Ruslan', '11A', 18)
print('2: ', st_2.getName(), st_2.getAge(), st_2.getGroupNumber(), '\n')

st_3 = Student(age=15,groupNumber='7B', name='Vasiliy')
print('3: ', st_3.getName(), st_3.getAge(), st_3.getGroupNumber(), '\n')

st_4 = Student(groupNumber='7A', age=15)
print(st_4.setGroupNumber(new_groupNumber='8A'))
print('4: ', st_4.getName(), st_4.getAge(), st_4.getGroupNumber(), '\n')

st_5 = Student('Kirya', '5B', 13,)
print(st_5.name,st_5.age,st_5.groupNumber)
print(f'{st_5.setNameAge("Kirill", 14)}\n{st_5.setGroupNumber("6A")}')
print('5: ', st_5.getName(), st_5.getAge(), st_5.getGroupNumber(), '\n')
