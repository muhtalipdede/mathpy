def riemann_sum(s, n):
    """
    Riemann serisi toplamını hesaplar
    :param s: karmaşık sayı (sınırın gerçek kısmı 1'den büyük olmalıdır)
    :param n: seriye dahil edilecek terim sayısı
    :return: Riemann serisi toplamı
    """
    total = 0
    for i in range(1, n+1):
        total += 1 / (i ** s)
    return total

# Örnek kullanım
s = 2 + 3j # sınırın gerçek kısmı 1'den büyük
n = 1000 # 1000 terimli bir seri hesaplayacağız
result = riemann_sum(s, n)
print("Riemann serisi toplamı:", result)
