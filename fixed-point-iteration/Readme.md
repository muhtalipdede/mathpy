Fixed point iteration, matematiksel bir fonksiyonun köklerini veya sabit noktalarını bulmak için kullanılan bir yöntemdir. Bu yöntem, verilen bir başlangıç değerinden başlayarak, belirli bir iterasyon formülünü uygulayarak bir sonraki yaklaşımı hesaplar.

Genel olarak, verilen bir fonksiyonu f(x) ve başlangıç değeri olarak seçilen x0 için, bir sonraki yaklaşım x1 şu şekilde hesaplanabilir:

x1 = g(x0)
Burada, g(x) bir iterasyon fonksiyonudur ve genellikle g(x) = x - f(x)/f'(x) şeklinde tanımlanır. Bu iterasyon formülü, verilen bir fonksiyonun köklerini bulmak için kullanılır.

Aynı şekilde, bir sabit noktayı bulmak için, f(x) = x eşitliğini g(x) = x şeklinde yazabiliriz. Bu durumda, iterasyon formülü aşağıdaki gibi olur:

x1 = g(x0) = f(x0)
Bu formül, başlangıç değeri x0'dan başlayarak, f(x) fonksiyonunun sabit noktasını bulmak için tekrarlanabilir.

Fixed point iteration yöntemi, matematiksel fonksiyonların köklerini ve sabit noktalarını bulmak için yaygın olarak kullanılır. Ancak, bu yöntemin hızlı bir şekilde yakınsaması garanti edilemez. Dahası, bazı durumlarda, iterasyon formülü yanlış seçilirse, yöntem hiç yakınsamayabilir veya yanıltıcı sonuçlar verebilir. Bu nedenle, yöntemin uygulanmasından önce dikkatli bir analiz yapılması ve iterasyon fonksiyonunun doğru bir şekilde seçilmesi önemlidir.