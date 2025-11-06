# ML vs Statistical Models Comparison - Notebooks

This directory contains separate Jupyter notebooks for each problem type, allowing for focused analysis and easier experimentation.

## Notebook Structure

### 01_regression.ipynb
**Problem Type:** Regression  
**Datasets:**
- California Housing
- Diabetes
- Wine Quality
- Energy Consumption

**Models:**
- **ML Models:** Scikit-learn Linear Regression, Random Forest, Support Vector Machine, Multi-layer Perceptron
- **Statistical Models:** OLS Regression (statsmodels), Generalized Linear Model (statsmodels)

**Metrics:** R² Score, RMSE, MAE, Training Time, Prediction Time, Memory Usage, Explainability Score

---

### 02_classification.ipynb
**Problem Type:** Classification  
**Datasets:**
- Iris
- Wine Classification
- Breast Cancer
- Credit Default

**Models:**
- **ML Models:** Random Forest, Support Vector Machine, Multi-layer Perceptron
- **Statistical Models:** Logistic Regression (statsmodels), Generalized Linear Model (statsmodels)

**Metrics:** Accuracy, Training Time, Prediction Time, Memory Usage, Explainability Score

---

### 03_time_series.ipynb
**Problem Type:** Time Series Forecasting  
**Datasets:**
- Energy Consumption
- Stock Prices
- Temperature
- Sales Forecasting

**Models:**
- **ML Models:** Multi-layer Perceptron, Random Forest
- **Statistical Models:** Generalized Linear Model (statsmodels)

**Metrics:** R² Score, RMSE, MAE, Training Time, Prediction Time, Memory Usage, Explainability Score

**Special Features:** Time series feature engineering with lagged values, forecast visualizations

---

### 04_survival_analysis.ipynb
**Problem Type:** Survival Analysis  
**Datasets:**
- Customer Churn
- Patient Survival

**Models:**
- **ML Models:** Random Forest
- **Statistical Models:** Cox Regression (lifelines), Kaplan-Meier (lifelines)

**Metrics:** R² Score, RMSE, MAE, Training Time, Prediction Time, Memory Usage, Explainability Score

**Special Features:** Survival curves visualization, censoring handling

---

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Run Notebooks:**
   - Open each notebook in Jupyter Lab/Notebook
   - Run all cells sequentially
   - Each notebook is self-contained and can be run independently

3. **Customization:**
   - Modify dataset parameters in the `load_dataset()` function
   - Adjust model hyperparameters in the model definitions
   - Add new datasets or models by extending the existing functions

## Common Structure

All notebooks follow a similar structure:

1. **Introduction:** Problem type, datasets, and models overview
2. **Imports:** All necessary libraries
3. **Utility Functions:** Dataset loading, data preprocessing, model evaluation, memory tracking
4. **Data Preprocessing:** Comprehensive preprocessing pipeline (see PREPROCESSING_GUIDE.md)
5. **Main Comparison Function:** Orchestrates the comparison for a single dataset
6. **Run Comparisons:** Executes comparisons for all datasets
7. **Visualizations:** Creates performance and comparison plots
8. **Summary Statistics:** Displays aggregated results and key insights

## Data Preprocessing

Each notebook includes comprehensive data preprocessing:

- **Missing Value Handling**: Detection and imputation
- **Outlier Detection**: IQR method for identifying outliers
- **Outlier Handling**: Winsorization (capping outliers)
- **Feature Scaling**: RobustScaler for outlier-resistant scaling
- **Data Validation**: Checks for infinite values and data quality
- **Feature Analysis**: Statistics and multicollinearity checks

See `PREPROCESSING_GUIDE.md` for detailed documentation and `preprocessing_utils.py` for reusable preprocessing functions.

## Output

Each notebook generates:
- **Results DataFrame:** Detailed metrics for each model-dataset combination
- **Visualizations:** Performance comparisons, scatter plots, and specialized plots
- **Summary Statistics:** Best models, fastest models, most interpretable models

## Notes

- All notebooks use synthetic data generation for reproducibility
- Random seeds are fixed (seed=42) for consistent results
- Memory usage tracking may vary based on system resources
- Training times are approximate and depend on hardware

## Requirements

See `../requirements.txt` for all dependencies including:
- scikit-learn
- statsmodels
- lifelines (for survival analysis)
- matplotlib, seaborn (for visualization)
- pandas, numpy (for data manipulation)

