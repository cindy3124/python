# coding:utf-8

# 作业：2、设计一个作业1中服务器的子类，实现一个新的方法：
#         根据 cpu个数、内存大小、磁盘空间大小，计算出服务器当前价格
#         在子类里面实现一个服务价格的函数。
#         计算公式为: CPU个数* 1527.679+内存大小G* 100.21+磁盘空间大小G * 50.789 。
#         返回数据类型为浮点型。保留小 数点后2位。 并实例化此方法，打印出价格。 Round实现小数点后2位

from server import Server


class ServerPrice(Server):

    def __init__(self, cpu_num, mem_size, disk_size, system):
        Server.__init__(self, cpu_num, mem_size, disk_size, system)

    def cpu_price(self):
        return int(self.cpu_num) * 1527.679

    def mem_price(self):
        return int(self.mem_size) * 100.21

    def disk_price(self):
        return int(self.disk_size) * 50.789

    def total_price(self):
        return round(self.cpu_price()+self.mem_price()+self.disk_price(), 2)


if __name__ == '__main__':
    my_server = ServerPrice('8', '40', '150', 'Linux')
    print(my_server.total_price())
