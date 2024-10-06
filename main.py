from shiny import reactive

from shiny.express import input, render, ui

from utilis import fetch_data, total_profit, total_revenue

with ui.card():
    ui.h2("Sales Dashboard"),
    ui.input_select(
        "calculation", "Select calculation:", choices=["Total Profit", "Total Revenue"]
    )
    ui.input_action_button("compute", "Compute!")

with ui.card():
    with ui.h1():
        @render.text
        @reactive.event(input.compute)
        def result():
            if input.calculation() == "Total Profit":
                value = total_profit(fetch_data())
            else:
                value = total_revenue(fetch_data())

            return value