from utilis import fetch_data, total_profit, total_revenue
import pandas as pd

# Business Logic
data = fetch_data()


def test_total_profit():
    assert total_profit(data) == 15379.369


def test_total_revenue():
    assert total_revenue(data) == 307587.38
