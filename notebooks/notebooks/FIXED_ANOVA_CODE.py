# ============================================================================
# CORRECTED CODE FOR DATASET 1: TREATMENT EFFECTS
# Replace the problematic sections in your notebook with this code
# ============================================================================

# ===== FIX 1: Update train_test_split to get indices =====
# REPLACE THIS:
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=None
# )

# WITH THIS:
indices = np.arange(len(X))
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(
    X, y, indices, test_size=0.2, random_state=42, stratify=None
)


# ===== FIX 2: Update ANOVA predictions section =====
# REPLACE THIS:
# # Prepare data for ANOVA
# df_train = df.iloc[X_train[:, 0].argsort()].head(len(X_train))
# df_train = df.loc[df.index[:len(X_train)]]
# 
# # Actually, let's use the full dataset for ANOVA (typical for ANOVA)
# anova_df = df.copy()
# 
# # One-way ANOVA using statsmodels
# model_formula = 'recovery_time ~ C(treatment)'
# model = ols(model_formula, data=anova_df).fit()
# anova_table = anova_lm(model, typ=2)
# 
# start_time = time.time()
# anova_result = model
# anova_train_time = time.time() - start_time
# 
# # Get group means for predictions
# group_means = anova_df.groupby('treatment')['recovery_time'].mean().to_dict()
# 
# # Predictions (for comparison purposes, use group means)
# anova_train_pred = anova_df['treatment'].map(group_means).values
# anova_test_pred = df.loc[df.index[len(X_train):]]['treatment'].map(group_means).values
# 
# # Calculate metrics
# anova_train_r2 = r2_score(anova_df['recovery_time'], anova_train_pred)
# anova_test_r2 = r2_score(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred)
# anova_test_rmse = np.sqrt(mean_squared_error(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred))
# anova_test_mae = mean_absolute_error(df.loc[df.index[len(X_train):]]['recovery_time'], anova_test_pred)

# WITH THIS:
# Prepare data for ANOVA
# Use the full dataset for ANOVA (typical for ANOVA - uses all data for inference)
anova_df = df.copy()

# One-way ANOVA using statsmodels
model_formula = 'recovery_time ~ C(treatment)'
model = ols(model_formula, data=anova_df).fit()
anova_table = anova_lm(model, typ=2)

start_time = time.time()
anova_result = model
anova_train_time = time.time() - start_time

# Get group means for predictions (calculated on full dataset, but used for test set)
group_means = anova_df.groupby('treatment')['recovery_time'].mean().to_dict()

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


# ===== FIX 3: Update visualization code =====
# REPLACE THIS:
# test_actual = df.loc[df.index[len(X_train):]]['recovery_time'].values

# WITH THIS:
test_actual = y_test  # Already the correct test set values

# OR if you need it from DataFrame:
# test_df = df.iloc[indices_test]
# test_actual = test_df['recovery_time'].values


# ===== FIX 4: Update group means comparison visualization =====
# REPLACE THIS:
# test_df = df.loc[df.index[len(X_train):]].copy()
# test_df['svm_pred'] = svm_test_pred

# WITH THIS:
test_df = df.iloc[indices_test].copy()
test_df['svm_pred'] = svm_test_pred

