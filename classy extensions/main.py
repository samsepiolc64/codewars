class Animal:
    def speak(self):
        return f"{self.name} {self.voice}."

class Cat(Animal):
    def __init__(self, name):
        self.voice = "meows"
        self.name = name

cat = Cat('Lamp')
print(cat.speak())