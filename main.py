class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise  NotImplementedError("Subcalss must imp;ement abastract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит 'Гав'"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит 'Мяу'"
    
dog = Dog('Тузик')
cat = Cat('Мурзик')

print()