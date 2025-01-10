# Financial Metrics Calculator

# Overview

The Financial Metrics Calculator is a Python-based tool that allows users to calculate and analyze key financial ratios and metrics for a given stock ticker symbol. The tool leverages the Yahoo Finance API to fetch real-time and historical financial data.

# Features

Current Ratio: Measures a company's ability to pay short-term obligations.

Quick Ratio: Evaluates liquidity by excluding inventory from current assets.

Debt-to-Equity Ratio: Assesses the level of a company's financial leverage.

Days Sales Outstanding (DSO): Calculates the average number of days a company takes to collect revenue after a sale.

Inventory Turnover: Shows how efficiently inventory is managed.

Accounts Payable to Sales Ratio: Measures the proportion of sales used to settle accounts payable.

Return on Sales (ROS): Indicates profitability by dividing net income by revenue.

Return on Assets (ROA): Evaluates how efficiently assets generate profit.

Return on Equity (ROE): Assesses the profitability relative to shareholders' equity.

Earnings Per Share (EPS): Calculates the net income per outstanding share of stock.

Price-to-Earnings (P/E) Ratio: Determines stock valuation by comparing its price to its earnings per share.

# Installation

Ensure Python 3.7 or later is installed.

Install the required library:

pip install yfinance

# Usage

Run the script:

python financial_metrics_calculator.py

Enter the ticker symbol of the stock when prompted (e.g., AAPL for Apple).

View the calculated financial metrics in the terminal.

# Code Breakdown

Data Retrieval: The script uses the Yahoo Finance API via the yfinance library to fetch stock data.

Financial Metric Functions: Each financial metric is implemented as a dedicated function for modularity and readability.

Error Handling: The script includes error handling for missing or unavailable data.

Example Output

For the ticker symbol AAPL:

Ticker Symbol:
AAPL
Current Ratio: 1.07
Quick Ratio: 0.85
Debt to Equity: 1.68
Days Sales Outstanding (DSO): 45.12
Inventory Turnover: 3.5
Accounts Payable to Sales: 15.2
Return on Sales: 22.3
Return On Assets: 18.5
Return On Equity: 36.2
Earnings Per Share trailing 12 months: 5.61
P/E ratio: 28.4

# Limitations

The tool depends on the availability of data from Yahoo Finance. Missing or incomplete data may cause some metrics to be unavailable.

Certain calculations (e.g., DSO, Inventory Turnover) assume specific data formats and may fail for some stocks.

# Future Enhancements

Add a graphical user interface (GUI) for easier interaction.

Support for exporting results to a CSV or PDF file.

Additional financial metrics and charts for visualization.

# License

This project is licensed under the MIT License. See the LICENSE file for more information.

Note: Always ensure that financial data is accurate and consult a financial advisor for investment decisions.
