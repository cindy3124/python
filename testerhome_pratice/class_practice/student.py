from person import Person


class Student(Person):

    # 子类初始化方法要对父类方法进行初始化
    def __init__(self, name):
        Person.__init__(self, name)

    def set_grade(self, grade):
        self.grade = grade
        return self.grade


if __name__ == '__main__':
    toni_instance = Student('toni')
    print(toni_instance.get_name())
    print(toni_instance.set_grade('一年级'))
