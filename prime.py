import numpy as np

def is_prime(n: int) -> bool:
    for i in range(1, np.sqrt(n)+1):
        if n % i == 0:
            return False
        else:
            return True
