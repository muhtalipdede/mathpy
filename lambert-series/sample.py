import math

def lambert_series(x, n):
    if x <= 0:
        raise ValueError("Lambert serisi için x değeri 0'dan büyük olmalıdır.")
    
    total = 0.0
    for i in range(1, n+1):
        term = ((-1)**(i-1) * i**(i-2) * x**i) / math.factorial(i)
        if math.isnan(term) or math.isinf(term):
            break
        total += term
        
    return total

# Örnek kullanım
x = 1.5
n = 20
result = lambert_series(x, n)
print(f"Lambert serisinin toplamı: {result}")
