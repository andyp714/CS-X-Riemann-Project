import numpy as np
import matplotlib.pyplot as plt
from polynomialClass import Polynomial



def main():
    coefficientArray = list(map(float, input("Enter Coefficients each seperated by a space. First number is the x^0th coefficient and so on. > ").split()))
    polynomialObject = Polynomial(coefficientArray)
    polynomialObject.printPolynomial()
    startInterval = int(input("Enter Start Interval > "))
    endInterval = int(input("Enter End Interval > "))
    sliceAmount = int(input("Enter how many subdivisions > "))
    print("Right Riemann Sum:", polynomialObject.rightRiemannSum(startInterval,endInterval,sliceAmount))
    print("Left Riemann Sum:",polynomialObject.leftRiemannSum(startInterval,endInterval,sliceAmount))
    print("Midpoint Riemann Sum:",polynomialObject.midRiemannSum(startInterval,endInterval,sliceAmount))
    print("Trapezoidal Riemann Sum:",polynomialObject.trapRiemannSum(startInterval,endInterval,sliceAmount))

        
    


if __name__ == "__main__":
    main()