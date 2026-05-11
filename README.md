# 📈 Options Volatility Surface Cleaner & Interpolator

![Volatility Surface](volatility_surface_3d.png)

This project provides a comprehensive pipeline for processing raw option chain data to construct a smooth and arbitrage-free 3D Implied Volatility (IV) surface. It addresses common real-world data issues such as liquidity gaps, erroneous data entries, and sparse maturity points.

## 📖 Overview

In derivatives trading, the Implied Volatility Surface is a critical tool for pricing, risk management (Greeks), and identifying market anomalies. However, raw data from exchanges often contains noise—zero bids, extreme outliers, or missing values—that can lead to unstable Greeks and incorrect pricing models.

This tool implements a professional-grade workflow to:
1.  **Simulate/Import** raw, noisy option data.
2.  **Clean** data using quantitative filters (Liquidity, Z-Score, logical bounds).
3.  **Interpolate** missing points using advanced mathematical methods to create a continuous grid.
4.  **Visualize** the final surface for qualitative analysis of Skew and Term Structure.

## 🛠️ Key Features

-   **Data Cleaning Pipeline:**
    *   **Liquidity Filter:** Removes options with zero bid prices or insufficient depth.
    *   **Outlier Detection:** Utilizes Z-score analysis to identify and eliminate statistical anomalies in IV.
    *   **Boundary Enforcement:** Filters out nonsensical IV values (e.g., negative or extremely high %500+).
-   **Mathematical Interpolation:**
    *   Employs `SciPy`'s 2D `griddata` with **Cubic Spline** methodology for surface smoothing.
    *   Implements a **Linear Fallback** for boundary conditions where cubic interpolation might result in NaN values.
-   **3D Visualization:**
    *   High-resolution 3D surface mapping using `Matplotlib mplot3d`.
    *   Adjustable perspective to analyze the **Volatility Skew** (across strikes) and **Term Structure** (across time).

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Required Libraries: `pandas`, `numpy`, `scipy`, `matplotlib`

### Installation
```bash
git clone https://github.com/ArifKemal/Options-Surface-Cleaner-and-Interpolator.git
cd Options-Surface-Cleaner-and-Interpolator
pip install -r requirements.txt # Or install the libraries manually
```

### Usage
The most comprehensive way to interact with the project is through the Jupyter Notebook:
1.  Open `Volatility_Surface_Analysis.ipynb`.
2.  Run all cells to see the step-by-step transformation from raw data to the final model.

Alternatively, you can run the modular scripts:
-   `step1_generate_data.py`: Creates the initial noisy dataset.
-   `step2_3_clean_and_interpolate.py`: Performs cleaning and surface construction.
-   `generate_plot.py`: Updates the 3D visualization.

## 📊 Methodology Detail

### Volatility Skew & Smile
The model accounts for the equity-style skew where OTM puts (lower strikes) generally command higher IV than ATM or OTM calls, reflecting market fear of downside moves.

### Grid Construction
The interpolation creates a $50 \times 50$ grid across the time-to-maturity and strike dimensions, providing a granular surface suitable for calculating smooth first and second-order Greeks.

---
*Disclaimer: This project is for educational and research purposes only. It is not intended for live trading or financial advice.*
