import pandas as pd

# 1. Load the Dataset
def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

# 2. Data Cleaning
def clean_data(df):
    """Clean the dataset by handling missing values and data types."""
    df = df.copy()
    # Replace 'NA' with NaN for easier processing
    df.replace('NA', pd.NA, inplace=True)
    # Convert date column to datetime format
    df['last_reported'] = pd.to_datetime(df['last_reported'], format='%b %Y')
    return df

# 3. Descriptive Statistics
def descriptive_statistics(df):
    """Generate descriptive statistics for the dataset."""
    summary_stats = df.describe(include='all')
    return summary_stats

# 4. Data Aggregation by Continent
def aggregate_by_continent(df):
    """Aggregate data by continent."""
    aggregated = df.groupby('who_region').agg({
        'case_total': 'sum',
        'death_total': 'sum',
        'cases_past_month': 'sum',
        'cases_month_before': 'sum'
    }).reset_index()
    return aggregated

# 5. Most Recent Updates
def most_recent_updates(df):
    """Get the most recent updates based on the last reported date."""
    most_recent = df[df['last_reported'] == df['last_reported'].max()]
    return most_recent

# 6. Top 10 Countries by Cases and Deaths
def top_10_countries(df):
    """Get the top 10 countries with the highest total cases and deaths."""
    top_cases = df.nlargest(10, 'case_total')
    top_deaths = df.nlargest(10, 'death_total')
    return top_cases, top_deaths

# 7. Percentage Change Calculation
def calculate_percentage_change(df):
    """Calculate the percentage change in cases."""
    df = df.copy()
    df['perc_change_cases'] = (df['cases_past_month'] - df['cases_month_before']) / df['cases_month_before']
    return df

# 8. Save Results
def save_results(df, output_file):
    """Save the analysis results to a CSV file."""
    df.to_csv(output_file, index=False)

# Main Analysis Workflow
def main():
    # Load the data
    data = load_data('data/mpox_data.csv')
    
    # Clean the data
    data_cleaned = clean_data(data)
    
    # Perform descriptive statistics
    summary_stats = descriptive_statistics(data_cleaned)
    print("Descriptive Statistics:\n", summary_stats)
    
    # Aggregate data by WHO region
    aggregated_data = aggregate_by_continent(data_cleaned)
    print("Aggregated Data by Continent:\n", aggregated_data)
    
    # Get the most recent updates
    recent_updates = most_recent_updates(data_cleaned)
    print("Most Recent Updates:\n", recent_updates[['country', 'case_total', 'death_total', 'last_reported']])
    
    # Get top 10 countries by cases and deaths
    top_cases, top_deaths = top_10_countries(data_cleaned)
    print("Top 10 Countries by Cases:\n", top_cases[['country', 'case_total']])
    print("Top 10 Countries by Deaths:\n", top_deaths[['country', 'death_total']])
    
    # Calculate percentage changes
    data_with_changes = calculate_percentage_change(data_cleaned)
    print("Data with Percentage Changes:\n", data_with_changes[['country', 'perc_change_cases']])
    
    # Save results
    save_results(data_with_changes, 'output/mpox_data_analysis.csv')

if __name__ == "__main__":
    main()