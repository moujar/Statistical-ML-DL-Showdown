# Fixed Code for ANOVA Predictions

Replace the problematic section in your notebook with this corrected code:

## 1. Fix the train_test_split to get indices:

```python
# Split data - get indices to properly map back to DataFrame
indices = np.arange(len(X))
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(
    X, y, indices, test_size=0.2, random_state=42, stratify=None
)
```

## 2. Fix the ANOVA predictions section:

Replace this:
```python
# Predictions (for comparison purposes, use group means)
anova_train_pred = anova_df['treatment'].map(group_means).values
anova_test_pred = df.loc[df.index[len(X_train):]]['treatment'].map(group_means).values

# Calculate metrics
anova_train_r2 = r2_score(anova_df['recovery_time'], anova_train_pred)
anova_test_r2 = r2_score(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred)
anova_test_rmse = np.sqrt(mean_squared_error(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred))
anova_test_mae = mean_absolute_error(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred)
```

With this:
```python
# Predictions: use group means for test set
# Get test set treatments from DataFrame using indices_test
test_df = df.iloc[indices_test]
anova_test_pred = test_df['treatment'].map(group_means).values

# Actual test values (already correctly split as y_test)
test_actual = y_test

# Calculate metrics on test set
anova_test_r2 = r2_score(test_actual, anova_test_pred)
anova_test_rmse = np.sqrt(mean_squared_error(test_actual, anova_test_pred))
anova_test_mae = mean_absolute_error(test_actual, anova_test_pred)
```

## 3. Fix the visualization code:

Replace this:
```python
test_actual = df.loc[df.index[len(X_train):]]['recovery_time'].values
```

With this:
```python
test_actual = y_test  # Already the correct test set values
```

Or if you need it from DataFrame:
```python
test_df = df.iloc[indices_test]
test_actual = test_df['recovery_time'].values
```

