
s = "Python cơ bản"
print(s.lower(), s.upper(), s.title())
print(s[0:6], s[-4:])

name, score = "Minh", 9.4567
print(f"{name} đạt {score:.2f} điểm")

parts = ["xin", "chào", "bạn"]
print(" ".join(parts))
print("  hello  ".strip())
print("a,b,c".split(","))

b = "Tiếng Việt".encode("utf-8")
print(b, b.decode("utf-8"))

import re
text = "Email: user@example.com"
text_ = "Email: user@a.x"
m = re.search(r"[\w.-]+@[\w.-]+", text)
m_ = re.search(r"[\w.-]+@[\w.-]+", text_)
print("Tìm email:", m.group(0) if m else None)
print("Tìm email:", m_.group(0) if m_ else None)
