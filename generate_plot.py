import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Kaydedilen grid ve yüzey verilerini yükle
try:
    T = np.load('T_grid.npy')
    S = np.load('S_grid.npy')
    IV_Surface = np.load('IV_surface.npy')

    # Görselleştirme
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(T, S, IV_Surface, cmap=cm.plasma,
                           linewidth=0.1, antialiased=True, alpha=0.9)

    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Implied Volatility (IV)')

    ax.set_xlabel('Vade (Days to Maturity)')
    ax.set_ylabel('Kullanım Fiyatı (Strike)')
    ax.set_zlabel('IV')
    ax.set_title('BRENT Petrol Opsiyon Volatilite Yüzeyi (Cleaned & Interpolated)')

    # Bakış açısını orijinal (Notebook) ayarlarına geri döndürdük
    ax.view_init(elev=25, azim=-130)

    plt.tight_layout()
    # Görseli README'de kullanılmak üzere kaydet
    plt.savefig('volatility_surface_3d.png', dpi=300)
    print("Görsel 'volatility_surface_3d.png' olarak başarıyla kaydedildi.")

except FileNotFoundError:
    print("Hata: Grid veya Yüzey verileri bulunamadı. Lütfen önce Step 2 ve 3'ü çalıştırın.")
