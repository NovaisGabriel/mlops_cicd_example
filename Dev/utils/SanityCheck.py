import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SanityCheck:
    def __init__(self, df):
        self.df = df.copy()
    
    def missing_values_summary(self):
        """
        Returns a DataFrame with the count and percentage of missing (NaN/inf) values per column.
        """
        total = self.df.isnull().sum() + self.df.isin([np.inf, -np.inf]).sum()
        percent = 100 * total / len(self.df)
        summary = pd.DataFrame({
            'MissingCount': total,
            'MissingPercent': percent
        })
        return summary[summary.MissingCount > 0].sort_values(by='MissingPercent', ascending=False)
    
    def column_distribution_summary(self):
        """
        Returns descriptive statistics for each column in the DataFrame.
        """
        return self.df.describe(include='all').transpose()
    
    def column_value_counts(self, column, top_n=10):
        """
        Returns the top N most frequent values for a given column.
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        return self.df[column].value_counts(dropna=False).head(top_n)
    
    def plot_distribution(self, column, bins=30):
        """
        Plots a histogram for numerical columns or bar chart for categorical columns.
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")

        plt.figure(figsize=(8, 4))
        if pd.api.types.is_numeric_dtype(self.df[column]):
            sns.histplot(self.df[column].replace([np.inf, -np.inf], np.nan).dropna(), bins=bins, kde=True)
            plt.title(f'Distribution of {column}')
        else:
            counts = self.df[column].value_counts().head(10)
            sns.barplot(x=counts.values, y=counts.index)
            plt.title(f'Top 10 Categories in {column}')
        plt.tight_layout()
        plt.show()