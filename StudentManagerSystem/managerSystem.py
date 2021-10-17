from student import Student


class StudentManager(object):
    """管理系统对象，保存学生对象"""

    def __init__(self):
        self.student_list = []

    # 功能入库函数
    def run(self):
        # 封装管理系统的功能
        # 1、家在学生信息
        while True:
            # 2、显示功能菜单
            self.show_menu()
            # 3、获取用户输入的功能编号
            menu_num = int(input('输入功能编号：'))
            # 4、根据功能编号执行相应方法
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_all()
            elif menu_num == 6:
                self.show_all()
            elif menu_num == 7:
                print("系统退出")
                break

    # 二系统功能函数
    # 显示系统功能菜单
    @staticmethod
    def show_menu():
        print(f'请选择系统功能：\n1:添加学员\n2:删除学员\n3:修改学员信息\n4:查询学员信息\n5:显示所有学员\n6:保存学员信息\n7:退出系统')

    # 学员信息的增删改查、保存、加载信息
    def add_student(self):
        # print("添加学员")
        name = input("请输出学生姓名：")
        gender = input("请输入学生性别：")
        tel = input("请输入手机号：")
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(f"添加学生{student}")

    def del_student(self):
        name = input("请输入待删除学生姓名：")
        student = self.find_student_by_name(name)
        if student is not None:
            check = input(f"确定删除学员{name}？Y:确定,N:再考虑一下")
            if check == 'Y':
                print(f'已删除{self.student_list.pop(student)}')


def modify_student(self):
    print("修改学员信息")


def search_student(self):
    print("查询学员信息")


def show_all(self):
    # 显示所有学员
    print("显示所有学员")


def save_student(self):
    print("保存学员信息")


def find_student_by_name(self, name):
    for i in self.student_list:
        if i.name == name:
            return i
    else:
        print("查无此人")
