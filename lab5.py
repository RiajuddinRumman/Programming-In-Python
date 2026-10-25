try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")