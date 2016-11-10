def is_prime(number):
    '''
    function to check for prime numbers
    '''
    if number < 2 and isinstance(number, str):
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    else:
        return True

def generate_prime_numbers(n):
    '''
    function to generate the list of prime 
    numbers based on the is_prime function
    '''
    if isinstance(n, int): #Ensure that one passes an integer
        prime_numbers = []
        for number in range(1,n):
            if is_prime(number):
                prime_numbers.append(number)
        return prime_numbers
    else:
        return "Please ensure that you pass an integer"

    

def main():
    print(generate_prime_numbers(2))
    
if __name__ == '__main__':
    main()