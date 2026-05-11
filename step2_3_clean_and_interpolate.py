import pandas as pd
import numpy as np
from scipy.stats import zscore
from scipy.interpolate import griddata

# 1. Adım'dan gelen veriyi yükleyelim (veya DataFrame'i doğrudan kullanalım)
df = pd.read_csv('noisy_options_data.csv')

# --- ADIM 2: VERİ TEMİZLEME (DATA CLEANING) ---

def clean_option_data(df):
    initial_count = len(df)
    
    # A. Likidite Filtresi: Bid fiyatı 0 olanları çıkar (İşlem görmeyen/derinliksiz opsiyonlar)
    df = df[df['Bid'] > 0].copy()
    
    # B. Eksik Veri Filtresi: IV'si NaN olanları çıkar
    df = df.dropna(subset=['ImpliedVolatility'])
    
    # C. Mantıksal Sınırlar: IV çok düşük veya çok yüksek olamaz (%1 ile %200 arası kabul edelim)
    df = df[(df['ImpliedVolatility'] > 0.01) & (df['ImpliedVolatility'] < 2.0)]
    
    # D. İstatistiksel Aykırı Değer (Outlier) Temizliği: Z-Score Yöntemi
    # IV kolonunda ortalamadan 3 standart sapma uzaklıktaki verileri temizle
    df['iv_zscore'] = zscore(df['ImpliedVolatility'])
    df = df[abs(df['iv_zscore']) < 3]
    
    final_count = len(df)
    print(f"Temizleme Öncesi: {initial_count} | Temizleme Sonrası: {final_count}")
    print(f"Elenen Satır Sayısı: {initial_count - final_count}")
    
    return df

cleaned_df = clean_option_data(df)

# --- ADIM 3: İNTERPOLASYON (CORE INTERPOLATION) ---

def interpolate_volatility_surface(df):
    # Mevcut veri noktaları (X: Vade, Y: Kullanım Fiyatı, Z: IV)
    points = df[['DaysToMaturity', 'Strike']].values
    values = df['ImpliedVolatility'].values
    
    # Hedef ızgara (Grid) oluşturma
    # Daha pürüzsüz bir görüntü için grid yoğunluğunu artırıyoruz
    ti = np.linspace(df['DaysToMaturity'].min(), df['DaysToMaturity'].max(), 50)
    si = np.linspace(df['Strike'].min(), df['Strike'].max(), 50)
    
    T, S = np.meshgrid(ti, si)
    
    # Cubic Interpolation (Daha pürüzsüz yüzey sağlar)
    iv_surface = griddata(points, values, (T, S), method='cubic')
    
    # Kenarlarda kalan NaN değerleri 'linear' ile doldur (Cubic bazen kenarlarda başarısız olabilir)
    nan_mask = np.isnan(iv_surface)
    if nan_mask.any():
        iv_surface[nan_mask] = griddata(points, values, (T[nan_mask], S[nan_mask]), method='linear')
    
    return T, S, iv_surface

T, S, IV_Surface = interpolate_volatility_surface(cleaned_df)

# Sonuçları kaydedelim
cleaned_df.to_csv('cleaned_options_data.csv', index=False)
np.save('T_grid.npy', T)
np.save('S_grid.npy', S)
np.save('IV_surface.npy', IV_Surface)

print("\n--- İnterpolasyon Tamamlandı ---")
print(f"Yüzey Matrisi Boyutu: {IV_Surface.shape}")
