import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from polynomialClass import Polynomial



def main():
    coefficientArray = list(map(float, input("Enter Coefficients each seperated by a space. First number is the x^0th coefficient and so on. > ").split()))
    polynomialObject = Polynomial(coefficientArray)
    polynomialObject.printPolynomial()
    startInterval = float(input("Enter Start Interval > "))
    endInterval = float(input("Enter End Interval > "))
    sliceAmount = int(input("Enter how many subdivisions > "))
    print("Right Riemann Sum:", polynomialObject.rightRiemannSum(startInterval,endInterval,sliceAmount))
    print("Left Riemann Sum:",polynomialObject.leftRiemannSum(startInterval,endInterval,sliceAmount))
    print("Midpoint Riemann Sum:",polynomialObject.midRiemannSum(startInterval,endInterval,sliceAmount))
    print("Trapezoidal Riemann Sum:",polynomialObject.trapRiemannSum(startInterval,endInterval,sliceAmount))
    polynomialObject.graphRiemann(startInterval, endInterval, sliceAmount)

    polynomialObject.animRiemann(startInterval, endInterval, 1, 100)

    

        
    


if __name__ == "__main__":
    main()