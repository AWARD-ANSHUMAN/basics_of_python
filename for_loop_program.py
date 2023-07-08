# finding sum of all even integers between 1 to 1000
total=0
for number in range(1, 201):
    if number % 2 == 0:
        total = total+number
print(f"Sum of all even integers is {total} ")
