class Idol:
    def __init__(self, name, age, appearance):
        self.name = name
        self.age = age
        self.__appearance = appearance

    def get_appearance(self):
        return self.__appearance
    def set_appearance(self, appearance):
        self.__appearance = appearance


class KhaBanh(Idol):

    def __init__(self, name, age, appearance, location):
        super().__init__(name, age, appearance)
        self.location = location

    def livestream(self):
        pass  # Chưa viết nội dung livestream

    def signature_q(self):
        print("Ao that day")


class TienBip(Idol):
    def livestream(self):
        pass  # Chưa viết nội dung livestream

    def signature(self):
        print("Con cai nit")


kb = TienBip("TienBip", 100, 100)
kb.livestream()
kb.signature()
print(kb.name)

kb = KhaBanh("KhaBanh", 100, 100, "trong tu")
kb.livestream()
kb.signature_q()
print(kb.name)
print(kb.location)
