import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Processed Dataset
def load_processed_data(file_path):
    """Load the processed dataset for visualization."""
    return pd.read_csv(file_path)

# 2. Visualize Total Cases by Continent
def visualize_cases_by_continent(df):
    """Visualize total cases by continent."""
    plt.figure(figsize=(10, 6))
    plt.bar(df['who_region'], df['case_total'], color='blue')
    plt.title('Total Cases by Continent')
    plt.xlabel('Continent')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/figures/total_cases_by_continent.png')
    plt.close()

# 3. Visualize Total Deaths by Continent
def visualize_deaths_by_continent(df):
    """Visualize total deaths by continent."""
    plt.figure(figsize=(10, 6))
    plt.bar(df['who_region'], df['death_total'], color='red')
    plt.title('Total Deaths by Continent')
    plt.xlabel('Continent')
    plt.ylabel('Total Deaths')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/figures/total_deaths_by_continent.png')
    plt.close()

# 4. Visualize Most Recent Updates
def visualize_most_recent_updates(df):
    """Visualize the most recent updates in cases and deaths."""
    recent_df = df.sort_values('last_reported', ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    plt.bar(recent_df['country'], recent_df['case_total'], color='green', label='Total Cases')
    plt.bar(recent_df['country'], recent_df['death_total'], color='purple', label='Total Deaths', alpha=0.7)
    plt.title('Most Recent Updates: Cases and Deaths')
    plt.xlabel('Country')
    plt.ylabel('Total')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('output/figures/most_recent_updates.png')
    plt.close()

# 5. Visualize Top 10 Countries
def visualize_top_10_countries(top_cases, top_deaths):
    """Visualize the top 10 countries by cases and deaths."""
    plt.figure(figsize=(10, 6))
    plt.bar(top_cases['country'], top_cases['case_total'], color='blue')
    plt.title('Top 10 Countries by Total Cases')
    plt.xlabel('Country')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('output/figures/top_10_countries_cases.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_deaths['country'], top_deaths['death_total'], color='red')
    plt.title('Top 10 Countries by Total Deaths')
    plt.xlabel('Country')
    plt.ylabel('Total Deaths')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('output/figures/top_10_countries_deaths.png')
    plt.close()

# 6. Visualize Percentage Change in Cases
def visualize_percentage_change(df):
    """Visualize the percentage change in cases."""
    plt.figure(figsize=(10, 6))
    df.sort_values('perc_change_cases', ascending=False, inplace=True)
    plt.bar(df['country'], df['perc_change_cases'], color='orange')
    plt.title('Percentage Change in Cases by Country')
    plt.xlabel('Country')
    plt.ylabel('Percentage Change')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('output/figures/percentage_change_cases_by_country.png')
    plt.close()

# Main Visualization Workflow
def main():
    # Load the processed data
    data = load_processed_data('output/mpox_data_analysis.csv')
    
    # Visualize total cases by continent
    visualize_cases_by_continent(data)
    
    # Visualize total deaths by continent
    visualize_deaths_by_continent(data)
    
    # Visualize most recent updates
    visualize_most_recent_updates(data)
    
    # Load the top 10 data
    top_cases, top_deaths = data.nlargest(10, 'case_total'), data.nlargest(10, 'death_total')
    
    # Visualize top 10 countries by cases and deaths
    visualize_top_10_countries(top_cases, top_deaths)
    
    # Visualize percentage change in cases
    visualize_percentage_change(data)

if __name__ == "__main__":
    main()
