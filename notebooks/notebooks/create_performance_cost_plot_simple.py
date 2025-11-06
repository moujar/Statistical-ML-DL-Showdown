"""
Create Performance vs Training Cost Plot - Simple version without pandas
Similar to interpretability plot but with Performance vs Training Cost
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data from model_comparison.csv
models = [
    'OLS Regression', 'ANOVA', 'Linear Regression (ML)', 'Poisson Regression',
    'Logistic Regression', 'Cox Regression', 'Random Forest', 'ARIMA',
    'SVM (SVR)', 'Gradient Boosting', 'RNN/LSTM (PyTorch)'
]

training_times = [
    0.0001, 0.0001, 0.0005, 0.001, 0.002, 0.04, 0.15, 0.18, 0.4, 0.5, 2.5
]

performances = [
    0.65, 0.55, 0.65, 0.35, 0.88, 0.40, 0.92, 0.45, 0.85, 0.85, 0.89
]

categories = [
    'Statistical', 'Statistical', 'ML', 'Statistical', 'Statistical', 
    'Statistical', 'ML', 'Statistical', 'ML', 'ML', 'ML/DL'
]

# Define model categories and colors
category_colors = {
    'Statistical': '#2E86AB',  # Blue
    'ML': '#A23B72',  # Purple
    'ML/DL': '#F18F01'  # Orange
}

# Convert to numpy arrays
training_times = np.array(training_times)
performances = np.array(performances)

# Use log scale for training time for better visualization
log_training_times = np.log10(training_times + 1e-6)

# Create the plot - smaller and more compact
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor('white')

# Plot each model as a point with algorithm name
for i, (model, perf, time, cat) in enumerate(zip(models, performances, training_times, categories)):
    color = category_colors.get(cat, '#666666')
    ax.scatter(log_training_times[i], perf, s=200, alpha=0.7, 
               color=color, edgecolors='black', linewidths=1.5, zorder=3)
    
    # Add algorithm name label with better positioning
    offset_x = 0.05  # Fixed offset to the right
    offset_y = 0.02 if perf < 0.7 else -0.02  # Above or below based on position
    
    # Shorten long names for better readability
    display_name = model
    if len(model) > 20:
        # Shorten very long names
        if 'Regression' in model:
            display_name = model.replace(' Regression', ' Reg.')
        if 'PyTorch' in model:
            display_name = model.replace(' (PyTorch)', '')
        if 'Linear Regression' in model:
            display_name = model.replace('Linear Regression', 'Linear Reg.')
    
    ax.annotate(display_name, 
                xy=(log_training_times[i], perf),
                xytext=(log_training_times[i] + offset_x, perf + offset_y),
                fontsize=8, ha='left', va='bottom' if perf < 0.7 else 'top',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, 
                         edgecolor=color, linewidth=1.2),
                weight='bold')

# Removed trend line for cleaner visualization
# Points show the performance-cost relationship without connecting line

# Add "Ideal Solution" point (high performance, low cost) - very clear and prominent
# Position in top-left corner (high performance, low cost)
ideal_x = log_training_times.min() - 0.35
ideal_y = performances.max() + 0.1

# Large, hollow circle with thick border - very visible
ax.scatter([ideal_x], [ideal_y], s=500, facecolors='none', 
          edgecolors='#6C5CE7', linewidths=3, zorder=6, marker='o', alpha=0.9)

# Add inner point for emphasis
ax.scatter([ideal_x], [ideal_y], s=100, color='#6C5CE7', 
          edgecolors='white', linewidths=1, zorder=7, marker='o', alpha=0.8)

# Clear, prominent label positioned well
ax.annotate('Ideal solution', 
            xy=(ideal_x, ideal_y),
            xytext=(ideal_x - 0.3, ideal_y + 0.12),
            fontsize=13, fontweight='bold', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.95, 
                     edgecolor='#6C5CE7', linewidth=2.5),
            color='#6C5CE7')

# Add research arrow pointing to ideal - clear and prominent
avg_log_time = np.mean(log_training_times)
avg_perf = np.mean(performances)
arrow = mpatches.FancyArrowPatch(
    (avg_log_time + 0.1, avg_perf),
    (ideal_x + 0.1, ideal_y - 0.05),
    arrowstyle='->', mutation_scale=30, color='#E74C3C', linewidth=3, zorder=3
)
ax.add_patch(arrow)
# Label along the arrow path
ax.text((avg_log_time + ideal_x) / 2 + 0.1, 
        (avg_perf + ideal_y) / 2 + 0.04,
        'Efficient ML Research', fontsize=10, fontweight='bold', 
        color='#E74C3C', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                 edgecolor='#E74C3C', linewidth=2))

# Set labels and title
ax.set_xlabel('Training Cost (log scale, seconds)', fontsize=12, fontweight='bold')
ax.set_ylabel('Model Performance', fontsize=12, fontweight='bold')
ax.set_title('Model Performance vs Training Cost Trade-off', fontsize=13, fontweight='bold', pad=12)

# Customize axes - remove numerical labels, keep only Low/High
# Set ticks but don't show labels
x_ticks = np.array([-6, -5, -4, -3, -2, -1, 0, 1])
ax.set_xticks(x_ticks)
ax.set_xticklabels([''] * len(x_ticks))  # Empty labels

# Remove y-axis numerical labels too
ax.set_yticklabels([])

# Add axis arrows
ax.annotate('', xy=(1, 0), xytext=(0.95, 0), 
            arrowprops=dict(arrowstyle='->', lw=2, color='black'),
            xycoords='axes fraction', textcoords='axes fraction')
ax.annotate('', xy=(0, 1), xytext=(0, 0.95), 
            arrowprops=dict(arrowstyle='->', lw=2, color='black'),
            xycoords='axes fraction', textcoords='axes fraction')

# Add Low/High labels only (no numbers)
ax.text(0.98, 0.02, 'High', transform=ax.transAxes, fontsize=12, ha='right', fontweight='bold', color='black')
ax.text(0.02, 0.98, 'High', transform=ax.transAxes, fontsize=12, ha='left', fontweight='bold', va='top', color='black')
ax.text(0.98, 0.98, 'Low', transform=ax.transAxes, fontsize=12, ha='right', fontweight='bold', va='top', color='black')
ax.text(0.02, 0.02, 'Low', transform=ax.transAxes, fontsize=12, ha='left', fontweight='bold', color='black')

# Add grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Set axis limits - ensure ideal solution is clearly visible
ax.set_xlim(log_training_times.min() - 0.5, max(log_training_times.max(), ideal_x) + 0.3)
ax.set_ylim(0.25, ideal_y + 0.15)

# Add legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=category_colors['Statistical'], 
               markersize=12, label='Statistical Models', markeredgecolor='black', markeredgewidth=1.5),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=category_colors['ML'], 
               markersize=12, label='ML Models', markeredgecolor='black', markeredgewidth=1.5),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=category_colors['ML/DL'], 
               markersize=12, label='Deep Learning Models', markeredgecolor='black', markeredgewidth=1.5),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10, framealpha=0.95)

plt.tight_layout()

# Save as PNG and PDF
plt.savefig('performance_vs_training_cost.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('performance_vs_training_cost.pdf', bbox_inches='tight', facecolor='white')
print("✅ Plot saved as 'performance_vs_training_cost.png' and 'performance_vs_training_cost.pdf'")

# Also show the plot
plt.show()

