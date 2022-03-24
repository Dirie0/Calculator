class Calculator:

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def add(self):
        return self.number_1 + self.number_2
    
    def subtract(self):
        return self.number_1 - self.number_2

    def multiply(self):
        return self.number_1 * self.number_2

    def divide(self):
        return self.number_1 / self.number_2
    
    def decision_making(self, decision):
        if decision == "+":
            return self.add()
        if decision == "-":
            return self.subtract()
        if decision == "*":
            return self.multiply()
        if decision == "/":
            return self.divide()


while True:
    user_input = input("Please type in your calculation, eg number_1 + number_2: ")
    user_input = user_input.strip().split(" ")
    # print(user_input)

    user_number_1 = int(user_input[0])
    user_number_2 = int(user_input[2])
    user_decision = user_input[1]
    # print(user_number_1,user_number_2,user_decision)

    calc = Calculator(user_number_1, user_number_2)
    result = calc.decision_making(user_decision)
    print(result)

    user_continuation = input ("Please type 'yes' to continue and anything else to exit: ")
    lower_casing_user_input = user_continuation.lower()
    if lower_casing_user_input == 'yes':
        continue
    else:
        break




    

    

