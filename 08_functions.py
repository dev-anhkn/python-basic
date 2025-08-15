
def greet(name: str, times: int = 1) -> str:
    """Trả về chuỗi chào lặp lại `times` lần."""
    return ("Xin chào " + name + "! ") * times

print(greet("Hà", 2))

def add_all(*args: int) -> int:
    total = 0
    for v in args:
        total += v
    return total

def show_profile(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

print(add_all(1,2,3,4))
show_profile(name="Hien", age=33)

numbers = [5, 2, 9, 1]
print(sorted(numbers, key=lambda x: -x))
