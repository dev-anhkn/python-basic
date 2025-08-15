# models/dog.py
from models.pet import Pet

class Dog(Pet):  # Kế thừa Pet
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Ghi đè (Overriding) → Polymorphism
        print(f"{self.name} the {self.breed} says: Woof!")
        self._reduce_energy(10)  # Gọi hành vi được đóng gói từ lớp cha
