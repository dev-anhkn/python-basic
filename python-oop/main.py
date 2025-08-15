# main.py
from models.dog import Dog
from models.cat import Cat
from service.pet_manager import PetManager

def main():
    manager = PetManager()

    dog1 = Dog("Sữa", "Pomeranian")
    cat1 = Cat("Miu")

    manager.add_pet(dog1)
    manager.add_pet(cat1)

    manager.show_all()
    manager.make_all_speak()

    print("\n📊 Năng lượng tổng:", manager.get_total_energy())

if __name__ == "__main__":
    main()
