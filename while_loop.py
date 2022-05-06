number = 4
while number >= 1:
    if number != 3:
        print(number)
    number -= 1
print("Loop is executed!")

# another example
number2 = 10
while number2 > 1:
    if number2 == 9:
        number2 -= 1
        # when you want to skip current iteration and proceed to next iteration without executing the next statements
        continue
    if number2 == 3:
        # break halts the loop execution on that particular condition. in this case it stops the while loop
        break
    print(number2)
    number2 -= 1
