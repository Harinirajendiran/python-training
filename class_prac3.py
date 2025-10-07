#mathematical square and cube term finder using class
class Operation:
    def read(self):
        # Read a number from the user
        #print("def func read the input")
        self.num =num

    def write(self):
        # Display the stored number
        #print("def func write the input")
        print("Operation num:", self.num)   

    def calc(self):
        # Perform some calculations
        square= self.num ** 2
        cube = self.num ** 3
        print("Square of number:", square)
        print("Cube of number:", cube)
        
num=int(input("enter the number"))

# Create an object of the class
obj = Operation()
# Call the methods
obj.read()
obj.write()
obj.calc()

        