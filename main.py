import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred
import yfinance as yf
from statsmodels.tsa.seasonal import seasonal_decompose
import datetime

# Initialize FRED API
FRED_API_KEY = '3d94de4cccd00a08f2a139dc5d021664'
fred = Fred(api_key=FRED_API_KEY)


def fetch_data(start_date, end_date):
    """Fetch data from FRED and Yahoo Finance"""
    interest_rate = fred.get_series('FEDFUNDS', observation_start=start_date, observation_end=end_date)
    inflation = fred.get_series('CPIAUCSL')
    gdp = fred.get_series('GDPC1')
    unemployment = fred.get_series('UNRATE')
    ind_prod = fred.get_series('INDPRO', observation_start=start_date, observation_end=end_date)
    sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Adj Close']
    
    return interest_rate, inflation, gdp, unemployment, ind_prod, sp500


def preprocess_data(interest_rate, inflation, gdp, unemployment, ind_prod, sp500):
    """Preprocess data for analysis"""
    data = pd.DataFrame({
        'Interest_Rate': interest_rate,
        'Inflation': inflation,
        'GDP': gdp,
        'Unemployment': unemployment,
        'Ind_Prod': ind_prod
    })
    data['GDP'] = data['GDP'].fillna(method='ffill')
    
    df = pd.DataFrame(sp500)
    monthly_avg = df.resample('M').mean()
    monthly_avg.index = monthly_avg.index.to_period('M').to_timestamp()
    monthly_avg.reset_index(inplace=True)
    monthly_avg.rename(columns={'^GSPC': 'sp500'}, inplace=True)
    monthly_avg.set_index('Date', inplace=True)
    
    merged_df = pd.merge(data, monthly_avg, left_index=True, right_index=True)
    return merged_df


def plot_correlation_matrix(merged_df):
    """Plot the correlation matrix"""
    plt.figure(figsize=(10, 6))
    sns.heatmap(merged_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Variables')
    plt.show()


def plot_dual_axes(merged_df, col1, col2, col1_label, col2_label, title, col1_color, col2_color):
    """Plot two variables on dual y-axes"""
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(merged_df.index, merged_df[col1], label=col1_label, color=col1_color)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(col1_label, color=col1_color)
    ax1.tick_params(axis='y', labelcolor=col1_color)
    ax2 = ax1.twinx()
    ax2.plot(merged_df.index, merged_df[col2], label=col2_label, color=col2_color)
    ax2.set_ylabel(col2_label, color=col2_color)
    ax2.tick_params(axis='y', labelcolor=col2_color)
    fig.suptitle(title)
    ax1.grid()
    plt.show()


def seasonal_decompose_variable(data, column_name, model='multiplicative', period=12):
    """Perform seasonal decomposition on a given variable"""
    result = seasonal_decompose(data[column_name], model=model, period=period)
    result.plot()
    plt.suptitle(f'Decomposition of {column_name}', fontsize=16, y=0.95)
    plt.tight_layout()
    plt.show()


def main():
    """Main function to execute the analysis"""
    # Fetch data
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=50 * 365)
    interest_rate, inflation, gdp, unemployment, ind_prod, sp500 = fetch_data(start_date, end_date)

    # Preprocess data
    merged_df = preprocess_data(interest_rate, inflation, gdp, unemployment, ind_prod, sp500)

    # Plot correlation matrix
    plot_correlation_matrix(merged_df)

    # Visualizations
    plot_dual_axes(
        merged_df, 'Interest_Rate', 'sp500', 
        'Interest Rate', 'S&P 500', 
        'Interest Rate vs S&P 500', 'blue', 'red'
    )
    plot_dual_axes(
        merged_df, 'Interest_Rate', 'GDP', 
        'Interest Rate', 'GDP', 
        'Interest Rate vs GDP', 'blue', 'green'
    )
    plot_dual_axes(
        merged_df, 'Interest_Rate', 'Unemployment', 
        'Interest Rate', 'Unemployment', 
        'Interest Rate vs Unemployment', 'blue', 'orange'
    )
    plot_dual_axes(
        merged_df, 'Ind_Prod', 'Unemployment', 
        'Industrial Production', 'Unemployment', 
        'Industrial Production vs Unemployment', 'purple', 'orange'
    )
    plot_dual_axes(
        merged_df, 'sp500', 'GDP', 
        'S&P 500', 'GDP', 
        'S&P 500 vs GDP', 'red', 'green'
    )

    # Seasonal decomposition
    seasonal_decompose_variable(merged_df, 'GDP')
    seasonal_decompose_variable(merged_df, 'Ind_Prod')


if __name__ == "__main__":
    main()
