
# range function returns a list as output
#for loop then loops over this list
# formatted strings sytaxp:print(f")

count = 0
for x in range(1, 1001):
    if x % 2 == 0:
        count = count+1
print(f"there are total {count} even numbers between  1 to 1000")
