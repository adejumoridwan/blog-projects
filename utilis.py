import pandas as pd

# Business Logic
def fetch_data():
    data = pd.read_csv("supermarket_sales.csv")
    return data

def total_profit(data):
    profit = sum(data["gross income"])
    return profit

def total_revenue(data):
    revenue = sum(data["cogs"])
    return revenue