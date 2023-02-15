def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson Metodu kullanarak, f(x) = 0 denkleminin kökünü bulur.
    
    Args:
        f (function): f(x) fonksiyonu
        df (function): f(x) fonksiyonunun türevi olan f'(x) fonksiyonu
        x0 (float): Yaklaşık başlangıç değeri
        tol (float): Yakınsama toleransı
        max_iter (int): Maksimum iterasyon sayısı
        
    Returns:
        float: f(x) = 0 denkleminin bir köküne yaklaşık değer
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Sıfıra bölme hatası!")
        x = x - fx / dfx
    raise ValueError("Yakınsama sağlanamadı.")
    
# f(x) = x^3 - 2 fonksiyonu
def f(x):
    return x ** 3 - 2

# f(x) fonksiyonunun türevi olan f'(x) fonksiyonu
def df(x):
    return 3 * x ** 2

# Yaklaşık başlangıç değeri
x0 = 1.5

# Newton-Raphson Metodu kullanarak, f(x) = 0 denkleminin bir kökünü bulun
x = newton_raphson(f, df, x0)

print("Kök: ", x)
