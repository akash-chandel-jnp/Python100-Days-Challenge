num = 8 / 5
print(num)

print(
    round(num, 2)
)  # still the answer will be 1.6 not 1.60 as 8/5 is actually 1.6... so what we need to print ans as 1.60 is not rounding but formatting

new_num = "{:.2f}".format(round(num, 2))  # new number is -->  1.60
print(new_num)
