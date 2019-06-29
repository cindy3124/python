# coding:utf-8

# 作业：1、设计一个表示服务器的类。包含服务器的属性有:
#        CPU 个数、 内存大小、磁盘空间大小、操作系统类型(Linux, Windows)
#       其中操作系统类型设置为私有变量，外部不可以更改。
#       实现一个方法，输出服务器的属性内容为以下格式：8核CPU、40G内存、150G磁盘空间、Linux


class Server():

    def __init__(self, cpu_num, mem_size, disk_size, system):
        self.cpu_num = cpu_num
        self.mem_size = mem_size
        self.disk_size = disk_size
        self.__system = system

    def all_cpu_num(self):
        print('CPU为：', self.cpu_num, '核')
        return self.cpu_num

    def mem_info(self):
        print('内存大小为：', self.mem_size, 'G')
        return self.mem_size

    def disk_info(self):
        print('硬盘大小为：', self.disk_size, 'G')
        return self.disk_size

    def ope_system(self):
        if self.__system in ['Linux', 'Windows']:
            print('操作系统为：', self.__system)
            return self.__system
        else:
            print('操作系统填写错误，请重新检查。')


if __name__ == '__main__':
    my_server = Server('8', '40', '150', 'Linux')
    my_server.all_cpu_num()
    my_server.mem_info()
    my_server.disk_info()
    my_server.ope_system()

