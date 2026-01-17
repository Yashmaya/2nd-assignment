import random as rnd
three_digit_code = ""
for _ in range(3):
    three_digit_code += str(rnd.randint(0,9))
four_digit_code =""
for _ in range(4):
    four_digit_code += str(rnd.randint(1,6))
print("three_digit_code:", three_digit_code)
print("four_digit_code:", four_digit_code)