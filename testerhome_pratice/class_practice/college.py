from student import Student


class College(Student):

    def __init__(self, name):
        Student.__init__(self, name)

    def has_peer(self):
        return self.peer

    def set_peer(self, peer=None):
        if peer:
            self.peer = True
        else:
            self.peer = False

    def set_grade(self, grade):
        pass


if __name__ == '__main__':
    toni_instance = College('toni')
    print(toni_instance.get_name())
