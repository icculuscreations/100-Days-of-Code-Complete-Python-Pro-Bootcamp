class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # (Animal) is the class to inherit
    def __init__(self):
        super().__init__()  # this line inherits the attributes and methods from the Animal Class

    def breathe(self):
        super().breathe()  # takes the method "breathe" from Animal, runs it, and adds to it below
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)