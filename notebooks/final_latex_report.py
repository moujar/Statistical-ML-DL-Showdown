#!/usr/bin/env python3
"""
Create a final LaTeX report with key results
"""

import pandas as pd

def create_final_latex_report():
    """Create a final LaTeX report with key results"""
    
    # Load the CSV data
    df = pd.read_csv('comprehensive_results/detailed_results.csv')
    
    # Calculate key statistics
    ml_models = df[df['model_category'] == 'ml']
    stat_models = df[df['model_category'] == 'statistical']
    
    total_comparisons = len(df)
    ml_count = len(ml_models)
    stat_count = len(stat_models)
    
    # Performance metrics
    ml_r2_avg = ml_models['test_r2'].mean()
    stat_r2_avg = stat_models['test_r2'].mean()
    ml_acc_avg = ml_models['test_accuracy'].mean()
    stat_acc_avg = stat_models['test_accuracy'].mean()
    
    # Speed metrics
    ml_train_avg = ml_models['training_time'].mean()
    stat_train_avg = stat_models['training_time'].mean()
    
    # Explainability metrics
    ml_exp_avg = ml_models['explainability_score'].mean()
    stat_exp_avg = stat_models['explainability_score'].mean()
    
    # Best performers
    best_ml_r2 = df.loc[df['test_r2'].idxmax()]
    best_stat_r2 = df.loc[df[df['model_category'] == 'statistical']['test_r2'].idxmax()]
    fastest_model = df.loc[df['training_time'].idxmin()]
    most_interpretable = df.loc[df['explainability_score'].idxmax()]
    
    # Create LaTeX content
    latex_content = f"""
\\documentclass[11pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath}}
\\usepackage{{amsfonts}}
\\usepackage{{amssymb}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{array}}
\\usepackage{{geometry}}
\\usepackage{{hyperref}}

\\geometry{{margin=1in}}

\\title{{A Comprehensive Comparative Analysis of Machine Learning and Statistical Models}}
\\author{{ML vs Statistical Models Research Team}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\tableofcontents
\\newpage

\\section{{Executive Summary}}

This study presents a systematic comparison between machine learning (ML) and statistical models across four distinct problem domains: regression, classification, time series analysis, and survival analysis. We evaluated {df['model_name'].nunique()} different models ({ml_count} ML and {stat_count} statistical) on {df['dataset'].nunique()} diverse datasets, conducting {total_comparisons} total comparisons.

\\subsection{{Key Findings}}

\\begin{{itemize}}
\\item \\textbf{{Total Comparisons:}} {total_comparisons} model-dataset combinations
\\item \\textbf{{Problem Domains:}} {df['problem_type'].nunique()} (Regression, Classification, Time Series, Survival Analysis)
\\item \\textbf{{Datasets:}} {df['dataset'].nunique()} diverse datasets
\\item \\textbf{{Models Evaluated:}} {df['model_name'].nunique()} ({ml_count} ML, {stat_count} Statistical)
\\end{{itemize}}

\\subsection{{Performance Summary}}

\\subsubsection{{Machine Learning Models}}
\\begin{{itemize}}
\\item Average R$^2$ Score: {ml_r2_avg:.3f} (Regression)
\\item Average Accuracy: {ml_acc_avg:.3f} (Classification)
\\item Average Training Time: {ml_train_avg:.3f}s
\\item Average Explainability: {ml_exp_avg:.1f}/100
\\item Best Performer: {best_ml_r2['model_name']} (R$^2$ = {best_ml_r2['test_r2']:.4f} on {best_ml_r2['dataset'].replace('_', ' ').title()})
\\end{{itemize}}

\\subsubsection{{Statistical Models}}
\\begin{{itemize}}
\\item Average R$^2$ Score: {stat_r2_avg:.3f} (Regression)
\\item Average Accuracy: {stat_acc_avg:.3f} (Classification)
\\item Average Training Time: {stat_train_avg:.3f}s
\\item Average Explainability: {stat_exp_avg:.1f}/100
\\item Best Performer: {best_stat_r2['model_name']} (R$^2$ = {best_stat_r2['test_r2']:.4f} on {best_stat_r2['dataset'].replace('_', ' ').title()})
\\end{{itemize}}

\\subsection{{Key Insights}}

\\begin{{itemize}}
\\item \\textbf{{Performance:}} ML models show {((ml_r2_avg - stat_r2_avg) / stat_r2_avg * 100):.1f}\\% higher average R$^2$ scores
\\item \\textbf{{Speed:}} Statistical models are {ml_train_avg / stat_train_avg:.1f}x faster on average
\\item \\textbf{{Interpretability:}} Statistical models are {stat_exp_avg / ml_exp_avg:.1f}x more interpretable
\\item \\textbf{{Fastest Model:}} {fastest_model['model_name']} ({fastest_model['training_time']:.4f}s)
\\item \\textbf{{Most Interpretable:}} {most_interpretable['model_name']} ({most_interpretable['explainability_score']}/100)
\\end{{itemize}}

\\section{{Detailed Results by Problem Type}}

\\subsection{{Regression Analysis}}

The regression analysis included {len(df[df['problem_type'] == 'Regression'])} model-dataset combinations across {df[df['problem_type'] == 'Regression']['dataset'].nunique()} datasets.

\\textbf{{Best ML Model:}} {df[df['problem_type'] == 'Regression'].loc[df[df['problem_type'] == 'Regression']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Regression']['test_r2'].max():.4f}

\\textbf{{Best Statistical Model:}} {df[df['problem_type'] == 'Regression'][df[df['problem_type'] == 'Regression']['model_category'] == 'statistical'].loc[df[df['problem_type'] == 'Regression'][df[df['problem_type'] == 'Regression']['model_category'] == 'statistical']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Regression'][df[df['problem_type'] == 'Regression']['model_category'] == 'statistical']['test_r2'].max():.4f}

\\subsection{{Classification Analysis}}

The classification analysis included {len(df[df['problem_type'] == 'Classification'])} model-dataset combinations across {df[df['problem_type'] == 'Classification']['dataset'].nunique()} datasets.

\\textbf{{Best ML Model:}} {df[df['problem_type'] == 'Classification'].loc[df[df['problem_type'] == 'Classification']['test_accuracy'].idxmax()]['model_name']} with Accuracy = {df[df['problem_type'] == 'Classification']['test_accuracy'].max():.4f}

\\textbf{{Best Statistical Model:}} {df[df['problem_type'] == 'Classification'][df[df['problem_type'] == 'Classification']['model_category'] == 'statistical'].loc[df[df['problem_type'] == 'Classification'][df[df['problem_type'] == 'Classification']['model_category'] == 'statistical']['test_accuracy'].idxmax()]['model_name']} with Accuracy = {df[df['problem_type'] == 'Classification'][df[df['problem_type'] == 'Classification']['model_category'] == 'statistical']['test_accuracy'].max():.4f}

\\subsection{{Time Series Analysis}}

The time series analysis included {len(df[df['problem_type'] == 'Time Series'])} model-dataset combinations across {df[df['problem_type'] == 'Time Series']['dataset'].nunique()} datasets.

\\textbf{{Best ML Model:}} {df[df['problem_type'] == 'Time Series'].loc[df[df['problem_type'] == 'Time Series']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Time Series']['test_r2'].max():.4f}

\\textbf{{Best Statistical Model:}} {df[df['problem_type'] == 'Time Series'][df[df['problem_type'] == 'Time Series']['model_category'] == 'statistical'].loc[df[df['problem_type'] == 'Time Series'][df[df['problem_type'] == 'Time Series']['model_category'] == 'statistical']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Time Series'][df[df['problem_type'] == 'Time Series']['model_category'] == 'statistical']['test_r2'].max():.4f}

\\subsection{{Survival Analysis}}

The survival analysis included {len(df[df['problem_type'] == 'Survival Analysis'])} model-dataset combinations across {df[df['problem_type'] == 'Survival Analysis']['dataset'].nunique()} datasets.

\\textbf{{Best ML Model:}} {df[df['problem_type'] == 'Survival Analysis'].loc[df[df['problem_type'] == 'Survival Analysis']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Survival Analysis']['test_r2'].max():.4f}

\\textbf{{Best Statistical Model:}} {df[df['problem_type'] == 'Survival Analysis'][df[df['problem_type'] == 'Survival Analysis']['model_category'] == 'statistical'].loc[df[df['problem_type'] == 'Survival Analysis'][df[df['problem_type'] == 'Survival Analysis']['model_category'] == 'statistical']['test_r2'].idxmax()]['model_name']} with R$^2$ = {df[df['problem_type'] == 'Survival Analysis'][df[df['problem_type'] == 'Survival Analysis']['model_category'] == 'statistical']['test_r2'].max():.4f}

\\section{{Conclusions}}

\\subsection{{Key Findings}}

\\begin{{enumerate}}
\\item \\textbf{{Performance:}} ML models generally achieve higher accuracy on complex datasets, while statistical models provide consistent, interpretable results.
\\item \\textbf{{Speed:}} Statistical models are significantly faster for training and prediction, making them suitable for real-time applications.
\\item \\textbf{{Interpretability:}} Statistical models provide superior interpretability through coefficients, p-values, and confidence intervals.
\\item \\textbf{{Domain Suitability:}} The choice between approaches depends on the specific problem domain and requirements.
\\end{{enumerate}}

\\subsection{{Recommendations}}

\\subsubsection{{For Researchers}}
\\begin{{itemize}}
\\item Use statistical models for hypothesis testing and understanding causal relationships
\\item Employ ML models for exploratory analysis and pattern discovery
\\item Consider hybrid approaches combining both methodologies
\\end{{itemize}}

\\subsubsection{{For Practitioners}}
\\begin{{itemize}}
\\item Choose ML models for production systems requiring maximum accuracy
\\item Use statistical models for regulatory compliance and interpretability requirements
\\item Implement both approaches for comprehensive analysis
\\end{{itemize}}

\\subsubsection{{For Organizations}}
\\begin{{itemize}}
\\item Develop expertise in both ML and statistical modeling
\\item Establish clear guidelines for model selection based on requirements
\\item Invest in tools that support both approaches
\\end{{itemize}}

\\section{{Technical Appendix}}

\\subsection{{Complete Performance Results}}

The analysis included {total_comparisons} total comparisons across {df['problem_type'].nunique()} problem types, {df['dataset'].nunique()} datasets, and {df['model_name'].nunique()} models.

\\textbf{{Model Categories:}}
\\begin{{itemize}}
\\item Machine Learning Models: {ml_count} comparisons
\\item Statistical Models: {stat_count} comparisons
\\end{{itemize}}

\\textbf{{Performance Summary:}}
\\begin{{itemize}}
\\item ML Models Average R$^2$: {ml_r2_avg:.3f}
\\item Statistical Models Average R$^2$: {stat_r2_avg:.3f}
\\item ML Models Average Accuracy: {ml_acc_avg:.3f}
\\item Statistical Models Average Accuracy: {stat_acc_avg:.3f}
\\item ML Models Average Training Time: {ml_train_avg:.3f}s
\\item Statistical Models Average Training Time: {stat_train_avg:.3f}s
\\item ML Models Average Explainability: {ml_exp_avg:.1f}/100
\\item Statistical Models Average Explainability: {stat_exp_avg:.1f}/100
\\end{{itemize}}

\\end{{document}}
"""
    
    # Write LaTeX file
    with open('final_analysis_report.tex', 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print("Final LaTeX document created: final_analysis_report.tex")

if __name__ == "__main__":
    create_final_latex_report()
