# models/cat.py
from models.pet import Pet

class Cat(Pet):
    def __init__(self, name: str):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Meow!")
        self._reduce_energy(5)
