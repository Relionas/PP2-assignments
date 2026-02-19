class Class:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Class("Tobias", 15)
print(p1.name)
print(p1.age)



class Class:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
p1 = Class("Tobias", 15)
p2 = Class("Emily")
print(p1.name, p1.age)
print(p2.name, p2.age)



class Class:
    def __init__(self, country = "Kazakhstan", city = "Almaty"):
        self.country = country
        self.city = city
p1 = Class("France","Paris")
p2 = Class()
print(p1.country, p1.city)
print(p2.country, p2.city)



class Class:
    def __init__(self, country, city, street, favourite_music):
        self.country = country
        self.city = city
        self.street = street
        self.favourite_music = favourite_music
p1 = Class("Kazakhstan","Almaty","Buqar-Jyrau","Flashing lights")
print(p1.country, p1.city, p1.street, p1.favourite_music)




