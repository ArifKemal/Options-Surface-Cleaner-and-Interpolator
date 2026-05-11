# Project Overview: Options Volatility Surface Cleaner & Interpolator

This project is a high-quality "Showcase" Quant tool designed to process noisy and incomplete real-world option chain data. It cleans the data using statistical methods and interpolates missing Implied Volatility (IV) points to create a smooth 3D Volatility Surface, essential for derivatives pricing and risk management.

## 🛠️ Main Technologies
- **Python**: Core programming language.
- **Pandas & NumPy**: Data manipulation and numerical computations.
- **SciPy**: Statistical filtering (Z-score) and mathematical interpolation (Cubic Griddata).
- **Matplotlib (mplot3d)**: Professional 3D visualization.

## 📂 Project Structure
- `Options_Surface_Project/`: Contains the main source files.
  - `Volatility_Surface_Analysis.ipynb`: The primary "Showcase" notebook.
  - `step1_generate_data.py`: Script for generating the noisy mock data.
  - `step2_3_clean_and_interpolate.py`: Script for cleaning and interpolation logic.
- `README.md`: Project introduction and showcase details.
- `*.csv` & `*.npy`: Local data storage for simulations.

## 🚀 Building and Running
The project is designed to be run within a Jupyter environment.

1.  **Environment Setup**:
    ```bash
    pip install pandas numpy scipy matplotlib
    ```
2.  **Running the Analysis**:
    - Open `Options_Surface_Project/Volatility_Surface_Analysis.ipynb` in Jupyter Notebook or VS Code.
    - Execute the cells sequentially to see the transformation from raw data to a smooth 3D surface.
3.  **Standalone Scripts**:
    - You can also run the individual Python scripts in the `Options_Surface_Project` directory to regenerate data or test logic.

## 📐 Development Conventions
- **Quant Workflow**: Always follow the "Clean -> Interpolate -> Validate -> Visualize" pipeline.
- **Data Integrity**: Never use raw, noisy data for surface construction without applying Z-score or liquidity filters.
- **Visuals**: Use Matplotlib's 3D tools (mplot3d) for Markdown-compatible rendering instead of interactive libraries for GitHub visibility.
- **Math**: Prefer `Cubic` interpolation for surface smoothing, with `Linear` fallbacks for boundary points.
