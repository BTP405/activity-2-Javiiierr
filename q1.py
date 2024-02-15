def isPrime(n):
    """
    Functionality: Determines whether or not a number is prime
    
    Input Argument: n(int) - input number
    Returns: A boolean determining if a number is prime
    """

    # check all numbers until half of n
    for i in range(2, n//2+1):
        # if any factor is found return False
        if (n%i) == 0:
            return False
    # if no factor is found return True
    return True
    
def getPrimeNumbers(n):
    """
    Functionality: Uses helper function isPrime and comprehension to return a list containing all prime numbers between 2 and n
    
    Input Arguments: n(int) - input number
    Returns: Returns said list
    """

    # comprehension to create list based on number primeness
    return [num for num in range(2, n) if isPrime(num)]

print(getPrimeNumbers(300))