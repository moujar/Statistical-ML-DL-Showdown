# Fix for the NameError: name 'species_col' is not defined
# 
# The problem: species_col is defined inside an if block but used later outside that block
# Solution: Define species_col at the beginning of the cell

# REPLACE THE BEGINNING OF YOUR CELL WITH THIS:

# Species richness and distribution
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Identify species column - define at the beginning so it's available throughout
species_col = None
if 'species_code' in observations_df.columns:
    species_col = 'species_code'
elif 'species_name' in observations_df.columns:
    species_col = 'species_name'
elif 'ESPECE' in observations_df.columns:
    species_col = 'ESPECE'
else:
    # Try to find any column that might contain species names
    potential_cols = [col for col in observations_df.columns if 'espece' in col.lower() or 'species' in col.lower()]
    if potential_cols:
        species_col = potential_cols[0]
        print(f"Using column '{species_col}' for species identification")

if species_col is None:
    print("Warning: Could not find species column. Please check column names.")
    print(f"Available columns: {list(observations_df.columns)}")
else:
    # 1. Most common species (by observation count)
    species_counts = observations_df[species_col].value_counts().head(20)
    
    axes[0, 0].barh(range(len(species_counts)), species_counts.values)
    axes[0, 0].set_yticks(range(len(species_counts)))
    axes[0, 0].set_yticklabels(species_counts.index)
    axes[0, 0].set_xlabel('Number of Observations')
    axes[0, 0].set_title('Top 20 Most Frequently Observed Species')
    axes[0, 0].invert_yaxis()
    axes[0, 0].grid(axis='x', alpha=0.3)

    # 2. Most abundant species (by individual count)
    if 'individual_count' in observations_df.columns:
        species_abundance = observations_df.groupby(species_col)['individual_count'].sum().sort_values(ascending=False).head(20)
        
        axes[0, 1].barh(range(len(species_abundance)), species_abundance.values)
        axes[0, 1].set_yticks(range(len(species_abundance)))
        axes[0, 1].set_yticklabels(species_abundance.index)
        axes[0, 1].set_xlabel('Total Individuals')
        axes[0, 1].set_title('Top 20 Most Abundant Species')
        axes[0, 1].invert_yaxis()
        axes[0, 1].grid(axis='x', alpha=0.3)
    else:
        axes[0, 1].text(0.5, 0.5, 'Individual count data not available', 
                        ha='center', va='center', transform=axes[0, 1].transAxes)
        axes[0, 1].set_title('Abundance Analysis')

    # 3. Species richness by transect
    # Check for transect column - try different possible names
    transect_col = None
    if 'transect_id' in observations_df.columns:
        transect_col = 'transect_id'
    elif 'Nom transect' in observations_df.columns:
        transect_col = 'Nom transect'
    else:
        potential_cols = [col for col in observations_df.columns if 'transect' in col.lower()]
        if potential_cols:
            transect_col = potential_cols[0]
    
    if transect_col:
        richness_by_transect = observations_df.groupby(transect_col)[species_col].nunique().sort_values(ascending=False)
        
        axes[1, 0].bar(range(len(richness_by_transect)), richness_by_transect.values)
        axes[1, 0].set_xlabel('Transect ID')
        axes[1, 0].set_ylabel('Species Richness')
        axes[1, 0].set_title('Species Richness by Transect')
        axes[1, 0].grid(axis='y', alpha=0.3)
        
        print(f"Mean species richness per transect: {richness_by_transect.mean():.2f}")
        print(f"Median species richness per transect: {richness_by_transect.median():.2f}")
    else:
        axes[1, 0].text(0.5, 0.5, 'Transect data not available', 
                        ha='center', va='center', transform=axes[1, 0].transAxes)
        axes[1, 0].set_title('Species Richness by Transect')

    # 4. Species observation frequency distribution
    obs_per_species = observations_df[species_col].value_counts()
    axes[1, 1].hist(obs_per_species.values, bins=50, edgecolor='black', alpha=0.7)
    axes[1, 1].set_xlabel('Number of Observations')
    axes[1, 1].set_ylabel('Number of Species')
    axes[1, 1].set_title('Distribution of Observation Frequency per Species')
    axes[1, 1].set_yscale('log')
    axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

