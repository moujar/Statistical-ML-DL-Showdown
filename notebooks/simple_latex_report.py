#!/usr/bin/env python3
"""
Create a simple LaTeX report with key results
"""

import pandas as pd

def create_simple_latex_report():
    """Create a simple LaTeX report with key results"""
    
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
\\item Average R² Score: {ml_r2_avg:.3f} (Regression)
\\item Average Accuracy: {ml_acc_avg:.3f} (Classification)
\\item Average Training Time: {ml_train_avg:.3f}s
\\item Average Explainability: {ml_exp_avg:.1f}/100
\\item Best Performer: {best_ml_r2['model_name']} (R² = {best_ml_r2['test_r2']:.4f} on {best_ml_r2['dataset']})
\\end{{itemize}}

\\subsubsection{{Statistical Models}}
\\begin{{itemize}}
\\item Average R² Score: {stat_r2_avg:.3f} (Regression)
\\item Average Accuracy: {stat_acc_avg:.3f} (Classification)
\\item Average Training Time: {stat_train_avg:.3f}s
\\item Average Explainability: {stat_exp_avg:.1f}/100
\\item Best Performer: {best_stat_r2['model_name']} (R² = {best_stat_r2['test_r2']:.4f} on {best_stat_r2['dataset']})
\\end{{itemize}}

\\subsection{{Key Insights}}

\\begin{{itemize}}
\\item \\textbf{{Performance:}} ML models show {((ml_r2_avg - stat_r2_avg) / stat_r2_avg * 100):.1f}\\% higher average R² scores
\\item \\textbf{{Speed:}} Statistical models are {ml_train_avg / stat_train_avg:.1f}x faster on average
\\item \\textbf{{Interpretability:}} Statistical models are {stat_exp_avg / ml_exp_avg:.1f}x more interpretable
\\item \\textbf{{Fastest Model:}} {fastest_model['model_name']} ({fastest_model['training_time']:.4f}s)
\\item \\textbf{{Most Interpretable:}} {most_interpretable['model_name']} ({most_interpretable['explainability_score']}/100)
\\end{{itemize}}

\\section{{Detailed Results}}

\\subsection{{Regression Analysis}}

The following table shows the best performing models for each regression dataset:

\\begin{{table}}[h!]
\\centering
\\begin{{tabular}}{{lccc}}
\\toprule
Dataset & Best ML Model & R² Score & Best Statistical Model & R² Score \\\\
\\midrule
"""
    
    # Add regression results
    regression_data = df[df['problem_type'] == 'Regression']
    for dataset in regression_data['dataset'].unique():
        dataset_data = regression_data[regression_data['dataset'] == dataset]
        ml_best = dataset_data[dataset_data['model_category'] == 'ml'].loc[dataset_data[dataset_data['model_category'] == 'ml']['test_r2'].idxmax()]
        stat_best = dataset_data[dataset_data['model_category'] == 'statistical'].loc[dataset_data[dataset_data['model_category'] == 'statistical']['test_r2'].idxmax()]
        
        latex_content += f"{dataset.replace('_', ' ').title()} & {ml_best['model_name']} & {ml_best['test_r2']:.4f} & {stat_best['model_name']} & {stat_best['test_r2']:.4f} \\\\\n"
    
    latex_content += """\\bottomrule
\\end{tabular}
\\caption{Regression Analysis Results}
\\end{table}

\\subsection{Classification Analysis}

The following table shows the best performing models for each classification dataset:

\\begin{table}[h!]
\\centering
\\begin{tabular}{lccc}
\\toprule
Dataset & Best ML Model & Accuracy & Best Statistical Model & Accuracy \\\\
\\midrule
"""
    
    # Add classification results
    classification_data = df[df['problem_type'] == 'Classification']
    for dataset in classification_data['dataset'].unique():
        dataset_data = classification_data[classification_data['dataset'] == dataset]
        ml_best = dataset_data[dataset_data['model_category'] == 'ml'].loc[dataset_data[dataset_data['model_category'] == 'ml']['test_accuracy'].idxmax()]
        stat_best = dataset_data[dataset_data['model_category'] == 'statistical'].loc[dataset_data[dataset_data['model_category'] == 'statistical']['test_accuracy'].idxmax()]
        
        latex_content += f"{dataset.replace('_', ' ').title()} & {ml_best['model_name']} & {ml_best['test_accuracy']:.4f} & {stat_best['model_name']} & {stat_best['test_accuracy']:.4f} \\\\\n"
    
    latex_content += """\\bottomrule
\\end{tabular}
\\caption{Classification Analysis Results}
\\end{table}

\\subsection{Time Series Analysis}

The following table shows the best performing models for each time series dataset:

