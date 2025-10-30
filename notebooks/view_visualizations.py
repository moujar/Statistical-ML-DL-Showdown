#!/usr/bin/env python3
"""
Simple script to display all generated visualizations
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def display_visualizations():
    """Display all generated visualization files"""
    
    visualization_files = [
        'performance_comparison.png',
        'model_performance_heatmap.png', 
        'speed_vs_performance.png',
        'interpretability_analysis.png',
        'dataset_analysis.png',
        'comprehensive_dashboard.png'
    ]
    
    # Check which files exist
    existing_files = [f for f in visualization_files if os.path.exists(f)]
    
    if not existing_files:
        print("No visualization files found!")
        return
    
    print(f"Found {len(existing_files)} visualization files:")
    for i, file in enumerate(existing_files, 1):
        print(f"{i}. {file}")
    
    print("\nTo view the visualizations:")
    print("1. Open the PNG files in your image viewer")
    print("2. Or run this script with matplotlib backend")
    
    # Try to display if possible
    try:
        for file in existing_files:
            print(f"\nDisplaying {file}...")
            img = mpimg.imread(file)
            plt.figure(figsize=(12, 8))
            plt.imshow(img)
            plt.axis('off')
            plt.title(file.replace('.png', '').replace('_', ' ').title())
            plt.show()
    except Exception as e:
        print(f"Could not display images: {e}")
        print("Please open the PNG files manually to view them.")

if __name__ == "__main__":
    display_visualizations()


