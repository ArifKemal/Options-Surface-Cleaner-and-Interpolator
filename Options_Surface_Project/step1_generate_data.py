import pandas as pd
import numpy as np

# Rastgelelik için seed sabitleyelim
np.random.seed(42)

def generate_noisy_option_data():
    # 1. Temel Parametreler
    underlying_price = 450
    strikes = np.arange(380, 521, 5)
    maturities = np.array([15, 30, 60, 90, 180, 270, 360])
    
    data = []
    
    # 2. Opsiyon Zinciri Oluşturma
    for t in maturities:
        for s in strikes:
            # Teorik bir "Volatility Smile" ve "Skew" oluşturalım
            # Mesafe (Moneyness)
            dist = (s - underlying_price) / underlying_price
            
            # Temel IV: Skew + Smile + Time etkisi
            # IV = Base + Linear Skew + Quadratic Smile + Term Structure
            base_iv = 0.15 + (-0.2 * dist) + (0.5 * (dist**2)) + (0.02 * np.sqrt(t/365))
            
            # Bid/Ask Spread (Derinlik azaldıkça artar)
            spread = 0.05 + abs(dist) * 0.2
            bid = (1 - spread/2) * 5.0 # Sembolik bir fiyat
            ask = (1 + spread/2) * 5.0
            
            data.append({
                'Strike': s,
                'DaysToMaturity': t,
                'Bid': round(max(0, bid), 2),
                'Ask': round(ask, 2),
                'ImpliedVolatility': base_iv
            })

    df = pd.DataFrame(data)

    # 3. KASITLI GÜRÜLTÜ VE HATA EKLEME (Noise Injection)
    
    # A. NaN Değerler (Eksik Veriler)
    nan_indices = df.sample(frac=0.1).index
    df.loc[nan_indices, 'ImpliedVolatility'] = np.nan
    
    # B. Outliers (Aşırı Uç Değerler)
    # %500 IV (Hatalı veri girişi simülasyonu)
    outlier_indices = df.sample(n=5).index
    df.loc[outlier_indices, 'ImpliedVolatility'] = 5.0 
    
    # %0 IV (Sıfır volatilite hatası)
    zero_iv_indices = df.sample(n=5).index
    df.loc[zero_iv_indices, 'ImpliedVolatility'] = 0.0
    
    # C. Likidite Sorunları (Bid = 0)
    # Çok derin OTM veya ITM opsiyonlarda bid'in olmaması
    df.loc[(df['Strike'] > 500) | (df['Strike'] < 400), 'Bid'] = df.apply(
        lambda x: 0 if np.random.random() > 0.7 else x['Bid'], axis=1
    )

    return df

# Veriyi üret ve ilk 10 satırı göster
raw_options_data = generate_noisy_option_data()
raw_options_data.to_csv('noisy_options_data.csv', index=False)

print("--- Ham (Gürültülü) Veri Seti Özeti ---")
print(raw_options_data.head(15))
print("\nİstatistiksel Özet (IV Kolonu):")
print(raw_options_data['ImpliedVolatility'].describe())
print(f"\nToplam NaN Sayısı (IV): {raw_options_data['ImpliedVolatility'].isna().sum()}")
