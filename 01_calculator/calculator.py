class calculator:
    def add(self, nums):
        """add as many numbers in the list"""
        if not nums:
            return 0
        
        final = 0
        for i in nums:
            final += i

        return final
        # return sum(nums)


    def subtract(self, nums):
        """subtract as many numbers in the list"""
        if not nums:
            return 0
        
        final = nums[0]
        for i in nums[1:]:
            final -= i

        return final


    def multiply(self, nums):
        """multiply as many numbers in the list"""
        if not nums:
            return 0
        
        final = 1
        for i in nums:
            final *= i

        return final


    def divide(self, nums):
        """divide as many numbers in the list"""
        if not nums:
            return 0
        
        final = nums[0]
        for i in nums[1:]:
            if i == 0:
                print("Error, can't divide by zero") 
                return None
            final /= i

        return final



def getNumsAndOperation():
    """parse the input to get the operation and the numbers from the input"""
    raw_input = input("Enter the operation and then the numbers with a space (add 5 6 7): ").strip()
    if not raw_input:
        return None, []

    split = raw_input.split()
    operation = split[0].lower()

    numbers = []
    for i in split[1:]:
        try:
            numbers.append(float(i))
        except:
            print("Skipping invalid number")

    return operation, numbers



def main():
    calc = calculator()

    while True:
        op, nums = getNumsAndOperation()

        if op in ["exit", "quit", "q"]:
            print("calculator closed")
            return None

        if not nums:
            print("Please add in valid numbers")

        if op == "add":
            result = calc.add(nums)
        elif op == "subtract":
            result = calc.subtract(nums)
        elif op == "multiply":
            result = calc.multiply(nums)
        elif op == "divide":
            result = calc.divide(nums)
        else:
            print("Unknown op. Please use add, subtract, multiply, divide")

        if result is not None:
            print(result)


if __name__ == "__main__":
    main()