
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("grade =", grade)

is_pass = "Đậu" if score >= 50 else "Rớt"
print(is_pass)

cmd = "start"
match cmd:
    case "start":
        print("Bắt đầu!")
    case "stop":
        print("Dừng lại!")
    case _:
        print("Không rõ lệnh")
