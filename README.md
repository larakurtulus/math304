# Math 304 - Numerical Analysis Algorithms 🧮

Bu depo, Nümerik Analiz dersi kapsamında geliştirilen etkileşimli Python algoritmalarını içermektedir. Dönem boyunca işlenen yeni matematiksel yöntemler ve problem çözümleri modüler olarak buraya eklenmeye devam edecektir.

🌟 **ÖNE ÇIKAN: [Master Calculator (Tüm Yöntemler Tek Programda)](math304_master_calculator.py)**
Beş farklı kök bulma algoritmasını (Bisection, Fixed-Point, Newton-Raphson, Secant, Regula Falsi) tek bir interaktif konsol uygulamasında birleştiren ana programdır. DRY prensiplerine uygun modüler yapısı sayesinde esnek ve hatasız bir matematiksel değerlendirme sunar.

---

## 📋 İçindekiler (Table of Contents)

### 1. Kök Bulma Yöntemleri (Root Finding Methods)
* [1.1. Bisection (İkiye Bölme) Yöntemi](#11-bisection-method-calculator-)
* [1.2. Fixed-Point (Sabit Nokta) İterasyonu](#12-fixed-point-iteration-calculator-)
* [1.3. Newton-Raphson Yöntemi](#13-newton-raphson-method-calculator-)
* [1.4. Secant (Kiriş) Yöntemi](#14-secant-method-calculator-)
* [1.5. Regula Falsi (False Position) Yöntemi](#15-regula-falsi-false-position-method-calculator-)

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

---

### 1.2. Fixed-Point Iteration Calculator 🔄
Doğrusal olmayan f(x) = 0 denklemlerini x = g(x) formuna dönüştürerek tek bir başlangıç noktası üzerinden kök arayan algoritmaya dayanır.

**Özellikler (Features):**
* **Esnek Matematik Desteği:** `math` modülündeki tüm fonksiyonları (`sin(x)`, `exp(x)` vb.) doğrudan metin olarak destekler.
* **Iraksama (Divergence) Koruması:** Türev şartının sağlanmadığı durumlarda oluşabilecek matematiksel taşmaları (overflow) yakalayarak programın çökmesini engeller.

---

### 1.3. Newton-Raphson Method Calculator 🚀
Doğrusal olmayan denklemleri çözmek için en güçlü ve hızlı (quadratic convergence) yöntemlerden biridir. Her adımda fonksiyona teğet çizerek köke yaklaşır.

**Özellikler (Features):**
* **Hızlı Yakınsama:** Kök etrafında quadratik (ikinci dereceden) hızla yakınsar.
* **Türev Kontrolü:** Türevin sıfır olduğu noktalarda (division by zero) programın çökmesini engeller.

---

### 1.4. Secant Method Calculator 🌉
Newton yöntemine güçlü bir alternatiftir. Analitik türev hesaplamanın zor veya imkansız olduğu durumlarda, türev yerine son iki noktayı birleştiren bir doğru (secant line) kullanarak kökü bulur.

**Özellikler (Features):**
* **Türevsiz Çalışma:** Fonksiyonun türevini gerektirmez (Derivative-free).
* **Altın Oran Hızı:** Bisection'dan hızlı, Newton'dan biraz yavaş olan yaklaşık 1.618 (Altın Oran) derecesiyle yakınsar.

---

### 1.5. Regula Falsi (False Position) Method Calculator 📏
Bisection yönteminin garantili kök bulma (bracketing) özelliği ile lineer interpolasyonun (doğrusal tahmin) hızını birleştiren gelişmiş bir yöntemdir.

**Özellikler (Features):**
* **Akıllı Tahmin:** Aralığı körü körüne ikiye bölmek yerine, fonksiyon değerlerinin büyüklüğüne göre kök noktasını orantısal olarak tahmin eder.
* **Uç Nokta Durgunluğu Uyarısı:** İterasyon sırasında aralığın bir ucunun sabit kalıp yöntemi yavaşlattığı durumları tespit eder ve uyarır.
