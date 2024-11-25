# U.S. Economic and Financial Dataset

## Dataset Description
This dataset combines historical U.S. economic and financial indicators, spanning the last 50 years, to facilitate time series analysis and uncover patterns in macroeconomic trends. It is designed for exploring relationships between interest rates, inflation, economic growth, stock market performance, and industrial production.

## Key Features
- **Frequency**: Monthly  
- **Time Period**: Last 50 years from Nov-24  
- **Sources**:  
  - Federal Reserve Economic Data (FRED)  
  - Yahoo Finance 

## Dataset Feature Description
1. **Interest Rate** (`Interest_Rate`):  
   - The effective federal funds rate, representing the interest rate at which depository institutions trade federal funds overnight.

2. **Inflation** (`Inflation`):  
   - The Consumer Price Index for All Urban Consumers, an indicator of inflation trends.

3. **GDP** (`GDP`):  
   - Real GDP measures the inflation-adjusted value of goods and services produced in the U.S.

4. **Unemployment Rate** (`Unemployment`):  
   - The percentage of the labor force that is unemployed and actively seeking work.

5. **Stock Market Performance** (`S&P500`):  
   - Monthly average of the adjusted close price, representing stock market trends.

6. **Industrial Production** (`Ind_Prod`):  
   - A measure of real output in the industrial sector, including manufacturing, mining, and utilities.

## Executive Summary
This project explores the interconnected dynamics of key macroeconomic indicators and financial market trends over the past 50 years, leveraging data from the Federal Reserve Economic Data (FRED) and Yahoo Finance. The dataset integrates critical variables such as the Federal Funds Rate, Inflation (CPI), Real GDP, Unemployment Rate, Industrial Production, and the S&P 500 Index, providing a holistic view of the U.S. economy and financial markets.

The analysis focuses on uncovering relationships between these variables through time-series visualization, correlation analysis, and trend decomposition.  Key findings are included in the Insights section. This project serves as a robust resource for understanding long-term economic trends, policy impacts, and market behavior. It is particularly valuable for students, researchers, policymakers, and financial analysts seeking to connect macroeconomic theory with real-world data. 

## Potential Use Cases
- **Economic Analysis**: Examine relationships between interest rates, inflation, GDP, and unemployment.  
- **Stock Market Prediction**: Study how macroeconomic indicators influence stock market trends.  
- **Time Series Modeling**: Perform ARIMA, VAR, or other models to forecast economic trends.  
- **Cyclic Pattern Analysis**: Identify how economic shocks and recoveries impact key indicators.

## Snap of Power Analysis
<img width="468" alt="image" src="https://github.com/user-attachments/assets/1b40e0ca-7d2e-4fbc-8cfd-df3f09e4fdb8">

To ensure sufficient power, the dataset covers last 50 years of monthly data i.e., around 600 entries. 

## Key Insights derived through EDA, time-series visualization, correlation analysis, and trend decomposition. 
- **Interest Rate and Inflation Dynamics**: The interest Rate and inflation exhibit an inverse relationship, especially during periods of aggressive monetary tightening by the Federal Reserve.  
- **Economic Growth and Market Performance**: GDP growth and the S&P 500 Index show a positive correlation, reflecting how market performance often aligns with overall economic health.  
- **Labor Market and Industrial Output**: Unemployment and industrial production demonstrate a strong inverse relationship. Higher industrial output is typically associated with lower unemployment  
- **Market Behavior During Economic Shocks**: The S&P 500 experienced sharp declines during significant crises, such as the 2008 financial crash and the COVID-19 pandemic in 2020. These events also triggered increased unemployment and contractions in GDP, highlighting the interplay between markets and the broader economy.
- **Correlation Highlights**: S&P 500 and GDP have a strong positive correlation. Interest rates negatively correlate with GDP and inflation, reflecting monetary policy impacts.
Unemployment is negatively correlated with industrial production but positively correlated with interest rates.

## Link to Public Dataset
https://www.kaggle.com/datasets/abhishekb7/us-financial-indicators-1974-to-2024/data

## Ethics Statement 
This dataset and its analysis aim to provide insights into macroeconomic and financial trends for educational, research, and analytical purposes while adhering to the highest standards of ethical use and transparency. The data is sourced from reputable and publicly accessible providers, including the Federal Reserve Economic Data (FRED) and Yahoo Finance, ensuring accuracy and reliability without modification. It is intended strictly for educational, analytical, and non-commercial purposes, with no personally identifiable information (PII) included, as it solely represents aggregated macroeconomic indicators and financial trends. All data sources are appropriately credited, and analysis has been clearly documented to ensure transparency and reproducibility. While the dataset offers valuable insights into historical economic and financial trends, it is not a definitive predictor of future outcomes, and users should validate critical decisions with updated values from original sources. 

## Data Limitations
- Missing values in GDP column were forward-filled, which might introduce bias. But GDP is calculated quarterly. 
- S&P 500 data represents the stock market and may not capture broader financial market trends.

