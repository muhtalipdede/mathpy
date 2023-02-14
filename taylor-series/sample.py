import math

def sin_taylor(x, n):
    """
    x: float - radyan cinsinden açı değeri
    n: int - Taylor serisinde hesaplanacak toplam terim sayısı
    """
    # Sinüs fonksiyonunun Taylor serisindeki katsayılar
    katsayilar = [(-1)**i / math.factorial(2*i + 1) for i in range(n)]
    # Hesaplanacak Taylor serisi terimlerini toplamak için bir değişken oluşturun
    taylor_sum = 0
    # Taylor serisinin hesaplanması
    for i, katsayi in enumerate(katsayilar):
        terim = katsayi * x**(2*i + 1)
        taylor_sum += terim
    return taylor_sum

# Pi/4 radyan açısı için sin(x) fonksiyonunu hesaplayın
x = math.pi / 4
# Taylor serisindeki toplam terim sayısı
n = 10
# Sinüs fonksiyonunun Taylor serisine dayalı yaklaşımını hesaplayın
sin_approx = sin_taylor(x, n)
# Gerçek sin(x) değerini hesaplayın
sin_actual = math.sin(x)
# Yaklaşık ve gerçek değerleri yazdırın
print(f"Sin yaklaşımı: {sin_approx}")
print(f"Gerçek sin değeri: {sin_actual}")
