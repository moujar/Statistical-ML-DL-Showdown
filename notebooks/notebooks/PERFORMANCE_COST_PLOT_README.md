# Performance vs Training Cost Plot

This directory contains scripts and LaTeX code to create a "Model Performance vs Training Cost" plot similar to the interpretability trade-off plot, but with actual numerical data.

## Files

1. **`create_performance_cost_plot.py`** - Python script to generate the plot
2. **`performance_cost_plot.tex`** - Basic LaTeX TikZ version
3. **`performance_cost_plot_improved.tex`** - Improved LaTeX version with accurate positioning and labels

## Usage

### Option 1: Python/Matplotlib (Recommended for Quick Visualization)

```python
# Run the Python script
python create_performance_cost_plot.py
```

This will generate:
- `performance_vs_training_cost.png` (high-resolution PNG)
- `performance_vs_training_cost.pdf` (vector PDF)

### Option 2: LaTeX (For Publication/Reports)

```latex
% Include in your LaTeX document:
\input{performance_cost_plot_improved.tex}

% Or compile standalone:
pdflatex performance_cost_plot_improved.tex
```

## Data Source

The plot uses data from `model_comparison.csv` with the following models:

| Model | Training Time (s) | Performance | Category |
|-------|------------------|-------------|----------|
| OLS Regression | 0.0001 | 0.65 | Statistical |
| ANOVA | 0.0001 | 0.55 | Statistical |
| Linear Regression (ML) | 0.0005 | 0.65 | ML |
| Poisson Regression | 0.001 | 0.35 | Statistical |
| Logistic Regression | 0.002 | 0.88 | Statistical |
| Cox Regression | 0.04 | 0.40 | Statistical |
| Random Forest | 0.15 | 0.92 | ML |
| ARIMA | 0.18 | 0.45 | Statistical |
| SVM (SVR) | 0.4 | 0.85 | ML |
| Gradient Boosting | 0.5 | 0.85 | ML |
| RNN/LSTM | 2.5 | 0.89 | ML/DL |

## Features

- **X-axis**: Training Cost (log scale, seconds)
- **Y-axis**: Model Performance (0.2 to 1.0)
- **Curve**: Shows the performance-cost trade-off
- **Ideal Solution**: High performance, low cost (research goal)
- **Color coding**: Statistical (Blue), ML (Purple), Deep Learning (Orange)
- **Actual numbers**: Each point shows (time, performance) values

## Customization

To modify the plot:

1. **Python version**: Edit `create_performance_cost_plot.py` and change:
   - Colors in `category_colors` dictionary
   - Point sizes, labels, etc.

2. **LaTeX version**: Edit `performance_cost_plot_improved.tex` and adjust:
   - Coordinates for each model
   - Colors in `\definecolor` commands
   - Curve path in `\draw` commands

## Requirements

- Python: numpy, pandas, matplotlib (scipy optional for smooth curves)
- LaTeX: TikZ package (included in most LaTeX distributions)

