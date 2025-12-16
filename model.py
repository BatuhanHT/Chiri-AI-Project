import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. VERİ OLUŞTURMA VE HAZIRLIK
# ---------------------------------------------------------
# Sabit sonuç için seed
np.random.seed(42)

# Geçmiş 15 günün (örnek veri) sıcaklık verilerini oluştur
# Tahmin için yeterli geçmiş veri olması gerekir (7 gün + test)
gecmis_gun_sayisi = 15
gecmis_sicaklik_tum = np.random.randint(15, 30, gecmis_gun_sayisi).tolist()
gunler_tum = [f"{i}. Gün" for i in range(1, gecmis_gun_sayisi + 1)]

# Son 7 gün (Hareketli ortalama penceresi)
gecmis_7_gun_sicaklik = gecmis_sicaklik_tum[-7:]
gunler_7_gun = gunler_tum[-7:]

# Yarınki (8. gün) sıcaklık için rastgele bir gerçek değer oluşturalım (Test için)
gercek_yarin_sicaklik = np.random.randint(18, 28)

# ---------------------------------------------------------
# 2. HAREKETLİ ORTALAMA YÖNTEMİ İLE TAHMİN
# ---------------------------------------------------------
# NumPy kullanarak son 7 günün ortalamasını al
tahmin_sicaklik = np.mean(gecmis_7_gun_sicaklik)

# Tahmin sonucunu yuvarla
tahmin_sicaklik_yuvarlanmis = round(tahmin_sicaklik, 1)

# Tahmin metni
sonuc_metni = (
    f"Son 7 Günlük Hareketli Ortalama Tahmini: {tahmin_sicaklik_yuvarlanmis}°C\n"
    f"(Gerçek Yarınki Sıcaklık: {gercek_yarin_sicaklik}°C)"
)

print("\n--- 🌡️ BASİT SICAKLIK TAHMİN SİSTEMİ (Hareketli Ortalama) ---")
print("-" * 60)
print(f"Son 7 Gün Sıcaklıkları: {gecmis_7_gun_sicaklik}")
print(f"Ortalama Tahmini: {tahmin_sicaklik_yuvarlanmis}°C")
print(f"Gerçek Değer (Simülasyon): {gercek_yarin_sicaklik}°C")
print("-" * 60)
print("Grafik penceresi açılıyor...")

# ---------------------------------------------------------
# 3. GRAFİK ÇİZİMİ (KURUMSAL TASARIM)
# ---------------------------------------------------------

# Grafikte gösterilecek tüm veriler (Son 7 gün + Tahmin + Gerçek Yarın)
tum_gunler_grafik = gunler_7_gun + ["TAHMİN", "GERÇEK YARIN"]
tum_sicaklik_grafik = gecmis_7_gun_sicaklik + [tahmin_sicaklik_yuvarlanmis, gercek_yarin_sicaklik]

# Sıcaklıklar
sicakliklar = np.array(gecmis_7_gun_sicaklik)

# Grafik Ayarları
plt.figure(figsize=(12, 7))

# --- Çizgi 1: Geçmiş 7 Gün Sıcaklıkları ---
plt.plot(gunler_7_gun, sicakliklar, color='#2563eb', marker='o', linewidth=2, label='Geçmiş Sıcaklıklar')
plt.fill_between(gunler_7_gun, sicakliklar, color='#3b82f6', alpha=0.1) # Altını doldur

# --- Tahmin Noktası (Kırmızı Yıldız) ---
# Tahmin noktası 8. pozisyonda
plt.scatter(tum_gunler_grafik[-2], tahmin_sicaklik_yuvarlanmis, 
            s=400, c='#ef4444', marker='*', edgecolors='white', zorder=10, label=f'Tahmin: {tahmin_sicaklik_yuvarlanmis}°C')

# --- Gerçek Değer Noktası (Yeşil Üçgen) ---
# Gerçek değer noktası 9. pozisyonda
plt.scatter(tum_gunler_grafik[-1], gercek_yarin_sicaklik, 
            s=200, c='#10b981', marker='^', edgecolors='white', zorder=10, label=f'Gerçek Değer: {gercek_yarin_sicaklik}°C')

# --- Geçmiş 7 Günü Tahmine Bağlayan Kesik Çizgi ---
tahmin_cizgi_x = [gunler_7_gun[-1], tum_gunler_grafik[-2]]
tahmin_cizgi_y = [gecmis_7_gun_sicaklik[-1], tahmin_sicaklik_yuvarlanmis]
plt.plot(tahmin_cizgi_x, tahmin_cizgi_y, color='#ef4444', linestyle=':', linewidth=1)

# Başlık ve Etiketler
plt.title("Son 7 Gün Sıcaklık Trendi ve Yarın Tahmini (Hareketli Ortalama)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Zaman Çizelgesi", fontsize=11)
plt.ylabel("Sıcaklık (°C)", fontsize=11)

# Sadece 7 gün, Tahmin ve Gerçek Yarın etiketlerini göster
plt.xticks(tum_gunler_grafik, rotation=45, ha='right')

# Izgara ve Arkaplan
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(loc='upper left', frameon=True, shadow=True, fontsize=10)

# Alt tarafa not düşme
plt.figtext(0.5, 0.01, sonuc_metni, 
            ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.8, "pad":5})

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# HAREKETLİ ORTALAMA TANIMI
# ---------------------------------------------------------
print("\n--- 💡 Hareketli Ortalama (Moving Average) Nedir? ---")
print("Hareketli Ortalama, bir zaman serisindeki verilerin, belirli bir 'pencere' uzunluğu (bizim örneğimizde 7 gün) boyunca hesaplanan ortalamasıdır.")
print("Bu yöntem, kısa vadeli rastgele dalgalanmaları (gürültüyü) yumuşatarak ana trendi ortaya çıkarmayı ve gelecekteki bir değeri tahmin etmeyi amaçlar.")
print("Formül: $MA = \\frac{P_t + P_{t-1} + \\dots + P_{t-N+1}}{N}$")
print("Burada $P$ sıcaklık değerini, $t$ zamanı ve $N$ pencere uzunluğunu (7) temsil eder.")