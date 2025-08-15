
nums = [1, 2, 3]
nums.append(4)
nums.extend([5, 6])
nums.insert(1, 0)
print(nums)

squares = [x*x for x in nums if x % 2 == 0]
print("Bình phương số chẵn:", squares)

t = (1, "a")

a, b = {1,2,3}, {3,4}
print(a | b, a & b, a - b, a ^ b)
