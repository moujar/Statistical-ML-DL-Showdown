#!/usr/bin/env python3
"""
Create comprehensive visualizations for ML vs Statistical Models analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_prepare_data():
    """Load and prepare the data for visualization"""
    df = pd.read_csv('comprehensive_results/detailed_results.csv')
    
    # Clean up model names for better display
    df['model_short'] = df['model_name'].str.replace(' (statsmodels)', '').str.replace(' (lifelines)', '')
    df['model_short'] = df['model_short'].str.replace('Scikit-learn ', '').str.replace('Multi-layer Perceptron', 'MLP')
    
    # Create performance metric (use R² for regression, accuracy for classification)
    df['performance'] = np.where(df['problem_type'] == 'Classification', 
                                df['test_accuracy'], 
                                df['test_r2'])
    
    return df

def create_performance_comparison_plot(df):
    """Create performance comparison between ML and Statistical models"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Performance Comparison: ML vs Statistical Models', fontsize=16, fontweight='bold')
    
    # 1. Overall Performance by Model Category
    ax1 = axes[0, 0]
    category_performance = df.groupby('model_category')['performance'].agg(['mean', 'std']).reset_index()
    bars = ax1.bar(category_performance['model_category'], category_performance['mean'], 
                   yerr=category_performance['std'], capsize=5, alpha=0.7)
    ax1.set_title('Average Performance by Model Category')
    ax1.set_ylabel('Performance Score')
    ax1.set_xlabel('Model Category')
    
    # Add value labels on bars
    for i, (bar, mean_val) in enumerate(zip(bars, category_performance['mean'])):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{mean_val:.3f}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Performance by Problem Type
    ax2 = axes[0, 1]
    problem_performance = df.groupby(['problem_type', 'model_category'])['performance'].mean().unstack()
    problem_performance.plot(kind='bar', ax=ax2, alpha=0.8)
    ax2.set_title('Performance by Problem Type')
    ax2.set_ylabel('Performance Score')
    ax2.set_xlabel('Problem Type')
    ax2.legend(title='Model Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.tick_params(axis='x', rotation=45)
    
    # 3. Training Time Comparison
    ax3 = axes[1, 0]
    time_data = df.groupby('model_category')['training_time'].agg(['mean', 'std']).reset_index()
    bars = ax3.bar(time_data['model_category'], time_data['mean'], 
                   yerr=time_data['std'], capsize=5, alpha=0.7, color=['skyblue', 'lightcoral'])
    ax3.set_title('Average Training Time by Model Category')
    ax3.set_ylabel('Training Time (seconds)')
    ax3.set_xlabel('Model Category')
    ax3.set_yscale('log')
    
    # Add value labels
    for i, (bar, mean_val) in enumerate(zip(bars, time_data['mean'])):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.1, 
                f'{mean_val:.3f}s', ha='center', va='bottom', fontweight='bold')
    
    # 4. Interpretability Comparison
    ax4 = axes[1, 1]
    interpretability_data = df.groupby('model_category')['explainability_score'].agg(['mean', 'std']).reset_index()
    bars = ax4.bar(interpretability_data['model_category'], interpretability_data['mean'], 
                   yerr=interpretability_data['std'], capsize=5, alpha=0.7, color=['lightgreen', 'orange'])
    ax4.set_title('Average Interpretability by Model Category')
    ax4.set_ylabel('Interpretability Score (0-100)')
    ax4.set_xlabel('Model Category')
    ax4.set_ylim(0, 100)
    
    # Add value labels
    for i, (bar, mean_val) in enumerate(zip(bars, interpretability_data['mean'])):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                f'{mean_val:.1f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_model_performance_heatmap(df):
    """Create heatmap showing model performance across datasets"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Model Performance Heatmaps by Problem Type', fontsize=16, fontweight='bold')
    
    problem_types = ['Regression', 'Classification', 'Time Series', 'Survival Analysis']
    
    for idx, problem_type in enumerate(problem_types):
        ax = axes[idx // 2, idx % 2]
        
        # Filter data for this problem type
        problem_data = df[df['problem_type'] == problem_type].copy()
        
        if len(problem_data) > 0:
            # Create pivot table
            pivot_data = problem_data.pivot_table(
                values='performance', 
                index='dataset', 
                columns='model_short', 
                aggfunc='mean'
            )
            
            # Create heatmap
            sns.heatmap(pivot_data, annot=True, fmt='.3f', cmap='RdYlBu_r', 
                       ax=ax, cbar_kws={'label': 'Performance Score'})
            ax.set_title(f'{problem_type} Performance')
            ax.set_xlabel('Model')
            ax.set_ylabel('Dataset')
            
            # Rotate x-axis labels for better readability
            ax.tick_params(axis='x', rotation=45)
            ax.tick_params(axis='y', rotation=0)
    
    plt.tight_layout()
    plt.savefig('model_performance_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_speed_vs_performance_scatter(df):
    """Create scatter plot showing speed vs performance trade-off"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create scatter plot
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        ax.scatter(category_data['training_time'], category_data['performance'], 
                  label=category.title(), alpha=0.7, s=100)
    
    # Add trend lines
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        if len(category_data) > 1:
            z = np.polyfit(category_data['training_time'], category_data['performance'], 1)
            p = np.poly1d(z)
            ax.plot(category_data['training_time'], p(category_data['training_time']), 
                   alpha=0.5, linestyle='--')
    
    ax.set_xlabel('Training Time (seconds)')
    ax.set_ylabel('Performance Score')
    ax.set_title('Speed vs Performance Trade-off')
    ax.set_xscale('log')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add annotations for extreme points
    fastest_idx = df['training_time'].idxmin()
    best_perf_idx = df['performance'].idxmax()
    
    ax.annotate(f'Fastest: {df.loc[fastest_idx, "model_short"]}', 
                xy=(df.loc[fastest_idx, 'training_time'], df.loc[fastest_idx, 'performance']),
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    ax.annotate(f'Best Performance: {df.loc[best_perf_idx, "model_short"]}', 
                xy=(df.loc[best_perf_idx, 'training_time'], df.loc[best_perf_idx, 'performance']),
                xytext=(10, -20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    plt.tight_layout()
    plt.savefig('speed_vs_performance.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_interpretability_analysis(df):
    """Create interpretability analysis plots"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Interpretability Analysis', fontsize=16, fontweight='bold')
    
    # 1. Interpretability vs Performance
    ax1 = axes[0, 0]
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        ax1.scatter(category_data['explainability_score'], category_data['performance'], 
                   label=category.title(), alpha=0.7, s=100)
    
    ax1.set_xlabel('Interpretability Score (0-100)')
    ax1.set_ylabel('Performance Score')
    ax1.set_title('Interpretability vs Performance Trade-off')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Interpretability by Model Type
    ax2 = axes[0, 1]
    model_interpretability = df.groupby('model_short')['explainability_score'].mean().sort_values(ascending=True)
    bars = ax2.barh(range(len(model_interpretability)), model_interpretability.values, alpha=0.7)
    ax2.set_yticks(range(len(model_interpretability)))
    ax2.set_yticklabels(model_interpretability.index)
    ax2.set_xlabel('Interpretability Score (0-100)')
    ax2.set_title('Interpretability by Model')
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, model_interpretability.values)):
        ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                f'{value:.0f}', va='center', fontweight='bold')
    
    # 3. Interpretability Distribution
    ax3 = axes[1, 0]
    df['explainability_score'].hist(bins=20, alpha=0.7, ax=ax3, color='skyblue', edgecolor='black')
    ax3.set_xlabel('Interpretability Score (0-100)')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Distribution of Interpretability Scores')
    ax3.axvline(df['explainability_score'].mean(), color='red', linestyle='--', 
                label=f'Mean: {df["explainability_score"].mean():.1f}')
    ax3.legend()
    
    # 4. Model Category Interpretability Box Plot
    ax4 = axes[1, 1]
    df.boxplot(column='explainability_score', by='model_category', ax=ax4)
    ax4.set_title('Interpretability Distribution by Model Category')
    ax4.set_xlabel('Model Category')
    ax4.set_ylabel('Interpretability Score (0-100)')
    ax4.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.savefig('interpretability_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_dataset_analysis(df):
    """Create dataset-specific analysis plots"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Dataset-Specific Analysis', fontsize=16, fontweight='bold')
    
    # 1. Performance by Dataset Size
    ax1 = axes[0, 0]
    dataset_sizes = {
        'iris': 150, 'wine_classification': 178, 'diabetes': 442, 'breast_cancer': 569,
        'wine_quality': 1599, 'temperature': 1000, 'sales_forecasting': 2000,
        'stock_prices': 2500, 'patient_survival': 5000, 'customer_churn': 10000,
        'california_housing': 20640, 'energy_consumption': 35000
    }
    
    df['dataset_size'] = df['dataset'].map(dataset_sizes)
    df['dataset_size_log'] = np.log10(df['dataset_size'])
    
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        ax1.scatter(category_data['dataset_size_log'], category_data['performance'], 
                   label=category.title(), alpha=0.7, s=100)
    
    ax1.set_xlabel('Dataset Size (log10)')
    ax1.set_ylabel('Performance Score')
    ax1.set_title('Performance vs Dataset Size')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Training Time vs Dataset Size
    ax2 = axes[0, 1]
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        ax2.scatter(category_data['dataset_size_log'], category_data['training_time'], 
                   label=category.title(), alpha=0.7, s=100)
    
    ax2.set_xlabel('Dataset Size (log10)')
    ax2.set_ylabel('Training Time (seconds)')
    ax2.set_title('Training Time vs Dataset Size')
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Best Model per Dataset
    ax3 = axes[1, 0]
    best_models = df.loc[df.groupby('dataset')['performance'].idxmax()]
    model_counts = best_models['model_category'].value_counts()
    
    wedges, texts, autotexts = ax3.pie(model_counts.values, labels=model_counts.index, 
                                      autopct='%1.1f%%', startangle=90)
    ax3.set_title('Best Performing Model Category per Dataset')
    
    # 4. Performance Range by Dataset
    ax4 = axes[1, 1]
    dataset_stats = df.groupby('dataset')['performance'].agg(['min', 'max', 'mean']).reset_index()
    dataset_stats['range'] = dataset_stats['max'] - dataset_stats['min']
    
    bars = ax4.bar(range(len(dataset_stats)), dataset_stats['range'], alpha=0.7)
    ax4.set_xticks(range(len(dataset_stats)))
    ax4.set_xticklabels([d.replace('_', ' ').title() for d in dataset_stats['dataset']], 
                        rotation=45, ha='right')
    ax4.set_ylabel('Performance Range')
    ax4.set_title('Performance Range by Dataset')
    
    plt.tight_layout()
    plt.savefig('dataset_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_summary_dashboard(df):
    """Create a comprehensive summary dashboard"""
    fig = plt.figure(figsize=(20, 12))
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    
    # Main title
    fig.suptitle('ML vs Statistical Models: Comprehensive Analysis Dashboard', 
                 fontsize=20, fontweight='bold', y=0.95)
    
    # 1. Performance comparison (top left)
    ax1 = fig.add_subplot(gs[0, 0])
    category_performance = df.groupby('model_category')['performance'].mean()
    bars = ax1.bar(category_performance.index, category_performance.values, 
                   color=['skyblue', 'lightcoral'], alpha=0.8)
    ax1.set_title('Average Performance', fontweight='bold')
    ax1.set_ylabel('Performance Score')
    for i, (bar, value) in enumerate(zip(bars, category_performance.values)):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{value:.3f}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Speed comparison (top center)
    ax2 = fig.add_subplot(gs[0, 1])
    category_speed = df.groupby('model_category')['training_time'].mean()
    bars = ax2.bar(category_speed.index, category_speed.values, 
                   color=['lightgreen', 'orange'], alpha=0.8)
    ax2.set_title('Average Training Time', fontweight='bold')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_yscale('log')
    for i, (bar, value) in enumerate(zip(bars, category_speed.values)):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.1, 
                f'{value:.3f}s', ha='center', va='bottom', fontweight='bold')
    
    # 3. Interpretability comparison (top right)
    ax3 = fig.add_subplot(gs[0, 2])
    category_interpretability = df.groupby('model_category')['explainability_score'].mean()
    bars = ax3.bar(category_interpretability.index, category_interpretability.values, 
                   color=['gold', 'purple'], alpha=0.8)
    ax3.set_title('Average Interpretability', fontweight='bold')
    ax3.set_ylabel('Score (0-100)')
    ax3.set_ylim(0, 100)
    for i, (bar, value) in enumerate(zip(bars, category_interpretability.values)):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
    
    # 4. Model count (top far right)
    ax4 = fig.add_subplot(gs[0, 3])
    model_counts = df['model_category'].value_counts()
    wedges, texts, autotexts = ax4.pie(model_counts.values, labels=model_counts.index, 
                                      autopct='%1.1f%%', startangle=90)
    ax4.set_title('Model Distribution', fontweight='bold')
    
    # 5. Performance by problem type (middle left)
    ax5 = fig.add_subplot(gs[1, :2])
    problem_performance = df.groupby(['problem_type', 'model_category'])['performance'].mean().unstack()
    problem_performance.plot(kind='bar', ax=ax5, alpha=0.8)
    ax5.set_title('Performance by Problem Type', fontweight='bold')
    ax5.set_ylabel('Performance Score')
    ax5.set_xlabel('Problem Type')
    ax5.legend(title='Model Category')
    ax5.tick_params(axis='x', rotation=45)
    
    # 6. Speed vs Performance scatter (middle right)
    ax6 = fig.add_subplot(gs[1, 2:])
    for category in df['model_category'].unique():
        category_data = df[df['model_category'] == category]
        ax6.scatter(category_data['training_time'], category_data['performance'], 
                   label=category.title(), alpha=0.7, s=80)
    ax6.set_xlabel('Training Time (seconds)')
    ax6.set_ylabel('Performance Score')
    ax6.set_title('Speed vs Performance Trade-off', fontweight='bold')
    ax6.set_xscale('log')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # 7. Top performing models (bottom)
    ax7 = fig.add_subplot(gs[2, :])
    top_models = df.nlargest(10, 'performance')[['model_short', 'dataset', 'performance', 'model_category']]
    y_pos = np.arange(len(top_models))
    
    colors = ['skyblue' if cat == 'ml' else 'lightcoral' for cat in top_models['model_category']]
    bars = ax7.barh(y_pos, top_models['performance'], color=colors, alpha=0.8)
    
    ax7.set_yticks(y_pos)
    ax7.set_yticklabels([f"{model} ({dataset})" for model, dataset in 
                        zip(top_models['model_short'], top_models['dataset'])])
    ax7.set_xlabel('Performance Score')
    ax7.set_title('Top 10 Performing Model-Dataset Combinations', fontweight='bold')
    ax7.invert_yaxis()
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, top_models['performance'])):
        ax7.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, 
                f'{value:.3f}', va='center', fontweight='bold')
    
    plt.savefig('comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function to create all visualizations"""
    print("Loading data...")
    df = load_and_prepare_data()
    
    print("Creating performance comparison plots...")
    create_performance_comparison_plot(df)
    
    print("Creating model performance heatmaps...")
    create_model_performance_heatmap(df)
    
    print("Creating speed vs performance analysis...")
    create_speed_vs_performance_scatter(df)
    
    print("Creating interpretability analysis...")
    create_interpretability_analysis(df)
    
    print("Creating dataset analysis...")
    create_dataset_analysis(df)
    
    print("Creating comprehensive dashboard...")
    create_summary_dashboard(df)
    
    print("All visualizations created successfully!")
    print("Generated files:")
    print("- performance_comparison.png")
    print("- model_performance_heatmap.png")
    print("- speed_vs_performance.png")
    print("- interpretability_analysis.png")
    print("- dataset_analysis.png")
    print("- comprehensive_dashboard.png")

if __name__ == "__main__":
    main()


