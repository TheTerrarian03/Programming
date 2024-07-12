class Girl:

    gender = "female" # A Class variable is used/shared to all objects in a class

    def __init__(self, name):
        self.name = name # A unique variable, unique to each object.

r = Girl("Rachel")
s = Girl("Stanky")
print(r.gender, r.name)
print(s.gender, s.name)