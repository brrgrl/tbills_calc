import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Investment Return Comparison: Rolling 4-Week Treasury Bills vs Savings Account')

# Input fields
initial_investment = st.number_input('Initial Investment Amount ($)', value=1000.0, min_value=0.0, step=100.0)
t_bill_annual_rate = st.number_input('Annual Treasury Bill Rate (%)', value=3.0, min_value=0.0, step=0.1)
savings_annual_rate = st.number_input('Annual Savings Account Rate (%)', value=1.0, min_value=0.0, step=0.1)
investment_period_years = st.number_input('Investment Period (Years)', value=1.0, min_value=0.0, step=0.1)

# Convert annual rates from percentage to decimal
t_bill_annual_rate /= 100
savings_annual_rate /= 100

# Convert annual rates to weekly rates (assuming 52 weeks in a year)
weeks_in_year = 52
t_bill_weekly_rate = (1 + t_bill_annual_rate) ** (1 / weeks_in_year) - 1
savings_weekly_rate = (1 + savings_annual_rate) ** (1 / weeks_in_year) - 1

# Calculate the number of weeks in the investment period
investment_period_weeks = int(investment_period_years * weeks_in_year)

# Calculate returns for rolling 4-week Treasury Bills
t_bill_value = initial_investment
t_bill_values = [t_bill_value]
for week in range(1, investment_period_weeks + 1):
    if week % 4 == 0:  # Assume T-bills are reinvested every 4 weeks
        t_bill_value *= (1 + t_bill_weekly_rate * 4)
    t_bill_values.append(t_bill_value)

# Calculate returns for Savings Account (compounded weekly)
savings_value = initial_investment * (1 + savings_weekly_rate) ** investment_period_weeks
savings_values = [initial_investment * (1 + savings_weekly_rate) ** week for week in range(investment_period_weeks + 1)]

# Display the results
st.subheader('Results')
st.write(f'Initial Investment: ${initial_investment:,.2f}')
st.write(f'Treasury Bill Return after {investment_period_years} years: ${t_bill_value:,.2f}')
st.write(f'Savings Account Return after {investment_period_years} years: ${savings_value:,.2f}')

# Plotting the results
weeks = np.arange(0, investment_period_weeks + 1, 1)

plt.figure(figsize=(10, 6))
plt.plot(weeks, t_bill_values, label='Rolling 4-Week Treasury Bills', marker='o')
plt.plot(weeks, savings_values, label='Savings Account', marker='o')
plt.xlabel('Weeks')
plt.ylabel('Value ($)')
plt.title('Investment Value Over Time')
plt.legend()
plt.grid(True)

st.pyplot(plt)
