#total of two value and avg
class Operation:
    def __init__(self,num1,num2):
        # Read two numbers from the user
        self.num1 = num1
        self.num2 = num2
        print("Operation read completed")

    def write(self):
        # Display the entered numbers
        print("First number:", self.num1)
        print("Second number:", self.num2)
        print("Operation write completed")

    def calc(self):
        # Perform addition
        total = self.num1 + self.num2
        avg=total/2
        print("Total:", total)
        print("Average:", avg)

num1=int(input("Enter the number: "))
num2=int(input("enter the number: "))

# Create an object of the class
obj= Operation(num1,num2)

# Call the method
obj.write()
obj.calc()

