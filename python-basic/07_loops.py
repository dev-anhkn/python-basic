
fruits = ["apple", "banana", "cherry"]
for i, name in enumerate(fruits, start=1):
    print(i, name)

prices = [10, 20, 30]
for fruit, price in zip(fruits, prices):
    print(f"{fruit}: {price}")

n = 3
while n > 0:
    print("n =", n)
    n -= 1
else:
    print("Kết thúc while (không bị break)")

for x in range(5):
    if x == 2:
        continue
    if x == 4:
        break
    print("x =", x)
