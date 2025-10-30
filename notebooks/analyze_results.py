#!/usr/bin/env python3
"""
Comprehensive Results Analysis Script
Analyzes the detailed results CSV and generates updated reports
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_and_analyze_results():
    """Load and analyze the detailed results CSV"""
    
    # Load the CSV file
    df = pd.read_csv('comprehensive_results/detailed_results.csv')
    
    print("=== COMPREHENSIVE RESULTS ANALYSIS ===")
    print(f"Total comparisons: {len(df)}")
    print(f"Problem types: {df['problem_type'].nunique()}")
    print(f"Datasets: {df['dataset'].nunique()}")
    print(f"Models: {df['model_name'].nunique()}")
    print(f"ML models: {len(df[df['model_category'] == 'ml'])}")
    print(f"Statistical models: {len(df[df['model_category'] == 'statistical'])}")
    
    # Calculate summary statistics
    ml_models = df[df['model_category'] == 'ml']
    stat_models = df[df['model_category'] == 'statistical']
    
    # Performance metrics
    ml_r2_avg = ml_models['test_r2'].mean()
    stat_r2_avg = stat_models['test_r2'].mean()
    
    ml_acc_avg = ml_models['test_accuracy'].mean()
    stat_acc_avg = stat_models['test_accuracy'].mean()
    
    # Training time metrics
    ml_train_avg = ml_models['training_time'].mean()
    stat_train_avg = stat_models['training_time'].mean()
    
    # Explainability metrics
    ml_exp_avg = ml_models['explainability_score'].mean()
    stat_exp_avg = stat_models['explainability_score'].mean()
    
    print(f"\n=== PERFORMANCE SUMMARY ===")
    print(f"ML Models Average R²: {ml_r2_avg:.3f}")
    print(f"Statistical Models Average R²: {stat_r2_avg:.3f}")
    print(f"ML Models Average Accuracy: {ml_acc_avg:.3f}")
    print(f"Statistical Models Average Accuracy: {stat_acc_avg:.3f}")
    print(f"ML Models Average Training Time: {ml_train_avg:.3f}s")
    print(f"Statistical Models Average Training Time: {stat_train_avg:.3f}s")
    print(f"ML Models Average Explainability: {ml_exp_avg:.1f}/100")
    print(f"Statistical Models Average Explainability: {stat_exp_avg:.1f}/100")
    
    # Find best performers
    best_ml_r2 = df.loc[df['test_r2'].idxmax()]
    best_stat_r2 = df.loc[df[df['model_category'] == 'statistical']['test_r2'].idxmax()]
    
    fastest_model = df.loc[df['training_time'].idxmin()]
    most_interpretable = df.loc[df['explainability_score'].idxmax()]
    
    print(f"\n=== BEST PERFORMERS ===")
    print(f"Best ML Model: {best_ml_r2['model_name']} on {best_ml_r2['dataset']} (R² = {best_ml_r2['test_r2']:.4f})")
    print(f"Best Statistical Model: {best_stat_r2['model_name']} on {best_stat_r2['dataset']} (R² = {best_stat_r2['test_r2']:.4f})")
    print(f"Fastest Model: {fastest_model['model_name']} ({fastest_model['training_time']:.4f}s)")
    print(f"Most Interpretable: {most_interpretable['model_name']} ({most_interpretable['explainability_score']}/100)")
    
    # Problem type analysis
    print(f"\n=== PROBLEM TYPE ANALYSIS ===")
    for problem_type in df['problem_type'].unique():
        pt_data = df[df['problem_type'] == problem_type]
        ml_pt = pt_data[pt_data['model_category'] == 'ml']
        stat_pt = pt_data[pt_data['model_category'] == 'statistical']
        
        print(f"\n{problem_type.upper()}:")
        print(f"  ML Models: {len(ml_pt)} comparisons")
        print(f"  Statistical Models: {len(stat_pt)} comparisons")
        if len(ml_pt) > 0:
            print(f"  Best ML: {ml_pt.loc[ml_pt['test_r2'].idxmax()]['model_name']} (R² = {ml_pt['test_r2'].max():.4f})")
        if len(stat_pt) > 0:
            print(f"  Best Statistical: {stat_pt.loc[stat_pt['test_r2'].idxmax()]['model_name']} (R² = {stat_pt['test_r2'].max():.4f})")
    
    return df, {
        'total_comparisons': len(df),
        'problem_types': df['problem_type'].nunique(),
        'datasets': df['dataset'].nunique(),
        'models': df['model_name'].nunique(),
        'ml_models': len(ml_models),
        'stat_models': len(stat_models),
        'ml_r2_avg': ml_r2_avg,
        'stat_r2_avg': stat_r2_avg,
        'ml_acc_avg': ml_acc_avg,
        'stat_acc_avg': stat_acc_avg,
        'ml_train_avg': ml_train_avg,
        'stat_train_avg': stat_train_avg,
        'ml_exp_avg': ml_exp_avg,
        'stat_exp_avg': stat_exp_avg,
        'best_ml_r2': best_ml_r2,
        'best_stat_r2': best_stat_r2,
        'fastest_model': fastest_model,
        'most_interpretable': most_interpretable
    }

def update_technical_appendix(df, stats):
    """Update the technical appendix with actual results"""
    
    print("\n=== UPDATING TECHNICAL APPENDIX ===")
    
    # Read current technical appendix
    with open('TECHNICAL_APPENDIX.md', 'r') as f:
        content = f.read()
    
    # Update summary statistics
    content = content.replace(
        "**Total Comparisons:** 57",
        f"**Total Comparisons:** {stats['total_comparisons']}"
    )
    content = content.replace(
        "**Problem Types:** 4 (Regression, Classification, Time Series, Survival Analysis)",
        f"**Problem Types:** {stats['problem_types']} (Regression, Classification, Time Series, Survival Analysis)"
    )
    content = content.replace(
        "**Datasets:** 12 diverse datasets",
        f"**Datasets:** {stats['datasets']} diverse datasets"
    )
    content = content.replace(
        "**Models:** 9 (4 ML, 5 Statistical)",
        f"**Models:** {stats['models']} ({stats['ml_models']} ML, {stats['stat_models']} Statistical)"
    )
    
    # Update performance statistics
    content = content.replace(
        "- **ML Models Average R²:** 0.742",
        f"- **ML Models Average R²:** {stats['ml_r2_avg']:.3f}"
    )
    content = content.replace(
        "- **Statistical Models Average R²:** 0.641",
        f"- **Statistical Models Average R²:** {stats['stat_r2_avg']:.3f}"
    )
    content = content.replace(
        "- **Performance Difference:** ML models show 15.8% higher average R² scores",
        f"- **Performance Difference:** ML models show {((stats['ml_r2_avg'] - stats['stat_r2_avg']) / stats['stat_r2_avg'] * 100):.1f}% higher average R² scores"
    )
    
    content = content.replace(
        "- **ML Models Average Accuracy:** 0.850",
        f"- **ML Models Average Accuracy:** {stats['ml_acc_avg']:.3f}"
    )
    content = content.replace(
        "- **Statistical Models Average Accuracy:** 0.790",
        f"- **Statistical Models Average Accuracy:** {stats['stat_acc_avg']:.3f}"
    )
    content = content.replace(
        "- **Performance Difference:** ML models show 7.6% higher average accuracy",
        f"- **Performance Difference:** ML models show {((stats['ml_acc_avg'] - stats['stat_acc_avg']) / stats['stat_acc_avg'] * 100):.1f}% higher average accuracy"
    )
    
    content = content.replace(
        "- **ML Models Average Training Time:** 2.847s",
        f"- **ML Models Average Training Time:** {stats['ml_train_avg']:.3f}s"
    )
    content = content.replace(
        "- **Statistical Models Average Training Time:** 0.089s",
        f"- **Statistical Models Average Training Time:** {stats['stat_train_avg']:.3f}s"
    )
    content = content.replace(
        "- **Speed Difference:** Statistical models are 32x faster on average",
        f"- **Speed Difference:** Statistical models are {stats['ml_train_avg'] / stats['stat_train_avg']:.1f}x faster on average"
    )
    
    content = content.replace(
        "- **ML Models Average Score:** 35/100",
        f"- **ML Models Average Score:** {stats['ml_exp_avg']:.1f}/100"
    )
    content = content.replace(
        "- **Statistical Models Average Score:** 85/100",
        f"- **Statistical Models Average Score:** {stats['stat_exp_avg']:.1f}/100"
    )
    content = content.replace(
        "- **Interpretability Difference:** Statistical models are 2.4x more interpretable",
        f"- **Interpretability Difference:** Statistical models are {stats['stat_exp_avg'] / stats['ml_exp_avg']:.1f}x more interpretable"
    )
    
    # Write updated content
    with open('TECHNICAL_APPENDIX.md', 'w') as f:
        f.write(content)
    
    print("Technical appendix updated successfully!")

def update_executive_summary(stats):
    """Update the executive summary with actual results"""
    
    print("\n=== UPDATING EXECUTIVE SUMMARY ===")
    
    # Read current executive summary
    with open('EXECUTIVE_SUMMARY.md', 'r') as f:
        content = f.read()
    
    # Update key statistics
    content = content.replace(
        "- **Total Comparisons:** 57 model-dataset combinations",
        f"- **Total Comparisons:** {stats['total_comparisons']} model-dataset combinations"
    )
    content = content.replace(
        "- **Problem Domains:** 4 (Regression, Classification, Time Series, Survival Analysis)",
        f"- **Problem Domains:** {stats['problem_types']} (Regression, Classification, Time Series, Survival Analysis)"
    )
    content = content.replace(
        "- **Datasets:** 12 diverse datasets ranging from 150 to 35,000 samples",
        f"- **Datasets:** {stats['datasets']} diverse datasets ranging from 150 to 35,000 samples"
    )
    content = content.replace(
        "- **Models Evaluated:** 9 (4 ML, 5 Statistical)",
        f"- **Models Evaluated:** {stats['models']} ({stats['ml_models']} ML, {stats['stat_models']} Statistical)"
    )
    
    # Update performance summary
    content = content.replace(
        "- **Average R² Score:** 0.742 (Regression)",
        f"- **Average R² Score:** {stats['ml_r2_avg']:.3f} (Regression)"
    )
    content = content.replace(
        "- **Average Accuracy:** 0.850 (Classification)",
        f"- **Average Accuracy:** {stats['ml_acc_avg']:.3f} (Classification)"
    )
    content = content.replace(
        "- **Average Training Time:** 2.847s",
        f"- **Average Training Time:** {stats['ml_train_avg']:.3f}s"
    )
    content = content.replace(
        "- **Average Explainability:** 35/100",
        f"- **Average Explainability:** {stats['ml_exp_avg']:.1f}/100"
    )
    content = content.replace(
        "- **Best Performer:** Random Forest (R² = 0.999 on Stock Prices)",
        f"- **Best Performer:** {stats['best_ml_r2']['model_name']} (R² = {stats['best_ml_r2']['test_r2']:.4f} on {stats['best_ml_r2']['dataset']})"
    )
    
    content = content.replace(
        "- **Average R² Score:** 0.641 (Regression)",
        f"- **Average R² Score:** {stats['stat_r2_avg']:.3f} (Regression)"
    )
    content = content.replace(
        "- **Average Accuracy:** 0.790 (Classification)",
        f"- **Average Accuracy:** {stats['stat_acc_avg']:.3f} (Classification)"
    )
    content = content.replace(
        "- **Average Training Time:** 0.089s",
        f"- **Average Training Time:** {stats['stat_train_avg']:.3f}s"
    )
    content = content.replace(
        "- **Average Explainability:** 85/100",
        f"- **Average Explainability:** {stats['stat_exp_avg']:.1f}/100"
    )
    content = content.replace(
        "- **Best Performer:** GLM (R² = 0.999 on Stock Prices)",
        f"- **Best Performer:** {stats['best_stat_r2']['model_name']} (R² = {stats['best_stat_r2']['test_r2']:.4f} on {stats['best_stat_r2']['dataset']})"
    )
    
    # Update key insights
    performance_diff = ((stats['ml_r2_avg'] - stats['stat_r2_avg']) / stats['stat_r2_avg'] * 100)
    speed_ratio = stats['ml_train_avg'] / stats['stat_train_avg']
    interpretability_ratio = stats['stat_exp_avg'] / stats['ml_exp_avg']
    
    content = content.replace(
        "- **ML Models:** 15.8% higher accuracy but 2.4x less interpretable",
        f"- **ML Models:** {performance_diff:.1f}% higher accuracy but {interpretability_ratio:.1f}x less interpretable"
    )
    content = content.replace(
        "- **Statistical Models:** 32x faster training with full interpretability",
        f"- **Statistical Models:** {speed_ratio:.1f}x faster training with full interpretability"
    )
    
    # Write updated content
    with open('EXECUTIVE_SUMMARY.md', 'w') as f:
        f.write(content)
    
    print("Executive summary updated successfully!")

def update_comprehensive_report(stats):
    """Update the comprehensive research report with actual results"""
    
    print("\n=== UPDATING COMPREHENSIVE RESEARCH REPORT ===")
    
    # Read current comprehensive report
    with open('COMPREHENSIVE_RESEARCH_REPORT.md', 'r') as f:
        content = f.read()
    
    # Update abstract
    content = content.replace(
        "We evaluated 9 different models (4 ML and 5 statistical) on 12 diverse datasets, conducting 57 total comparisons.",
        f"We evaluated {stats['models']} different models ({stats['ml_models']} ML and {stats['stat_models']} statistical) on {stats['datasets']} diverse datasets, conducting {stats['total_comparisons']} total comparisons."
    )
    
    # Update results section
    content = content.replace(
        "Our comprehensive analysis of 57 model-dataset combinations revealed significant insights:",
        f"Our comprehensive analysis of {stats['total_comparisons']} model-dataset combinations revealed significant insights:"
    )
    content = content.replace(
        "**Total Comparisons:** 57",
        f"**Total Comparisons:** {stats['total_comparisons']}"
    )
    content = content.replace(
        "**Problem Types:** 4 (Regression, Classification, Time Series, Survival Analysis)",
        f"**Problem Types:** {stats['problem_types']} (Regression, Classification, Time Series, Survival Analysis)"
    )
    content = content.replace(
        "**Datasets:** 12 diverse datasets",
        f"**Datasets:** {stats['datasets']} diverse datasets"
    )
    content = content.replace(
        "**Models:** 9 (4 ML, 5 Statistical)",
        f"**Models:** {stats['models']} ({stats['ml_models']} ML, {stats['stat_models']} Statistical)"
    )
    
    # Write updated content
    with open('COMPREHENSIVE_RESEARCH_REPORT.md', 'w') as f:
        f.write(content)
    
    print("Comprehensive research report updated successfully!")

def create_latex_document():
    """Create a LaTeX document combining all reports"""
    
    print("\n=== CREATING LATEX DOCUMENT ===")
    
    # Read all markdown files
    with open('COMPREHENSIVE_RESEARCH_REPORT.md', 'r') as f:
        comprehensive_report = f.read()
    
    with open('EXECUTIVE_SUMMARY.md', 'r') as f:
        executive_summary = f.read()
    
    with open('TECHNICAL_APPENDIX.md', 'r') as f:
        technical_appendix = f.read()
    
    # Convert markdown to LaTeX (basic conversion)
    def markdown_to_latex(text):
        # Convert headers
        text = text.replace('# ', '\\section{')
        text = text.replace('## ', '\\subsection{')
        text = text.replace('### ', '\\subsubsection{')
        text = text.replace('#### ', '\\paragraph{')
        
        # Close headers
        text = text.replace('\n# ', '}\n\\section{')
        text = text.replace('\n## ', '}\n\\subsection{')
        text = text.replace('\n### ', '}\n\\subsubsection{')
        text = text.replace('\n#### ', '}\n\\paragraph{')
        
        # Add closing brace for last header
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('\\section{') or line.startswith('\\subsection{') or line.startswith('\\subsubsection{') or line.startswith('\\paragraph{'):
                if i + 1 < len(lines) and not lines[i + 1].startswith('\\'):
                    lines[i] += '}'
        text = '\n'.join(lines)
        
        # Convert bold text
        text = text.replace('**', '\\textbf{')
        text = text.replace('**', '}')
        
        # Convert tables (basic)
        text = text.replace('|', ' & ')
        text = text.replace('\n|', '\n\\hline\n|')
        
        # Convert lists
        text = text.replace('- ', '\\item ')
        text = text.replace('\n- ', '\n\\item ')
        
        # Convert code blocks
        text = text.replace('```', '\\begin{verbatim}')
        text = text.replace('```', '\\end{verbatim}')
        
        return text
    
    # Convert markdown to LaTeX
    comprehensive_latex = markdown_to_latex(comprehensive_report)
    executive_latex = markdown_to_latex(executive_summary)
    technical_latex = markdown_to_latex(technical_appendix)
    
    # Create LaTeX document
    latex_content = f"""
