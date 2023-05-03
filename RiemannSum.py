class Polynomial():
    def __init__(self, coefficientArray):
        self.coefficientValues = coefficientArray
        self.degree = len(coefficientArray) - 1

    def findValue(self,value):
        tempValue = 0
        for index, coefficient in enumerate(self.coefficientValues):
            tempValue += (value**index) * coefficient
        return(tempValue)


    def printPolynomial(self):
        polynomialString = 'f(x) = ' + str(self.coefficientValues[0])
        for index, coefficient in enumerate(self.coefficientValues[1:]):
            if coefficient != 0:
                tempString = str(coefficient) + 'x^' + str(index+1)
                polynomialString = polynomialString + ' + ' + tempString
        print(polynomialString)

    def rightRiemannSum(self, startPoint, endPoint, sliceAmount):
        sliceValue = (endPoint - startPoint)/sliceAmount
        totalSum = 0
        for i in range(sliceAmount):
            totalSum += sliceValue * self.findValue(startPoint + sliceValue * (i+1))
        return totalSum



def main():
    coefficientArray = list(map(int, input("Enter Coefficients each seperated by a space. First number is the x^0th coefficient and so on. > ").split()))
    polynomialObject = Polynomial(coefficientArray)
    polynomialObject.printPolynomial()
    print(polynomialObject.findValue(2))
    print(polynomialObject.rightRiemannSum(2,4,2))
    


if __name__ == "__main__":
    main()