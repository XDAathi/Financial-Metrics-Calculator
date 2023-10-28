import datetime
import yfinance as yf

stock = input("Ticker Symbol:\n")
ticker = yf.Ticker(stock)
startDate = datetime.datetime(2022, 1, 1)
endDate = datetime.datetime(2022, 12, 31)


def CurrentRatio():
    try:
        if 1>0:
            currentRatio = ticker.info["currentRatio"]
            print("Current Ratio: " + str(currentRatio))
        else:
            print("cannot find current ratio")
    except KeyError:
        print("Balance sheet data not available for this stock.")

def QuickRatio():
    quickRatio = ticker.info["quickRatio"]
    print("Quick Ratio: " + str(quickRatio))


def debtEquityRatio():
    debteqratio = ticker.info["debtToEquity"]
    print("Debt to equity: " + str(debteqratio))


def daysSalesOutstanding():
    try:
        balance_sheet = ticker.get_balance_sheet()
        income_statement = ticker.get_income_stmt()
        if 1 > 0:
            accounts_receivable = balance_sheet.loc["GrossAccountsReceivable"]
            total_revenue = income_statement.loc["TotalRevenue"]
            dso = (accounts_receivable.iloc[0] / (
                        total_revenue.iloc[0] + 1e-10)) * 365  # Adding a small value to avoid division by zero
            print("Days Sales Outstanding (DSO): " + str(dso))
        else:
            print("Data required for DSO calculation is not available.")
    except KeyError:
        print("DSO calculation error do manually")


def inventoryTurnOver():
    try:
        balance_sheet = ticker.get_balance_sheet()
        income_statement = ticker.get_income_stmt()
        if 1 > 0:
            total_sales = income_statement.loc["CostOfRevenue"]
            inventory = balance_sheet.loc["Inventory"]
            turnover = (total_sales.iloc[0] / inventory.iloc[0])
            print("Inventory Turnover: " + str(turnover))
        else:
            print("Data required for inventory Turnover calculation is not available.")
    except KeyError:
        print("Balance sheet data not available for this stock.")


def apSales():
    try:
        balance_sheet = ticker.get_balance_sheet()
        income_statement = ticker.get_income_stmt()
        if 1 > 0:
            accounts_payable = balance_sheet.loc["AccountsPayable"]
            revenue = income_statement.loc["TotalRevenue"]
            turnover = (accounts_payable.iloc[0] / revenue.iloc[0]) * 100
            print("Accounts Payable to Sales: " + str(turnover))
        else:
            print("Data required for Accounts Payable Sales calculation is not available.")
    except KeyError:
        print("Balance sheet data not available for this stock.")


def returnOnSales():
    try:
        income_statement = ticker.get_income_stmt()
        if 1 > 0:
            netIncome =income_statement.loc["NetIncome"]
            revenue = income_statement.loc["TotalRevenue"]
            turnover = (netIncome.iloc[0] / revenue.iloc[0]) * 100
            print("Return on Sales: " + str(turnover))
        else:
            print("Data required for Return on Sales calculation is not available.")
    except KeyError:
        print("Balance sheet data not available for this stock.")


def returnOnAssets():
    ROA = ticker.info["returnOnAssets"]
    print("Return On Assets: " + str(ROA*100))


def returnOnEquity():
    ROE = ticker.info["returnOnEquity"]
    print("Return On Equity: " + str(ROE*100))


def EPS():
    eps = ticker.info["trailingEps"]
    print("Earnings Per share trailing 12 months: " + str(eps))

def PE():
    stockPrice = ticker.info["currentPrice"]
    eps = ticker.info["trailingEps"]
    pe = stockPrice/eps
    print("P/E ratio: " + str(pe))





CurrentRatio()
QuickRatio()
debtEquityRatio()
daysSalesOutstanding()
inventoryTurnOver()
apSales()
returnOnSales()
returnOnAssets()
returnOnEquity()
EPS()
PE()

