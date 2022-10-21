class Animal:
    def __init__(self, name, age, type, location, diet):
        self.age = age,
        self.name = name,
        self.type = type,
        self.location = location
        self.diet = diet
    
    def __str__(self):
        return f"{self.age} + {self.name}  {self.type} + {self.location} + {self.diet} "

animal1 = Animal(31, "Jonas", "mamal", "Denmark", "Carinovire")
animal2 = Animal(33, "Yonas", "mamal", "England", "Vegan")
print(animal2)


print(getattr(animal1, 'type'))
print(animal1.type)


chosen_attr = "diet"
print(getattr(animal1, chosen_attr))

# hasattr - checks if this object contains this attribute (returns True or False)
print(hasattr(animal2, 'location')) # Used to check if an attribute is there for avoiding exceptions 

# setattr - Takes in object, attribute name and value and sets it. 
# Set an attribute that it doesn't already have
print(setattr(animal2, 'location', 'Denmark')) # returns None, because setattr doesn't return anything
print(hasattr(animal2, 'location'))

# delattr - Takes in object, attribute name and removes this attribute (not just value)
print(f"Location is: {animal1.diet}")
delattr(animal1, 'location')
print(animal1.location)
