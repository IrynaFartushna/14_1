class GroupLimitExceededError(Exception):
    """Виключення для ситуації, коли у групі більше 10 студентів."""
    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)

# Класс Human
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.record_book == other.record_book)
        return False

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10  # Ограничение на количество студентов в группе

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitExceededError()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)
        else:
            print(f"Student with last name {last_name} not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 18, 'Sveta', 'Jovs', 'AN143')
st4 = Student('Female', 20, 'Luiza', 'Tantova', 'AN146')
st5 = Student('Male', 40, 'Uriy', 'Starovskiy', 'AN144')
st6 = Student('Female', 65, 'Iryna', 'Kyseleva', 'AN147')
st7 = Student('Male', 37, 'Evgeniy', 'Egupov', 'AN145')
st8 = Student('Female', 23, 'Oleksandr', 'Hlushko', 'AN148')
st9 = Student('Male', 19, 'Inna', 'Honcharova', 'AN146')
st10 = Student('Female', 21, 'Lydmila', 'Tkach', 'AN149')
st11 = Student('Male', 39, 'Ihor', 'Seriy', 'AN150')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

print(gr)

try:
    for i in range(11):
        st = Student('Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN1{i}')
        try:
            gr.add_student(st)
        except GroupLimitExceededError as e:
            print(e)
            break
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Group after attempting to add 11 students:")
print(gr)
