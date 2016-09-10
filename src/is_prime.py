def is_prime(x):
    n = 2
    if x <= 1:
        return False
    else:
        while n > 1 and n < x:
            if x % n == 0:
                return False
            n +=1
        else:
            return True