\\documentclass[11pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath}}
\\usepackage{{amsfonts}}
\\usepackage{{amssymb}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{longtable}}
\\usepackage{{array}}
\\usepackage{{multirow}}
\\usepackage{{wrapfig}}
\\usepackage{{float}}
\\usepackage{{colortbl}}
\\usepackage{{pdflscape}}
\\usepackage{{tabu}}
\\usepackage{{threeparttable}}
\\usepackage{{threeparttablex}}
\\usepackage{{makecell}}
\\usepackage{{xcolor}}
\\usepackage{{geometry}}
\\geometry{{margin=1in}}

\\title{{A Comprehensive Comparative Analysis of Machine Learning and Statistical Models}}
\\author{{ML vs Statistical Models Research Team}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\tableofcontents
\\newpage

{executive_latex}

\\newpage
{comprehensive_latex}

\\newpage
{technical_latex}

\\end{{document}}
"""
    
    # Write LaTeX file
    with open('comprehensive_analysis_report.tex', 'w') as f:
        f.write(latex_content)
    
    print("LaTeX document created: comprehensive_analysis_report.tex")
    
    # Compile to PDF
    try:
        import subprocess
        result = subprocess.run(['pdflatex', 'comprehensive_analysis_report.tex'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("PDF generated successfully: comprehensive_analysis_report.pdf")
        else:
            print(f"Error compiling LaTeX: {result.stderr}")
    except FileNotFoundError:
        print("pdflatex not found. Please install LaTeX to generate PDF.")
        print("You can manually compile the .tex file using pdflatex.")

if __name__ == "__main__":
    # Load and analyze results
    df, stats = load_and_analyze_results()
    
    # Update all reports
    update_technical_appendix(df, stats)
    update_executive_summary(stats)
    update_comprehensive_report(stats)
    
    # Create LaTeX document
    create_latex_document()
    
    print("\n=== ANALYSIS COMPLETE ===")
    print("All reports have been updated with actual results!")
    print("LaTeX document created for PDF generation.")
