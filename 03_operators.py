a, b = 7, 3
print("a + b =", a + b, ", a - b =", a - b, ", a * b =", a * b, ",a / b =", a / b)
print("a // b =",a // b, a % b, a ** b)
print(a == b, a != b, a > b, a >= b, a < b, a <= b)

t, f = True, False
print(t and f, t or f,"not t:", not t)

a += 5
print(a)

lst = [1, 2, 3]
print(2 in lst, 5 not in lst)
x = lst
y = lst[:]
print(x is lst, y is lst, x == y)

if (n := len(lst)) > 2:
    print("Độ dài =", n)
