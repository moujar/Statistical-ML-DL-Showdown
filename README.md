# Bridging the Gap: Statistical vs Machine Learning Methods

**Performance, Cost, and Interpretability Trade-offs in the Age of Transparent AI**

A comprehensive comparative study evaluating statistical and machine learning approaches across multiple problem domains, quantifying fundamental trade-offs between performance, computational cost, and interpretability.

---

## 📋 Overview

This project presents a systematic comparison between traditional statistical methods and modern machine learning approaches across four distinct problem domains: **regression**, **classification**, **time series analysis**, and **survival analysis**. The study evaluates 13 model-dataset combinations to provide evidence-based recommendations for model selection in the context of Transparent AI.

### Core Research Question

*How do Machine Learning and Statistical models compare across different problem domains in terms of:*
- **Performance** (accuracy, R², RMSE)
- **Cost** (training time, computational resources)
- **Interpretability** (explainability, statistical inference)

---

## 🎯 Key Findings

### Performance Summary

| Metric | Statistical Models | ML/DL Models |
|--------|-------------------|--------------|
| **Avg Performance (R²/Acc)** | 0.547 | **0.818** |
| **Avg Training Time** | **0.037s** | 0.763s |
| **Interpretability** | **88.3/100** | 37.4/100 |
| **Efficiency (Perf/Cost)** | **High** | Medium |

### Main Insights

- **Statistical models excel in:**
  - Interpretability: 2.4x higher (88.3/100 vs 37.4/100)
  - Speed: 20-100x faster training
  - Efficiency: 6435.64 vs 0.36 efficiency scores
  - Regulatory compliance and hypothesis testing

- **ML/DL models excel in:**
  - Complex dataset performance: 1.5x higher (0.818 vs 0.547)
  - Scalability to large data
  - Capturing non-linear patterns
  - Handling complex temporal dependencies

**Conclusion:** No universal winner - the optimal choice depends on specific requirements including regulatory constraints, dataset characteristics, and computational resources.

---

## 📁 Repository Structure

```
StatisVsML/
│
├── notebooks/              # Jupyter notebooks with complete analysis
│   ├── 01_regression.ipynb                    # Regression analysis
│   ├── 02_classification.ipynb                # Classification analysis
│   ├── 03_Poisson_Cox_regression_vs_Gradient_Boosting_Machines.ipynb
│   ├── 04_survival_analysis.ipynb            # Survival analysis
│   ├── 05_Arima_RNN.ipynb                     # Time series analysis
│   └── full_comprasion.ipynb                  # Comprehensive summary
│
├── docs/                   # Documentation and reports
│   ├── report.tex          # Full research report (LaTeX)
│   ├── report.pdf          # Compiled report
│   ├── poster.tex          # Conference poster (LaTeX)
│   ├── poster.pdf          # Compiled poster
│   └── presentation.tex    # Presentation slides
│
├── imgs/                   # Visualizations and figures
│   ├── bridging_gap.png    # Performance vs Interpretability trade-off
│   ├── CostVsPerformance.png                  # Performance vs Cost analysis
│   └── Fused Trade-off: Performance vs. Cost vs. Interpretability.png
│
├── paper/                  # Reference papers and literature
│
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- LaTeX distribution (for compiling reports and poster)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd StatisVsML
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Required Packages

- **Core ML and Statistical Libraries:**
  - scikit-learn (≥1.3.0)
  - numpy (≥1.24.0)
  - pandas (≥2.0.0)
  - scipy (≥1.10.0)
  - statsmodels (≥0.14.0)

- **Visualization:**
  - matplotlib (≥3.7.0)
  - seaborn (≥0.12.0)
  - plotly (≥5.15.0)

- **Survival Analysis:**
  - lifelines (≥0.27.0)

- **Deep Learning:**
  - PyTorch (for LSTM/RNN models)

- **Jupyter:**
  - jupyter (≥1.0.0)
  - ipywidgets (≥8.0.0)

---

## 📊 Usage Guide

### Running the Analysis

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```

2. **Execute notebooks in order:**
   - Start with `01_regression.ipynb` for regression analysis
   - Continue with `02_classification.ipynb` for classification
   - Follow with `03_Poisson_Cox_regression_vs_Gradient_Boosting_Machines.ipynb`
   - Then `04_survival_analysis.ipynb` for survival analysis
   - Next `05_Arima_RNN.ipynb` for time series
   - Finally `full_comprasion.ipynb` for comprehensive summary

3. **View Results:**
   - All visualizations are generated inline in the notebooks
   - Key figures are saved in the `imgs/` directory

### Compiling Documentation

**Compile the report:**
```bash
cd docs
pdflatex report.tex
bibtex report  # if using bibliography
pdflatex report.tex
pdflatex report.tex
```

