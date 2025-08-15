# models/pet.py
from abc import ABC, abstractmethod

class Pet(ABC):  # Trừu tượng
    def __init__(self, name: str):
        self.name = name            # Thuộc tính công khai
        self._energy = 100          # Thuộc tính protected
        self.__secret = "I love my owner"  # Thuộc tính private → dùng cho Encapsulation

    @abstractmethod
    def speak(self):  # Phương thức trừu tượng
        pass

    def get_energy(self):
        return self._energy

    def _reduce_energy(self, amount):  # đóng gói hành vi nội bộ
        self._energy = max(0, self._energy - amount)
