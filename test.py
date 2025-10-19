
## python interview question find the factorical of given number

number  = int(input("Enter your number = "))
factorial = 1
if number == 0:
    print("factorial of 0 is 1")
    exit()
elif number ==1:
    print("factorial of 1 is 1")
    exit()
else:
    for i in range(1,number+1): 
     factorial = factorial * i

print(f"factorial of {number} is {factorial}")
