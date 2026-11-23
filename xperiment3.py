number = int(input("Enter a positive number: "))

if number <= 0:
    print("Please enter a positive number")
else:
    i = 1
    while i <= 10:
        product = number * i
        print(f"{number} * {i} = {product}")
        i = i + 1