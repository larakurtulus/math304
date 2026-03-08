# Math 304 - Numerical Analysis Algorithms 🧮

Bu depo, Nümerik Analiz dersi kapsamında geliştirilen etkileşimli Python algoritmalarını içermektedir. Dönem boyunca işlenen yeni matematiksel yöntemler ve problem çözümleri modüler olarak buraya eklenmeye devam edecektir.

---

## 📋 İçindekiler (Table of Contents)

### 1. Kök Bulma Yöntemleri (Root Finding Methods)
* [1.1. Bisection (İkiye Bölme) Yöntemi](#11-bisection-method-calculator-)
* [1.2. Fixed-Point (Sabit Nokta) İterasyonu](#12-fixed-point-iteration-calculator-)
* [1.3. Newton-Raphson Yöntemi](#13-newton-raphson-method-calculator-)
* [1.4. Secant (Kiriş) Yöntemi](#14-secant-method-calculator-)

### 2. Gelecek Konu Başlıkları (Planlanan)
* *Doğrusal Denklem Sistemleri (Linear Systems)*
* *İnterpolasyon ve Eğri Uydurma (Interpolation & Curve Fitting)*
* *Sayısal İntegral (Numerical Integration)*

---

## 1. Kök Bulma Yöntemleri (Root Finding Methods)

### 1.1. Bisection Method Calculator 🧮
Mühendislikte karşılaşılan doğrusal olmayan denklemlerin köklerini bulmak için en güvenilir yöntemlerden biri olan **İkiye Bölme (Bisection)** algoritmasını kullanır.

**Özellikler (Features):**
* **Adım Adım İzleme:** Her iterasyonda aralığın nasıl daraldığını adım adım konsola yazdırır.
* **Güvenlik Kontrolü:** Ara Değer Teoremi'ni test ederek başlangıç aralığının doğruluğunu en başta denetler.

**Nasıl Kullanılır? (Usage):**
Konsol sizden f(x) denklemini (Örn: `x**3 - x - 2`), aralık sınırlarını (Örn: `1` ve `2`) ve hata toleransını isteyecektir.

---

### 1.2. Fixed-Point Iteration Calculator 🔄
Doğrusal olmayan f(x) = 0 denklemlerini x = g(x) formuna dönüştürerek tek bir başlangıç noktası üzerinden kök arayan algoritmaya dayanır.

**Özellikler (Features):**
* **Esnek Matematik Desteği:** `math` modülündeki tüm fonksiyonları (`sin(x)`, `exp(x)` vb.) doğrudan metin olarak destekler.
* **Iraksama (Divergence) Koruması:** Türev şartının sağlanmadığı durumlarda oluşabilecek matematiksel taşmaları (overflow) yakalayarak programın çökmesini engeller.
* **Bağıl Hata Kontrolü:** İterasyonları durdurmak için iki adım arasındaki ardışık bağıl hatayı (relative error) ölçer.

**Nasıl Kullanılır? (Usage):**
Konsol sizden yeniden düzenlenmiş g(x) denklemini (Örn: `(x+1)**(1/3)`), başlangıç tahminini (Örn: `x0 = 1`) ve hedeflenen toleransı isteyecektir.

---

### 1.3. Newton-Raphson Method Calculator 🚀
Doğrusal olmayan denklemleri çözmek için en güçlü ve hızlı (quadratic convergence) yöntemlerden biridir. Her adımda fonksiyona teğet çizerek köke yaklaşır.

**Özellikler (Features):**
* **Hızlı Yakınsama:** Kök etrafında quadratik (ikinci dereceden) hızla yakınsar.
* **Türev Kontrolü:** Türevin sıfır olduğu noktalarda (division by zero) programın çökmesini engeller.
* **Çift Durma Kriteri:** Hem yer değiştirme (relative displacement) hem de kalıntı (residual) toleranslarını eşzamanlı kontrol eder.

**Nasıl Kullanılır? (Usage):**
Konsol sizden f(x) denklemini (Örn: `x**3 - x - 2`), bu denklemin türevini olan f'(x)'i (Örn: `3*x**2 - 1`), başlangıç tahminini (`x0`) ve hata toleransını isteyecektir.

---

### 1.4. Secant Method Calculator 🌉
Newton yöntemine güçlü bir alternatiftir. Analitik türev hesaplamanın zor veya imkansız olduğu durumlarda, türev yerine son iki noktayı birleştiren bir doğru (secant line) kullanarak kökü bulur.

**Özellikler (Features):**
* **Türevsiz Çalışma:** Fonksiyonun türevini gerektirmez (Derivative-free).
* **Altın Oran Hızı:** Bisection'dan hızlı, Newton'dan biraz yavaş olan yaklaşık 1.618 (Altın Oran) derecesiyle yakınsar.
* **Payda Koruması:** f(x_n) ile f(x_{n-1}) değerlerinin birbirine çok yaklaştığı durumlarda sıfıra bölünme hatasını engeller.

**Nasıl Kullanılır? (Usage):**
Konsol sizden f(x) denklemini (Örn: `exp(x) - 3`), iki farklı başlangıç tahminini (Örn: `x0 = 0`, `x1 = 2`) ve hata toleransını isteyecektir.
