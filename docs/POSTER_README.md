# Poster Compilation Guide

This directory contains LaTeX poster files for research projects.

## Files

### Project Posters:
- `poster.tex` - ML vs Statistical Models comparison (beamerposter package)
- `poster_tikz.tex` - ML vs Statistical Models comparison (tikzposter package, recommended)

### Paper Posters:
- `poster_2507.tex` - Poster for "Transparent AI: The Case for Interpretability and Explainability" (arXiv:2507.23535v1)

## Requirements

You need a LaTeX distribution with the following packages:
- TeX Live (recommended for Linux/Mac)
- MiKTeX (Windows)
- MacTeX (Mac)

### Required LaTeX Packages

**For `poster.tex` (beamerposter version):**
- `beamer` (poster mode)
- `beamerposter` (for A0 poster formatting) - may need separate installation
- `amsmath`, `amsfonts`, `amssymb`
- `graphicx`, `booktabs`, `multirow`, `xcolor`, `tikz`, `pgfplots`

**For `poster_tikz.tex` (tikzposter version - recommended):**
- `tikzposter` (standard package, widely available)
- `amsmath`, `amsfonts`, `amssymb`
- `graphicx`, `booktabs`, `multirow`, `xcolor`, `enumitem`

**Installing missing packages:**
- **TeX Live/MacTeX**: `tlmgr install <package-name>`
- **MiKTeX**: Usually installed automatically when needed

## Compilation Steps

1. **Navigate to the docs directory:**
   ```bash
   cd docs
   ```

2. **Compile the poster:**

   **Option A: Using tikzposter (Recommended - more compatible):**
   ```bash
   pdflatex poster_tikz.tex
   pdflatex poster_tikz.tex  # Run twice for proper cross-references
   ```

   **Option B: Using beamerposter:**
   ```bash
   pdflatex poster.tex
   pdflatex poster.tex  # Run twice for proper cross-references
   ```

   **Option C: Paper poster (Transparent AI):**
   ```bash
   pdflatex poster_2507.tex
   pdflatex poster_2507.tex  # Run twice for proper cross-references
   ```

   Or if you have `latexmk`:
   ```bash
   latexmk -pdf poster_tikz.tex
   # or
   latexmk -pdf poster.tex
   # or
   latexmk -pdf poster_2507.tex
   ```

3. **Output:**
   The compiled PDF will be generated as:
   - `poster_tikz.pdf` or `poster.pdf` (project comparison)
   - `poster_2507.pdf` (Transparent AI paper)

   All outputs are A0 size, suitable for printing.

**Recommendation:** Start with `poster_tikz.tex` or `poster_2507.tex` as they use the more widely available `tikzposter` package. Use `poster.tex` if you have `beamerposter` installed and prefer that style.

## Poster Specifications

- **Size:** A0 (841mm × 1189mm)
- **Orientation:** Portrait
- **Layout:** 3-column format
- **Colors:** 
  - Blue (#3498db) for ML models
  - Red (#e74c3c) for Statistical models
  - Green (#2ecc71) for highlights

## Poster Structure

The poster is organized into three main columns:

### Left Column
- Introduction & Research Question
- Methodology (Problem Domains, Models, Metrics)
- Study Scope

### Middle Column
- Key Results: Performance Summary
- Regression Analysis Results
- Classification Analysis Results
- Time Series & Survival Analysis Results

### Right Column
- Key Insights
- Strategic Recommendations
- Use Case Recommendations
- Conclusions
- Project Information

## Customization

### Colors
The poster uses custom color scheme defined in the preamble:
- `mlcolor`: Blue (#3498db) for ML models
- `statcolor`: Red (#e74c3c) for statistical models
- `accentcolor`: Green (#2ecc71) for highlights

### Adding Images
If you want to include visualization images from the `imgs/` folder, you can add them using:
```latex
\begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{../imgs/performance_comparison.png}
    \caption{Performance Comparison}
\end{figure}
```

### Title Information
Modify the title, author, and institute in the preamble:
```latex
\title{\textbf{Your Title}}
\author{Your Name}
\institute{Your Institution}
```

## Troubleshooting

### Missing tikzposter Package

If you get "tikzposter package not found" error (for `poster_tikz.tex`):

**TeX Live/MacTeX:**
```bash
tlmgr install tikzposter
```

**MiKTeX:**
The package manager should prompt you to install it automatically.

### Missing beamerposter Package

If you get "beamerposter package not found" error (for `poster.tex`):

**TeX Live/MacTeX:**
```bash
tlmgr install beamerposter
```

**Alternative:** Use `poster_tikz.tex` instead, which uses the more standard `tikzposter` package.

### Compilation Errors

- Make sure you're in the `docs/` directory when compiling
- Run `pdflatex` twice to resolve cross-references
- Check that all required packages are installed
- For very large files, you may need to increase TeX memory limits

### Font Size Issues

If the poster appears too large or too small, adjust the scale parameter:
```latex
\usepackage[orientation=portrait,size=a0,scale=1.4]{beamerposter}
```

Change `scale=1.4` to a different value (e.g., `1.2` for smaller, `1.6` for larger).

## Printing

The compiled PDF is in A0 size (841mm × 1189mm), suitable for:
- Conference posters
- Academic presentations
- Research showcases

Most professional printing services accept PDF files. Ensure the PDF is saved with high-quality settings if printing at large sizes.

## Notes

- The poster summarizes findings from 62 model-dataset combinations
- All statistics are based on comprehensive analysis across 4 problem domains
- The layout is optimized for readability at a distance (typical poster viewing)
- Consider printing a test page at A4 size first to check layout and formatting