\\begin{table}[h!]
\\centering
\\begin{tabular}{lccc}
\\toprule
Dataset & Best ML Model & R² Score & Best Statistical Model & R² Score \\\\
\\midrule
"""
    
    # Add time series results
    timeseries_data = df[df['problem_type'] == 'Time Series']
    for dataset in timeseries_data['dataset'].unique():
        dataset_data = timeseries_data[timeseries_data['dataset'] == dataset]
        ml_best = dataset_data[dataset_data['model_category'] == 'ml'].loc[dataset_data[dataset_data['model_category'] == 'ml']['test_r2'].idxmax()]
        stat_best = dataset_data[dataset_data['model_category'] == 'statistical'].loc[dataset_data[dataset_data['model_category'] == 'statistical']['test_r2'].idxmax()]
        
        latex_content += f"{dataset.replace('_', ' ').title()} & {ml_best['model_name']} & {ml_best['test_r2']:.4f} & {stat_best['model_name']} & {stat_best['test_r2']:.4f} \\\\\n"
    
    latex_content += """\\bottomrule
\\end{tabular}
\\caption{Time Series Analysis Results}
\\end{table}

\\subsection{Survival Analysis}

The following table shows the best performing models for each survival analysis dataset:

\\begin{table}[h!]
\\centering
\\begin{tabular}{lccc}
\\toprule
Dataset & Best ML Model & R² Score & Best Statistical Model & R² Score \\\\
\\midrule
"""
    
    # Add survival analysis results
    survival_data = df[df['problem_type'] == 'Survival Analysis']
    for dataset in survival_data['dataset'].unique():
        dataset_data = survival_data[survival_data['dataset'] == dataset]
        ml_best = dataset_data[dataset_data['model_category'] == 'ml'].loc[dataset_data[dataset_data['model_category'] == 'ml']['test_r2'].idxmax()]
        stat_best = dataset_data[dataset_data['model_category'] == 'statistical'].loc[dataset_data[dataset_data['model_category'] == 'statistical']['test_r2'].idxmax()]
        
        latex_content += f"{dataset.replace('_', ' ').title()} & {ml_best['model_name']} & {ml_best['test_r2']:.4f} & {stat_best['model_name']} & {stat_best['test_r2']:.4f} \\\\\n"
    
    latex_content += """\\bottomrule
\\end{tabular}
\\caption{Survival Analysis Results}
\\end{table}

\\section{Conclusions}

\\subsection{Key Findings}

\\begin{enumerate}
\\item \\textbf{Performance:} ML models generally achieve higher accuracy on complex datasets, while statistical models provide consistent, interpretable results.
\\item \\textbf{Speed:} Statistical models are significantly faster for training and prediction, making them suitable for real-time applications.
\\item \\textbf{Interpretability:} Statistical models provide superior interpretability through coefficients, p-values, and confidence intervals.
\\item \\textbf{Domain Suitability:} The choice between approaches depends on the specific problem domain and requirements.
\\end{enumerate}

\\subsection{Recommendations}

\\subsubsection{For Researchers}
\\begin{itemize}
\\item Use statistical models for hypothesis testing and understanding causal relationships
\\item Employ ML models for exploratory analysis and pattern discovery
\\item Consider hybrid approaches combining both methodologies
\\end{itemize}

\\subsubsection{For Practitioners}
\\begin{itemize}
\\item Choose ML models for production systems requiring maximum accuracy
\\item Use statistical models for regulatory compliance and interpretability requirements
\\item Implement both approaches for comprehensive analysis
\\end{itemize}

\\subsubsection{For Organizations}
\\begin{itemize}
\\item Develop expertise in both ML and statistical modeling
\\item Establish clear guidelines for model selection based on requirements
\\item Invest in tools that support both approaches
\\end{itemize}

\\section{Technical Appendix}

\\subsection{Complete Performance Results}

The following table shows all model-dataset combinations with their performance metrics:

\\begin{table}[h!]
\\centering
\\tiny
\\begin{tabular}{llllccc}
\\toprule
Problem Type & Dataset & Model Name & Category & R²/Accuracy & Training Time (s) & Explainability \\\\
\\midrule
"""
    
    # Add all results
    for _, row in df.iterrows():
        metric = row['test_r2'] if row['test_r2'] != 0 else row['test_accuracy']
        latex_content += f"{row['problem_type']} & {row['dataset'].replace('_', ' ').title()} & {row['model_name']} & {row['model_category']} & {metric:.4f} & {row['training_time']:.4f} & {row['explainability_score']} \\\\\n"
    
    latex_content += """\\bottomrule
\\end{tabular}
\\caption{Complete Performance Results}
\\end{table}

\\end{document}
"""
    
    # Write LaTeX file
    with open('simple_analysis_report.tex', 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print("Simple LaTeX document created: simple_analysis_report.tex")

if __name__ == "__main__":
    create_simple_latex_report()
