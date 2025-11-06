"""
Data Preprocessing Utilities for ML vs Statistical Models Comparison

This module provides comprehensive preprocessing functions for regression and classification tasks.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler


def preprocess_regression_data(X, y, feature_names):
    """
    Comprehensive data preprocessing pipeline for regression problems.
    
    Parameters:
    -----------
    X : array-like
        Feature matrix
    y : array-like
        Target vector
    feature_names : list
        List of feature names
        
    Returns:
    --------
    X_processed : ndarray
        Preprocessed feature matrix
    y_processed : ndarray
        Preprocessed target vector
    feature_names : list
        Feature names (unchanged)
    """
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    
    print("📊 Data Preprocessing:")
    print("-" * 60)
    
    # 1. Data Exploration
    print(f"\n1. Data Shape: {df.shape}")
    print(f"   Features: {len(feature_names)}")
    print(f"   Samples: {len(df)}")
    print(f"   Target range: [{y.min():.2f}, {y.max():.2f}]")
    print(f"   Target mean: {y.mean():.2f}, std: {y.std():.2f}")
    
    # 2. Missing Values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print(f"\n2. Missing Values Found:")
        print(missing_values[missing_values > 0])
        df = df.fillna(df.mean())
    else:
        print("\n2. Missing Values: None ✓")
    
    # 3. Infinite Values
    inf_values = np.isinf(df.select_dtypes(include=[np.number])).sum()
    if inf_values.sum() > 0:
        print(f"\n3. Infinite Values Found:")
        print(inf_values[inf_values > 0])
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.fillna(df.mean())
    else:
        print("\n3. Infinite Values: None ✓")
    
    # 4. Outlier Detection and Handling
    print("\n4. Outlier Detection (IQR method):")
    outliers_count = 0
    for col in feature_names:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        if IQR > 0:  # Avoid division by zero
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            if outliers > 0:
                outliers_count += outliers
                df[col] = np.clip(df[col], lower_bound, upper_bound)
    if outliers_count > 0:
        print(f"   Found and capped {outliers_count} outliers")
    else:
        print("   No outliers detected ✓")
    
    # 5. Feature Statistics
    print("\n5. Feature Statistics:")
    print(f"   Mean ranges: [{df[feature_names].mean().min():.2f}, {df[feature_names].mean().max():.2f}]")
    print(f"   Std ranges: [{df[feature_names].std().min():.2f}, {df[feature_names].std().max():.2f}]")
    
    # 6. Multicollinearity Check
    print("\n6. Multicollinearity Check:")
    corr_matrix = df[feature_names].corr().abs()
    high_corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if corr_matrix.iloc[i, j] > 0.8:
                high_corr_pairs.append((
                    corr_matrix.columns[i], 
                    corr_matrix.columns[j], 
                    corr_matrix.iloc[i, j]
                ))
    if high_corr_pairs:
        print(f"   Found {len(high_corr_pairs)} highly correlated feature pairs (>0.8)")
        for pair in high_corr_pairs[:3]:
            print(f"   {pair[0]} - {pair[1]}: {pair[2]:.3f}")
    else:
        print("   No high multicollinearity detected ✓")
    
    X_processed = df[feature_names].values
    y_processed = df['target'].values
    
    print("\n✅ Preprocessing completed!")
    print("-" * 60)
    
    return X_processed, y_processed, feature_names


def preprocess_classification_data(X, y, feature_names):
    """
    Comprehensive data preprocessing pipeline for classification problems.
    
    Parameters:
    -----------
    X : array-like
        Feature matrix
    y : array-like
        Target vector
    feature_names : list
        List of feature names
        
    Returns:
    --------
    X_processed : ndarray
        Preprocessed feature matrix
    y_processed : ndarray
        Preprocessed target vector
    feature_names : list
        Feature names (unchanged)
    """
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    
    print("📊 Data Preprocessing:")
    print("-" * 60)
    
    # 1. Data Exploration
    print(f"\n1. Data Shape: {df.shape}")
    print(f"   Features: {len(feature_names)}")
    print(f"   Samples: {len(df)}")
    print(f"   Classes: {len(np.unique(y))}")
    
    # 2. Missing Values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print(f"\n2. Missing Values Found:")
        print(missing_values[missing_values > 0])
        df = df.fillna(df.mean())
    else:
        print("\n2. Missing Values: None ✓")
    
    # 3. Infinite Values
    inf_values = np.isinf(df.select_dtypes(include=[np.number])).sum()
    if inf_values.sum() > 0:
        print(f"\n3. Infinite Values Found:")
        print(inf_values[inf_values > 0])
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.fillna(df.mean())
    else:
        print("\n3. Infinite Values: None ✓")
    
    # 4. Outlier Detection and Handling
    print("\n4. Outlier Detection (IQR method):")
    outliers_count = 0
    for col in feature_names:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        if IQR > 0:  # Avoid division by zero
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            if outliers > 0:
                outliers_count += outliers
                df[col] = np.clip(df[col], lower_bound, upper_bound)
    if outliers_count > 0:
        print(f"   Found and capped {outliers_count} outliers")
    else:
        print("   No outliers detected ✓")
    
    # 5. Feature Statistics
    print("\n5. Feature Statistics:")
    print(f"   Mean ranges: [{df[feature_names].mean().min():.2f}, {df[feature_names].mean().max():.2f}]")
    print(f"   Std ranges: [{df[feature_names].std().min():.2f}, {df[feature_names].std().max():.2f}]")
    
    # 6. Class Distribution
    print("\n6. Class Distribution:")
    class_counts = pd.Series(y).value_counts().sort_index()
    for cls, count in class_counts.items():
        pct = 100 * count / len(y)
        print(f"   Class {cls}: {count} ({pct:.1f}%)")
    
    X_processed = df[feature_names].values
    y_processed = df['target'].values
    
    print("\n✅ Preprocessing completed!")
    print("-" * 60)
    
    return X_processed, y_processed, feature_names

