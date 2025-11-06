# Research Questions, Hypotheses, and Task Completion Status

## Research Questions

1. **Temporal Trends**: Have bird populations (abundance and species richness) changed significantly over the monitoring period (2012-2025)?

2. **Habitat Relationships**: Do different habitat types support different bird communities in terms of species composition, richness, and abundance?

3. **Species-Specific Trends**: Are there significant population trends for individual bird species, and which species are declining or increasing?

4. **Spatial Patterns**: Are there spatial patterns in bird diversity across the island, and do certain transects or regions show higher biodiversity?

5. **Observer and Detection Effects**: Do observer characteristics or detection methods (visual vs. audio) significantly affect detection rates and abundance estimates?

## Hypotheses

### H1: Temporal Trends in Species Richness
- **H₀**: There is no significant change in species richness over time (2012-2025)
- **H₁**: Species richness has changed significantly over the monitoring period
- **Test**: Linear regression with year as predictor, t-test on slope coefficient

### H2: Temporal Trends in Total Abundance
- **H₀**: There is no significant change in total bird abundance over time (2012-2025)
- **H₁**: Total bird abundance has changed significantly over the monitoring period
- **Test**: Linear regression with year as predictor, t-test on slope coefficient

### H3: Habitat Effects on Species Richness
- **H₀**: Species richness does not differ significantly between habitat types
- **H₁**: Species richness differs significantly between at least two habitat types
- **Test**: ANOVA or Kruskal-Wallis test (if assumptions not met)

### H4: Habitat Effects on Abundance
- **H₀**: Bird abundance does not differ significantly between habitat types
- **H₁**: Bird abundance differs significantly between at least two habitat types
- **Test**: ANOVA or Kruskal-Wallis test (if assumptions not met)

### H5: Species-Specific Population Trends
- **H₀**: For each species, there is no significant temporal trend in abundance
- **H₁**: For some species, there are significant temporal trends (increasing or decreasing)
- **Test**: Linear regression for each species with sufficient data, multiple testing correction (Bonferroni or FDR)

### H6: Observer Effects on Detection
- **H₀**: Observer identity does not significantly affect detection rates
- **H₁**: Observer identity significantly affects detection rates
- **Test**: Mixed-effects model or ANOVA with observer as random/fixed effect

### H7: Detection Modality Effects
- **H₀**: Detection rates do not differ significantly between visual and audio detection methods
- **H₁**: Detection rates differ significantly between visual and audio methods
- **Test**: Chi-square test or logistic regression

### H8: Spatial Patterns in Biodiversity
- **H₀**: Species richness and abundance are uniformly distributed across transects
- **H₁**: There are significant spatial patterns in species richness and abundance
- **Test**: Spatial autocorrelation analysis, clustering analysis

## Critical Actions Required

### 1. DATA MERGING (HIGHEST PRIORITY)

**Current Status**: Sheets are loaded but NOT merged

**Required Steps**:
1. Examine actual column structure in all three sheets
2. Identify correct merge keys:
   - For ESPECES: Match `ESPECE` column in observations with species names in ESPECES
   - For GPS-MILIEU: Match `Nom transect` and `N° point` in observations with corresponding columns in GPS-MILIEU
3. Restructure ESPECES sheet if needed (it appears to have non-standard format)
4. Implement merge code
5. Validate merged dataset

**Impact**: Without merging, habitat analysis, species taxonomy analysis, and many EDA components cannot be completed.

### 2. COMPLETE EDA (HIGH PRIORITY)

**Current Status**: Framework exists but incomplete due to missing merged data

**Missing Components**:
- Species richness by habitat (needs GPS-MILIEU merge)
- Rare/endemic species identification (needs ESPECES merge)
- Habitat type analysis (needs GPS-MILIEU merge)
- Geographic patterns (needs GPS coordinates)
- Complete observer bias assessment
- Complete detection modality analysis

### 3. EXECUTE STATISTICAL TESTS (HIGH PRIORITY)

**Current Status**: Framework exists but tests not executed

**Required**:
- Execute all hypothesis tests (H1-H8)
- Report p-values, effect sizes, confidence intervals
- Apply multiple testing correction where needed
- Validate model assumptions

### 4. MODEL VALIDATION (MEDIUM PRIORITY)

**Current Status**: Models fitted but not validated

**Required**:
- Check normality assumptions
- Check homoscedasticity
- Check independence
- Residual analysis
- Model diagnostics

### 5. REPORTING (MEDIUM PRIORITY)

**Current Status**: Basic summary only

**Required**:
- Comprehensive written report
- Interpretation of all results
- Discussion of limitations
- Conservation implications
- Recommendations

## Next Steps Checklist

- [ ] **IMMEDIATE**: Fix data merging - examine column structures and implement proper merge
- [ ] **IMMEDIATE**: Run complete EDA on merged dataset
- [ ] **HIGH PRIORITY**: Execute all statistical hypothesis tests (H1-H8)
- [ ] **HIGH PRIORITY**: Validate all model assumptions
- [ ] **MEDIUM PRIORITY**: Complete reporting with full interpretation

## Notes

- Hypotheses have been added to the notebook (before Task 3)
- Task status report created: `TASK_STATUS_REPORT.md`
- Data merging code needs to be implemented based on actual column structure
- All analyses require the merged dataset to be complete

