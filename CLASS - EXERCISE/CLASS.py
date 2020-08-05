
class Students: #naming convention, class title capitalised
    def __init__(self): #call the constructor by def and initializing
        self.name = name
        self.gpa = gpa
        self.gender = gender
        self.age = age

    def view(self): #creates the interface!
        print("Name: ",self.name)
        print("GPA: ",self.gpa)
        print("Gender: ",self.gender)
        print("Age: ",self.age)

x = Students("Budi",3,"male","17") #way number 1
y = Students("John",3.5,"male","16")
x.view()
y.view()

arr = [] #creates an array
x.append(Students("Budi",3, "male","17"))
x.append(Students("John",3.5, "male","16"))
x.append(Students("Gal", 4, "female", "16"))
for e in arr: #prints each data one-by-one
    e.view()

#create using a dictionary
print("DICT:")

book = {}
book["Budi"] = ("Budi",3,"male","17")
book["John"] = ("John",3.5,"male","16")
book["Gal"] = ("Gal", 4, "female", "16")
for e in book: # in dictionaries, '.values' are needed
    e.view()
