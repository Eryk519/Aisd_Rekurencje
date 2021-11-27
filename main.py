def prime(n: int) -> bool:
    if n < 1:
        return bool(False)
    if n == 2:
        return bool(True)
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return bool(False)
            else:
                return bool(True)
print(prime(33))
