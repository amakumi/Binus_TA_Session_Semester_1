
class Student:
    def __init__(self, name, listening, reading, essay):
        self.name = name
        self.listening = listening
        self.reading = reading
        self.essay = essay

    def calculate(self):
        grade = 0
        #calculation
        grade = self.listening + self.reading + 2 * self.essay
        return grade

    def status(self):
        temp = ""
        grade = self.listening + self.reading + 2 * self.essay
        if grade < 50:
            temp = "failed"
        elif grade >= 50:
            temp = "passed!"
        return temp

