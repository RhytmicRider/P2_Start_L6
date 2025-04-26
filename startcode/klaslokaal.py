from student import Student

class Klaslokaal:

    def __int__(self):
        self.studenten = []

    def voeg_studenten_toe(self, student):
        self.studenten.append(student)

    def toon_studenten(self):
        for student in self.studenten:
            student.stel_voor()

student1 = Student("Lotte", 20)
student2 = Student("Jasper", 21)
student3 = Student("Emma", 20)
student4 = Student("Noah", 20)
student5 = Student("Sophie", 19)
student6 = Student("Liam", 20)
student7 = Student("Mila", 20)
student8 = Student("Lucas", 22)
student9 = Student("Zoe", 19)
student10 = Student("Finn", 20)
student11 = Student("Julia", 20)
student12 = Student("Daan", 20)
student13 = Student("Tess", 21)
student14 = Student("Sam", 20)
student15 = Student("Nina", 20)
student16 = Student("Max", 20)
student17 = Student("Eva", 20)
student18 = Student("Ravi", 21)
student19 = Student("Lara", 20)
student20 = Student("Yara", 20)



