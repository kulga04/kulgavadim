class Cat:
    def __init__(self,name, color, age ):
       self.name = name
       self.color = color
       self.age = age
    def meow(self):
        print(self.name + ": meow!")
    def myr(self):
        print(f"{self.name}: myr!")
    def sleep(self):
        print(f"{self.name}: sleep!")
kit = Cat("vaska", "black", "2" )
print(kit.name)
print(kit.color)
print(kit.age, "years")
kit.meow()
kit.myr()
kit.sleep()