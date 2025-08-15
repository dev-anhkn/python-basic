# Biến & Kiểu dữ liệu cơ bản

an_int = 42
a_float = 3.14
a_bool = True
a_str = "Xin chào"

a_list = [1, 2, 3]  # list (mutable)
a_tuple = (1, 2, 3)  # tuple (immutable)
a_dict = {"name": "Hien", "age": 33}
a_set = {1, 2, 2, 3}  # -> {1,2,3}
a_none = None

print("type: ", type(a_float))  # <class 'float'>
print("type: ", type(a_bool))  # <class 'bool'>
print("type: ", type(an_int))  # <class 'int'>
print(int(3.9), float(2), str(123))

x, y, z = (10, 20, 30)  # tuple unpacking (hay còn gọi là multiple assignment – gán nhiều biến cùng lúc).
print("x=", x, "y=", y, "z=", z)

from typing import List, Dict, Optional

numbers: List[int] = [1, 2, 3]
profile: Dict[str, int | str] = {"name": "Lan", "age": 25}
maybe_id: Optional[int] = None

print("numbers: ", numbers)
print("profile: ", profile)
print("maybe_id: ", maybe_id)