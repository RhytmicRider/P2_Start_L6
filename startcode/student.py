class Student:

    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def stel_voor(self):
        print(f"mijn naam is {self.naam} en ik ben {self.leeftijd} jaar oud.")


Student1 = Student("Floor Mat","18")
Student2 = Student("Ron De Bril","17")

#Student1.stel_voor()
##Student2.stel_voor()