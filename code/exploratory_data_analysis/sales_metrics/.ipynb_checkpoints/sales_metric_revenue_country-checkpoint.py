import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Determine the directory of the current notebook
notebook_dir = os.getcwd()

# Add the parent 'code' directory to sys.path for db_connector.py
code_dir = os.path.abspath(os.path.join(notebook_dir, '../../'))
sys.path.append(code_dir)

# Ensure the credentials file path is set relative to db_connector.py
credentials_file_path = os.path.join(code_dir, "db_credentials.json")

# Verify that the credentials file exists
if not os.path.exists(credentials_file_path):
    raise FileNotFoundError(f"Credentials file not found at {credentials_file_path}. Please ensure it exists.")

# Import the db_connector module
import db_connector

# Override the default path for the credentials file
db_connector.credentials_file = credentials_file_path

# Use get_credentials and connect_to_database
credentials = db_connector.get_credentials()

try:
    engine = db_connector.connect_to_database(credentials)
    print("Connected to the database successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

def fetch_revenue_data(engine):
    """
    Retrieve only the data needed to calculate revenue by country.
    """
    query = """
    SELECT 
        Country, 
        SUM(Quantity * UnitPrice) AS Revenue
    FROM clean_uci_online_retail
    GROUP BY Country
    ORDER BY Revenue DESC;
    """
    data = pd.read_sql(query, con=engine)
    return data

def generate_revenue_plot(data):
    """
    Generate Revenue by Country plot and save to the plots directory using Seaborn.
    """
    # Ensure only the top 10 countries are included
    data = data.head(10)

    # Set Seaborn style without gridlines
    sns.set_theme(style="white")

    # Create the bar plot with updated colors
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x='Country', y='Revenue', data=data, palette="Blues_d", hue=None, legend=False)

    # Customize the plot titles and axis labels
    ax.set_title('Top 10 Countries by Revenue', fontsize=16, fontweight='bold')
    ax.set_xlabel('Country', fontsize=12, fontstyle='italic')
    ax.set_ylabel('Revenue (£)', fontsize=12, fontstyle='italic')

    # Customize the tick labels
    ax.tick_params(axis='x', rotation=45, labelsize=10)

    # Format the y-axis as monetary values with commas and no decimals
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

    # Add data value annotations with commas and no decimal points
    for container in ax.containers:
        ax.bar_label(container, fmt="{:,.0f}", fontsize=9, label_type='edge', padding=2)

    # Save the plot
    plot_path = '../../../plots/revenue_by_country.png'
    plt.tight_layout()
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")

    # Show the plot
    plt.show()

# Main execution
if __name__ == "__main__":
    try:
        # Fetch sales data
        revenue_data = fetch_revenue_data(engine)
        generate_revenue_plot(revenue_data)

    except Exception as e:
        print(f"An error occurred: {e}")