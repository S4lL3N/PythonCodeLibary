class Car:
    
    #constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #methods
    def drive(self):
        print("The car is driving")

    def stop(self):
        print("The car is stopped")

    #toString Method
    def __str__(self):
        output = "Make: " + self.make
        output += " Model: " + self.model
        output += " Year: " + str(self.year)
        output += " Color: " + self.color
        return output
