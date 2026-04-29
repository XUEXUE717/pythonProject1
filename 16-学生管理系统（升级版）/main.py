import os


class Student:
    """学生实体类"""

    def __init__(self, student_id, name, age, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"学号: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 成绩: {self.score}"


class StudentManager:
    """学生管理类：负责业务逻辑与文件操作"""

    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()  # 初始化时加载数据

    def load_from_file(self):
        """从文件加载学生数据（读取操作 + 异常处理）"""
        if not os.path.exists(self.filename):
            print("未找到本地数据文件，将创建新文件。")
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    # 假设文件存储格式为：学号,姓名,年龄,成绩
                    parts = line.split(',')
                    student_id, name, age, score = parts, parts, int(parts), float(parts)
                    self.students.append(Student(student_id, name, age, score))
            print("数据加载成功！")
        except Exception as e:
            print(f"读取文件时发生异常: {e}")

    def save_to_file(self):
        """将学生数据保存到文件（写入操作 + 异常处理）"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for stu in self.students:
                    f.write(f"{stu.student_id},{stu.name},{stu.age},{stu.score}\n")
            print("数据已成功保存到文件！")
        except Exception as e:
            print(f"保存文件时发生异常: {e}")

    def add_student(self):
        """添加学生（输入异常处理）"""
        try:
            student_id = input("请输入学号: ").strip()
            # 检查学号是否已存在
            if any(s.student_id == student_id for s in self.students):
                print("该学号已存在！")
                return

            name = input("请输入姓名: ").strip()
            age = int(input("请输入年龄: "))
            score = float(input("请输入成绩: "))

            self.students.append(Student(student_id, name, age, score))
            print("添加成功！")
        except ValueError:
            print("输入错误：年龄和成绩必须是数字！")

    def delete_student(self):
        """删除学生"""
        student_id = input("请输入要删除的学号: ").strip()
        for stu in self.students:
            if stu.student_id == student_id:
                self.students.remove(stu)
                print("删除成功！")
                return
        print("未找到该学号的学生。")

    def modify_student(self):
        """修改学生信息"""
        student_id = input("请输入要修改的学号: ").strip()
        for stu in self.students:
            if stu.student_id == student_id:
                try:
                    print(f"当前信息: {stu}")
                    stu.name = input("请输入新姓名: ").strip()
                    stu.age = int(input("请输入新年龄: "))
                    stu.score = float(input("请输入新成绩: "))
                    print("修改成功！")
                except ValueError:
                    print("输入错误：年龄和成绩必须是数字！")
                return
        print("未找到该学号的学生。")

    def query_student(self):
        """查询学生"""
        student_id = input("请输入要查询的学号: ").strip()
        for stu in self.students:
            if stu.student_id == student_id:
                print(f"查询结果 -> {stu}")
                return
        print("未找到该学号的学生。")

    def show_all(self):
        """显示所有学生"""
        if not self.students:
            print("当前没有学生数据。")
            return
        print("\n--- 所有学生列表 ---")
        for stu in self.students:
            print(stu)
        print("------------------")


def main():
    manager = StudentManager()

    while True:
        print("\n=== 学生管理系统 ===")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生")
        print("4. 查询学生")
        print("5. 显示所有学生")
        print("6. 保存并退出")

        choice = input("请输入选项 (1-6): ").strip()

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.delete_student()
        elif choice == '3':
            manager.modify_student()
        elif choice == '4':
            manager.query_student()
        elif choice == '5':
            manager.show_all()
        elif choice == '6':
            manager.save_to_file()
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请重新输入。")


if __name__ == "__main__":
    main()