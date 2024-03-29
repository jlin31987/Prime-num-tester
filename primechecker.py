
def checkPrime(n):
    #checks if the number is equal to or less than 1
    if n <= 1:
        return False; #false because 0 and 1 are prime numbers, and returning false means NOT a prime number.
    else:
        #checks if the divisibility of the number from 2 up to the square root of the number
        for i in range(2, int(n**0.5) + 1 ):
            #if the number is divisible by i, then its not prime 
            if n % i == 0:
                return False
        #otherwise the number is true
        return True
            


n = int(input("Enter a number: "))

if checkPrime(n) == False:
    print("This number is not a prime number.")
else:
    print("This number is a prime number.")


