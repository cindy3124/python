class Person():
    # 类变量，是全局变量，各实例间共享
    total_person = 0

    def __init__(self, name):
        # 初始化函数里面的变量，各实例间不共享，是互相隔离的
        self.name = name
        Person.total_person += 1

    # 实例方法
    def get_name(self):
        return self.name

    # 静态方法
    @staticmethod
    def set_sex(sex):
        return "sex is:"+sex

    # 类方法
    @classmethod
    def set_province(cls, province):
        return "province is:"+province

    # property方法
    @property
    def get_new_name(self):
        return "name is:"+self.name


if __name__ == '__main__':
    # 实例方法调用
    print(Person('toni').get_name())
    '''
    toni_instance = Person('toni')
    print(toni_instance.total_person)     # 结果：1
    stella_instance = Person('stella')
    print(stella_instance.total_person)   # 结果：2
    print(stella_instance.get_name())
    '''
    # 静态方法调用
    print(Person.set_sex('男'))
    print(Person('toni').set_sex('男'))
    # 类方法调用
    print(Person.set_province('广东'))
    print(Person('toni').set_province('广东'))
    # property方法调用
    print(Person('toni').get_new_name)
    # 访问私有变量
    print(Person('toni').name)
    print(Person('toni').get_name())
