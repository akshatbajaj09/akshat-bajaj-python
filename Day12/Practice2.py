# Create a program with the following behavior:
# Story:
# You are designing a Student Record System.
# Instructions:
# Define a class for a student.
# Each student should store their name and grade when created.
# The school is the same for all students initially and is "DPS".
# It should be shared by all student objects.
# Add a way to change the school name for all students, say to "Kendriya Vidyalaya".
# Provide a method that allows a student to introduce themselves, printing:
# Hi, I'm <name> and I study in grade <grade> at <school>.
# Add a utility that can check if a grade is valid.
# Only grades 1 through 12 are considered valid.
# This check should not depend on any object.
# Finally, create:
# One student named Riya in grade 8
# One student named Raj in grade 13
# Let them introduce themselves
# Then, change the school to "Kendriya Vidyalaya"
# Let Riya introduce herself again
# Print whether Raj's grade is valid or not

class StudentRecord:
    school_name = 'DPS'
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade    
    @classmethod
    def new_school(cls, new_school_name):
        cls.school_name = new_school_name
    def introduce(self):
        print(f'Hi, I\'m {self.name} and I study in grade {self.grade} at {StudentRecord.school_name}.' )
    def grade_validity(self):
        if self.grade in range(1,13):
            print(f'{self.name}\'s grade is a valid grade.')
        else:
            print(f'{self.name}\'s grade is not a valid grade.')
Riya = StudentRecord('Riya', 8)
Raj = StudentRecord('Raj', 13)
Riya.introduce()
Raj.introduce()
StudentRecord.new_school('Kendriya Vidyalaya')
Riya.introduce()
Raj.grade_validity()