**Compile the poster:**
```bash
cd docs
pdflatex poster.tex
```

---

## 📓 Notebook Descriptions

### 01_regression.ipynb
**Regression Analysis: OLS vs ML Linear Regression**
- Datasets: California Housing, Diabetes, Wine Quality, Energy Consumption
- Models: OLS Regression (statsmodels) vs Linear Regression (scikit-learn)
- Focus: Statistical inference vs prediction optimization

### 02_classification.ipynb
**Classification Analysis: Logistic Regression vs Random Forest**
- Datasets: Iris, Wine Classification, Breast Cancer, Credit Default
- Models: Logistic Regression (statsmodels) vs Random Forest (scikit-learn)
- Focus: Interpretability vs predictive power trade-off

### 03_Poisson_Cox_regression_vs_Gradient_Boosting_Machines.ipynb
**Survival Analysis: Statistical vs ML Approaches**
- Models: Poisson Regression, Cox Regression vs Gradient Boosting
- Focus: Handling censored data and survival outcomes

### 04_survival_analysis.ipynb
**Comprehensive Survival Analysis**
- Extended survival analysis with multiple datasets
- Comparison of statistical and ML methods for time-to-event data

### 05_Arima_RNN.ipynb
**Time Series Analysis: ARIMA vs LSTM/RNN**
- Datasets: Energy Consumption, Temperature, Sales Forecasting
- Models: ARIMA (statsmodels) vs LSTM/RNN (PyTorch)
- Focus: Classical time series methods vs deep learning

### full_comprasion.ipynb
**Comprehensive Summary and Comparison**
- Synthesizes all previous analyses
- Integrated trade-off visualization
- Model selection framework

---

## 🔬 Methodology

### Study Scope

- **4 Problem Domains:** Regression, Classification, Time Series, Survival Analysis
- **13 Datasets:** Ranging from 150 to 35,000 samples
- **5 Statistical Models:** OLS Regression, Logistic Regression, ANOVA, ARIMA, Cox/Poisson Regression
- **5 ML/DL Models:** Linear Regression, Random Forest, SVM, RNN/LSTM, Gradient Boosting
- **13 Model-Dataset Combinations:** Comprehensive pairwise comparisons

### Experimental Design

1. **Data Preprocessing:**
   - Standardized train/test split (80/20)
   - Feature scaling (StandardScaler, RobustScaler)
   - Identical preprocessing for fair comparison

2. **Evaluation Metrics:**
   - **Performance:** R² (regression), Accuracy (classification)
   - **Cost:** Training time (seconds), computational resources
   - **Interpretability:** Composite score (0-100) based on transparency, statistical inference, explanation methods, and documentation

3. **Fair Comparison:**
   - Both model types trained on identical preprocessed data
   - Standardized evaluation protocols
   - Consistent hyperparameter tuning approaches

---

## 📈 Key Visualizations

The project includes three main visualizations:

1. **Performance vs Interpretability Trade-off** (`bridging_gap.png`)
   - Shows the traditional inverse relationship
   - Highlights Interpretable ML research direction

2. **Performance vs Training Cost** (`CostVsPerformance.png`)
   - Scatter plot showing cost-performance trade-offs
   - Model clustering by type

3. **Integrated Trade-off Analysis** (`Fused Trade-off: Performance vs. Cost vs. Interpretability.png`)
   - Three-dimensional visualization
   - Bubble size represents interpretability
   - Color coding by model type

---

## 🏆 Winners by Category

| Category | Winner | Performance |
|----------|--------|-------------|
| Best Overall Accuracy | Random Forest (ML) | 0.920 |
| Fastest Training | OLS Regression (Stat) | 0.0001s |
| Most Interpretable | OLS Regression (Stat) | 100/100 |
| Best Efficiency | OLS Regression (Stat) | 6435.64 |
| Best Time Series (Simple) | ARIMA (Stat) | R² = 0.972 |
| Best Time Series (Complex) | LSTM (DL) | R² = 0.890 |
| Best Survival Analysis | Poisson Regression (Stat) | R² = 0.340 |

---

## 📚 References

- Rudin, C., & Radin, J. (2019). Why Are We Using Black Box Models in AI When We Don't Need To? A Lesson From An Explainable AI Competition. *Harvard Data Science Review*.

- Arrieta, A. B., et al. (2020). Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges. *Information Fusion*, 58, 82-115.

- Ramachandram, D., Joshi, H., Zhu, J., Gandhi, D., Hartman, L., & Raval, A. (2025). Transparent AI: The Case for Interpretability and Explainability. arXiv:2507.23535v1 [cs.LG]

Additional references are available in the `paper/` directory and cited in the full report.

---

**Last Updated:** 2025

