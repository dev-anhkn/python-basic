# services/pet_manager.py
class PetManager:
    def __init__(self):
        self.__pets = []  # Thuộc tính private

    def add_pet(self, pet):
        self.__pets.append(pet)

    def show_all(self):
        print("🐾 Danh sách thú cưng:")
        for pet in self.__pets:
            print(f"- {pet.name} (energy: {pet.get_energy()})")

    def make_all_speak(self):
        print("\n🔊 Các bé đang phát biểu:")
        for pet in self.__pets:
            pet.speak()

    def get_total_energy(self):
        return sum(pet.get_energy() for pet in self.__pets)
