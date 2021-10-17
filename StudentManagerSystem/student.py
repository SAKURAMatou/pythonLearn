class Student(object):
    """学生对象，包含：姓名、性别、手机号"""

    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'姓名:{self.name},性别:{self.gender},手机号:{self.tel}'

# s = Student("Alice", "F", 18)
# print(s)
