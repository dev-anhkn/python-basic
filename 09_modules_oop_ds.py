
import math
print(math.sqrt(16))

class Person:
    species = "Homo sapiens"
    def __init__(self, name: str):
        self.name = name
    def say_hello(self):
        return f"Xin chào, tôi là {self.name}"

class Student(Person):
    def __init__(self, name: str, student_id: str):
        super().__init__(name)
        self.student_id = student_id

p = Person("Lan")
s = Student("Minh", "SV001")
print(p.say_hello(), "|", s.say_hello(), "|", s.student_id)

from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
print(Point(1,2))

from collections import deque, Counter, defaultdict, namedtuple
dq = deque([1,2,3]); dq.appendleft(0); dq.append(4); print(list(dq))
cnt = Counter("banana"); print(cnt)
dd = defaultdict(int); dd["a"] += 1; print(dd)
PointNT = namedtuple("PointNT", ["x","y"]); print(PointNT(3,4))
