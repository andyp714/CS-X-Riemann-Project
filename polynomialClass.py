import numpy as np
import matplotlib.pyplot as plt


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
        if self.coefficientValues[0] != 0:
            polynomialString = 'f(x) = ' + str(self.coefficientValues[0])
            firstDigit = False

        else:
            polynomialString = 'f(x) = '
            firstDigit = True
        for index, coefficient in enumerate(self.coefficientValues[1:]):
            if coefficient != 0:
                if index == 0:
                    tempString = str(abs(coefficient)) + 'x'
                else:
                    tempString = str(abs(coefficient)) + 'x^' + str(index+1)
                if coefficient > 0:
                    if firstDigit:
                        polynomialString = polynomialString + tempString
                        firstDigit = False
                    else:
                        polynomialString = polynomialString + ' + ' + tempString
                else:
                    polynomialString = polynomialString + ' - ' + tempString
        print(polynomialString)

    def rightRiemannSum(self, startPoint, endPoint, sliceAmount):
        sliceValue = (endPoint - startPoint)/sliceAmount
        totalSum = 0
        for i in range(sliceAmount):
            totalSum += sliceValue * self.findValue(startPoint + sliceValue * (i+1))
        return totalSum
    
    def leftRiemannSum(self, startPoint, endPoint, sliceAmount):
        sliceValue = (endPoint - startPoint)/sliceAmount
        totalSum = 0
        for i in range(sliceAmount):
            totalSum += sliceValue * self.findValue(startPoint + sliceValue * (i))
        return totalSum
    
    def midRiemannSum(self, startPoint, endPoint, sliceAmount):
        sliceValue = (endPoint - startPoint)/sliceAmount
        totalSum = 0
        for i in range(sliceAmount):
            totalSum += sliceValue * self.findValue(startPoint + sliceValue * (i+0.5))
        return totalSum
    
    def trapRiemannSum(self, startPoint, endPoint, sliceAmount):
        sliceValue = (endPoint - startPoint)/sliceAmount
        totalSum = 0
        for i in range(sliceAmount):
            totalSum += sliceValue * (self.findValue(startPoint + sliceValue * (i+1)) + self.findValue(startPoint + sliceValue * (i)))/2
        return totalSum