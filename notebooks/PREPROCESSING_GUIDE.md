# Data Preprocessing Guide

This guide explains the comprehensive preprocessing steps that should be added to all notebooks.

## Why Preprocessing is Important

Proper data preprocessing is crucial for:
- **Model Performance**: Clean data leads to better model accuracy
- **Model Stability**: Handling outliers and missing values prevents model failures
- **Fair Comparison**: Ensures all models are evaluated on the same clean data
- **Real-world Applicability**: Real datasets always need preprocessing

## Preprocessing Pipeline

### 1. Data Exploration
```python
print(f"Data Shape: {X.shape}")
print(f"Features: {len(feature_names)}")
print(f"Samples: {len(X)}")
print(f"Target range: [{y.min():.2f}, {y.max():.2f}]")
```

### 2. Missing Values Handling
```python
missing_values = pd.DataFrame(X, columns=feature_names).isnull().sum()
if missing_values.sum() > 0:
    print(f"Missing Values Found: {missing_values[missing_values > 0]}")
    # Mean imputation for numeric features
    X = pd.DataFrame(X, columns=feature_names).fillna(
        pd.DataFrame(X, columns=feature_names).mean()
    ).values
else:
    print("No missing values ✓")
```

### 3. Infinite Values Handling
```python
df = pd.DataFrame(X, columns=feature_names)
inf_values = np.isinf(df.select_dtypes(include=[np.number])).sum()
if inf_values.sum() > 0:
    print(f"Infinite Values Found: {inf_values[inf_values > 0]}")
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(df.mean())
    X = df.values
else:
    print("No infinite values ✓")
```

### 4. Outlier Detection and Handling
```python
from sklearn.preprocessing import RobustScaler

def detect_and_handle_outliers(X, feature_names, method='iqr'):
    """Detect and handle outliers using IQR method."""
    df = pd.DataFrame(X, columns=feature_names)
    outliers_count = 0
    
    for col in feature_names:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        if outliers > 0:
            outliers_count += outliers
            # Winsorization: cap outliers
            df[col] = np.clip(df[col], lower_bound, upper_bound)
    
    if outliers_count > 0:
        print(f"Found and capped {outliers_count} outliers")
    else:
        print("No outliers detected ✓")
    
    return df.values

X = detect_and_handle_outliers(X, feature_names)
```

### 5. Feature Statistics
```python
df = pd.DataFrame(X, columns=feature_names)
print(f"Feature means: [{df.mean().min():.2f}, {df.mean().max():.2f}]")
print(f"Feature stds: [{df.std().min():.2f}, {df.std().max():.2f}]")
```

### 6. Multicollinearity Check (for Regression)
```python
def check_multicollinearity(X, feature_names, threshold=0.8):
    """Check for highly correlated features."""
    corr_matrix = pd.DataFrame(X, columns=feature_names).corr().abs()
    high_corr_pairs = []
    
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if corr_matrix.iloc[i, j] > threshold:
                high_corr_pairs.append((
                    corr_matrix.columns[i], 
                    corr_matrix.columns[j], 
                    corr_matrix.iloc[i, j]
                ))
    
    if high_corr_pairs:
        print(f"Found {len(high_corr_pairs)} highly correlated pairs (>0.8)")
        for pair in high_corr_pairs[:5]:  # Show first 5
            print(f"  {pair[0]} - {pair[1]}: {pair[2]:.3f}")
    else:
        print("No high multicollinearity detected ✓")
    
    return high_corr_pairs

check_multicollinearity(X, feature_names)
```

### 7. Feature Scaling
```python
from sklearn.preprocessing import RobustScaler, StandardScaler

# Use RobustScaler for better outlier resistance
# It uses median and IQR instead of mean and std
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

### 8. Class Distribution (for Classification)
```python
class_counts = pd.Series(y).value_counts().sort_index()
print("Class Distribution:")
for cls, count in class_counts.items():
    pct = 100 * count / len(y)
    print(f"  Class {cls}: {count} ({pct:.1f}%)")
```

## Complete Preprocessing Function

### For Regression:
```python
def preprocess_data(X, y, feature_names):
    """Comprehensive data preprocessing pipeline for regression."""
    from sklearn.preprocessing import RobustScaler
    
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
    
    # 4. Outlier Detection
    print("\n4. Outlier Detection (IQR method):")
    outliers_count = 0
    for col in feature_names:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
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
                high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j]))
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
```

### For Classification:
```python
def preprocess_data(X, y, feature_names):
    """Comprehensive data preprocessing pipeline for classification."""
    from sklearn.preprocessing import RobustScaler
    
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
    
    # 4. Outlier Detection
    print("\n4. Outlier Detection (IQR method):")
    outliers_count = 0
    for col in feature_names:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
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
```

## How to Use

1. **Add the preprocessing function** after the `load_dataset` function
2. **Update imports** to include `RobustScaler`:
   ```python
   from sklearn.preprocessing import StandardScaler, RobustScaler
   ```
3. **Call preprocessing** in the comparison function:
   ```python
   X, y, feature_names = load_dataset(dataset_name)
   X, y, feature_names = preprocess_data(X, y, feature_names)
   ```
4. **Use RobustScaler** instead of StandardScaler:
   ```python
   scaler = RobustScaler()  # Better for outlier resistance
   X_train_scaled = scaler.fit_transform(X_train)
   X_test_scaled = scaler.transform(X_test)
   ```

## Benefits

- **Robustness**: Handles real-world data issues (missing values, outliers)
- **Transparency**: Shows what preprocessing steps were applied
- **Reproducibility**: Consistent preprocessing across all models
- **Educational**: Demonstrates best practices for data preparation

## Notes

- **RobustScaler** is preferred over StandardScaler because it uses median and IQR, making it more resistant to outliers
- **Winsorization** (capping) is preferred over removal to preserve data size
- **Mean imputation** is simple but can be replaced with more sophisticated methods (median, mode, KNN imputation)
- For **multicollinearity**, consider feature selection or dimensionality reduction if many highly correlated features exist

