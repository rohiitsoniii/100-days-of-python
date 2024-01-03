def prime(number):
    is_prime=True
    for i in range(2,number-1):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("number is prime")
    else:
        print("number is not a prime")


number=int(input("enter a number: "))
prime(number)