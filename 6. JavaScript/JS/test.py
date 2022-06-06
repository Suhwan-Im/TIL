# Python으로 JS 따라하기

# def add(num1, num2):
#     return num1 + num2

# def mul(num1, num2):
#     return num1 * num2

calculator = {
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y
    }

print(calculator['add'](1, 2))  # 3
print(calculator['mul'](3, 4))  # 12