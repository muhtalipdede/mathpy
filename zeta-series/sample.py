def zeta(s, limit=1000):
    """
    Zeta serisini hesaplayan fonksiyon
    s: zeta serisinin parametresi
    limit: serinin toplamı için hesaplanacak terim sayısı
    """
    result = 0.0
    for n in range(1, limit+1):
        result += 1.0 / pow(n, s)
    return result

result = zeta(2, 10000)
print(result)
