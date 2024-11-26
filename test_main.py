import warnings
warnings.filterwarnings("ignore")


import unittest
from main import fetch_data, preprocess_data, plot_correlation_matrix, plot_dual_axes, seasonal_decompose_variable
import datetime
import pandas as pd
import matplotlib.pyplot as plt


class Test(unittest.TestCase):

    def setUp(self):
        """Set up test environment with sample data."""
        self.end_date = datetime.datetime.today()
        self.start_date = self.end_date - datetime.timedelta(days=50 * 365)
        self.interest_rate, self.inflation, self.gdp, self.unemployment, self.ind_prod, self.sp500 = fetch_data(
            self.start_date, self.end_date
        )
        self.merged_df = preprocess_data(
            self.interest_rate, self.inflation, self.gdp, self.unemployment, self.ind_prod, self.sp500
        )

    def test_fetch_data(self):
        """Test that data is fetched successfully."""
        self.assertFalse(self.interest_rate.empty, "Interest rate data is empty")
        self.assertFalse(self.inflation.empty, "Inflation data is empty")
        self.assertFalse(self.gdp.empty, "GDP data is empty")
        self.assertFalse(self.unemployment.empty, "Unemployment data is empty")
        self.assertFalse(self.ind_prod.empty, "Industrial production data is empty")
        self.assertFalse(self.sp500.empty, "S&P 500 data is empty")

    def test_preprocess_data(self):
        """Test that preprocessing works and data is correctly merged."""
        self.assertIn('Interest_Rate', self.merged_df.columns, "Interest_Rate column missing in processed data")
        self.assertIn('sp500', self.merged_df.columns, "sp500 column missing in processed data")
        self.assertGreater(len(self.merged_df), 0, "Merged DataFrame is empty")

    def test_plot_correlation_matrix(self):
        """Test that the correlation matrix plot is generated without errors."""
        try:
            plot_correlation_matrix(self.merged_df)
            plt.close('all')  # Close plot to prevent resource leakage during testing
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

    def test_plot_dual_axes(self):
        """Test that dual-axis plots are generated without errors."""
        try:
            plot_dual_axes(
                self.merged_df, 'Interest_Rate', 'sp500',
                'Interest Rate', 'S&P 500',
                'Interest Rate vs S&P 500', 'blue', 'red'
            )
            plt.close('all')
        except Exception as e:
            self.fail(f"plot_dual_axes raised an exception: {e}")

    def test_seasonal_decompose_variable(self):
        """Test that seasonal decomposition works for a variable."""
        try:
            seasonal_decompose_variable(self.merged_df, 'GDP')
            plt.close('all')
        except Exception as e:
            self.fail(f"seasonal_decompose_variable raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
