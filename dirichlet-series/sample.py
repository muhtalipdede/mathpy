import math

def dirichlet_series(x, a, b, n):
    if len(a) != len(b):
        raise ValueError("a ve b dizileri aynı uzunlukta olmalıdır.")
    
    total = 0.0
    for i in range(0, n):
        term = a[i] * math.cos((i+1) * x) + b[i] * math.sin((i+1) * x)
        total += term
        
    return (a[0]/2) + total

# Örnek kullanım
x = 0.5
a = [1, 2, 3, 4]
b = [1, 1, 1, 1]
n = 4
result = dirichlet_series(x, a, b, n)
print(f"Dirichlet serisinin toplamı: {result}")
