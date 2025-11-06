# LaTeX Presentation Guide

This directory contains a Beamer presentation for the ML vs Statistical Models comparison project.

## File

- `presentation.tex` - The main LaTeX Beamer presentation file

## Compilation

### Requirements

You need a LaTeX distribution with Beamer class installed:
- TeX Live (recommended for Linux/Mac)
- MiKTeX (Windows)
- MacTeX (Mac)

### Required LaTeX Packages

The presentation uses the following packages (usually included in standard distributions):
- `beamer` (Madrid theme)
- `amsmath`, `amsfonts`, `amssymb`
- `graphicx`
- `booktabs`
- `multirow`
- `xcolor`
- `tikz`
- `pgfplots`

### Compilation Steps

1. **Navigate to the docs directory:**
   ```bash
   cd docs
   ```

2. **Compile the presentation:**
   ```bash
   pdflatex presentation.tex
   pdflatex presentation.tex  # Run twice for proper cross-references
   ```

   Or if you have `latexmk`:
   ```bash
   latexmk -pdf presentation.tex
   ```

3. **Output:**
   The compiled PDF will be generated as `presentation.pdf`

## Presentation Structure

The presentation includes the following sections:

1. **Introduction**
   - Research question
   - Scope of the study

2. **Methodology**
   - Evaluation framework
   - Performance, efficiency, and interpretability metrics

3. **Results**
   - Overall performance summary
   - Winners by category
   - Regression analysis
   - Classification analysis
   - Time series analysis
   - Survival analysis

4. **Key Insights**
   - Performance vs interpretability trade-off
   - Speed analysis
   - Interpretability gap

5. **Recommendations**
   - When to choose statistical models
   - When to choose ML models
   - Use case recommendations

6. **Conclusions**
   - Key takeaways
   - Strategic recommendations
   - Future research directions

## Customization

### Colors

The presentation uses custom color scheme defined in the preamble:
- `mlcolor`: Blue (#3498db) for ML models
- `statcolor`: Red (#e74c3c) for statistical models
- `accentcolor`: Green (#2ecc71) for highlights

### Theme

Currently uses the Madrid theme. You can change it by modifying:
```latex
\usetheme{Madrid}
```

Other popular Beamer themes: `Berlin`, `Darmstadt`, `Frankfurt`, `Montpellier`, `Singapore`, `et al.`

### Adding Images

If you want to include visualization images from the `imgs/` folder, uncomment and modify:
```latex
\titlegraphic{\includegraphics[width=2cm]{../imgs/comprehensive_dashboard.png}}
```

You can also add images within frames using:
```latex
\begin{figure}
    \includegraphics[width=0.8\textwidth]{../imgs/performance_comparison.png}
    \caption{Performance Comparison}
\end{figure}
```

### Title Page Information

Modify the title, author, and institute in the preamble:
```latex
\title[Short Title]{Full Title}
\author{Your Name}
\institute{Your Institution}
```

## Troubleshooting

### Missing Packages

If you get "Package not found" errors:
- **TeX Live/MacTeX**: Install missing packages via `tlmgr install <package>`
- **MiKTeX**: Packages are usually installed automatically

### Compilation Errors

- Make sure you're in the `docs/` directory when compiling
- Run `pdflatex` twice to resolve cross-references
- Check that all required packages are installed

### Image Paths

If you uncomment the `\titlegraphic` line, ensure the image path is correct relative to where you're compiling from.

## Notes

- The presentation is set to 16:9 aspect ratio (modern widescreen format)
- All results and statistics are based on the comprehensive analysis of 62 model-dataset combinations
- The presentation is designed to be approximately 20-25 minutes long when presented

