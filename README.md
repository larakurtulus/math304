# Math 304 - Numerical Analysis Algorithms 🧮

Bu depo, Nümerik Analiz dersi kapsamında geliştirilen etkileşimli Python algoritmalarını içermektedir. Dönem boyunca işlenen yeni matematiksel yöntemler ve problem çözümleri modüler olarak buraya eklenmeye devam edecektir.

---

## 📋 İçindekiler (Table of Contents)

### 1. Kök Bulma Yöntemleri (Root Finding Methods)
* [1.1. Bisection (İkiye Bölme) Yöntemi](#11-bisection-method-calculator-)
* [1.2. Fixed-Point (Sabit Nokta) İterasyonu](#12-fixed-point-iteration-calculator-)
* *Newton-Raphson Yöntemi (İleride eklenecek)*
* *Secant Yöntemi (İleride eklenecek)*

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
