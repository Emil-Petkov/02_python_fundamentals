class Person:
    def __init__(self, first_name, last_name, age, town='Sofia'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.town = town

    def say_hello(self, greeting):
        return f'{greeting}, {self.first_name} {self.last_name} from {self.town}.'

    def birthday(self):
        self.age += 1
        return f'Happy birthday, {self.first_name}! You are now {self.age} years old.'

    def move(self, new_town):
        old_town = self.town
        self.town = new_town
        return f'{self.first_name} has moved from {old_town} to {self.town}.'

# Създаване на обект от класа Person
p = Person('Emil', 'Petkov', 32, 'Varna')

# Извикване на метода say_hello
print(p.say_hello('Hello'))

# Извикване на метода birthday
print(p.birthday())

# Извикване на метода move
print(p.move('Plovdiv'))

# Отново извикване на метода say_hello за да видим новите данни
print(p.say_hello('Hi'))
