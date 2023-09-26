"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Please only input Positive Numbers Only.")

    list = [2]
    
    numbers = number_of_primes*5
    
    for number in range(3, numbers):
        is_Prime = True 
        for i in range(2,(number//2)+1):
            if number % i == 0:
                is_Prime = False

        if is_Prime == True and len(list) < number_of_primes:
            list.append(number)



    return list
