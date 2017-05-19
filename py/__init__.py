

class FizzBuzz:
    def __init__(self): self

    def getNumbers(self, inputRange=None):
        if inputRange is None: inputRange = range(1,16,1)
        outputNumbers = []
        for i in inputRange:
            outputNumbers.insert(i,self.processNumber(i))
        return outputNumbers

    def __processNumber(self, num):
        # if(num%5==0 and num%3==0): return "FizzBuzz"
        if(num%15==0): return "FizzBuzz"
        elif(num%5==0): return "Buzz"
        elif(num%3==0): return "Fizz"
        else: return num



























    def processNumberRecursion(self, inputRange, outputNumbers=[]):
        if not inputRange :
            return outputNumbers
        elif(inputRange[0]%15==0):
            outputNumbers.append("FizzBuzz")
            return self.processNumberRecursion(inputRange[1:],outputNumbers)
        elif(inputRange[0]%5==0):
            outputNumbers.append("Buzz")
            return self.processNumberRecursion(inputRange[1:],outputNumbers)
        elif(inputRange[0]%3==0):
            outputNumbers.append("Fizz")
            return self.processNumberRecursion(inputRange[1:],outputNumbers)
        else:
            outputNumbers.append(inputRange[0])
            return self.processNumberRecursion(inputRange[1:],outputNumbers)

x = FizzBuzz()
print x.processNumberRecursion([3,6,9])