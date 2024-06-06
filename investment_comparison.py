import streamlit as st
import numpy as np

st.title('Investment Return Comparison: Treasury Bills vs Savings Account')

# Input fields
initial_investment = st.number_input('Initial Investment Amount ($)', value=1000.0, min_value=0.0, step=100.0)
t_bill_rate = st.number_input('Annual Treasury Bill Rate (%)', value=3.0, min_value=0.0, step=0.1)
savings_rate = st.number_input('Annual Savings Account Rate (%)', value=1.0, min_value=0.0, step=0.1)
investment_period = st.number_input('Investment Period (Years)', value=1.0, min_value=0.0, step=0.1)

# Convert rates from percentage to decimal
t_bill_rate /= 100
savings_rate /= 100

# Calculate returns for Treasury Bills (assuming simple interest for simplicity)
# Rolling T-bills are assumed to be reinvested every year at the same rate
t_bill_return = initial_investment * (1 + t_bill_rate) ** investment_period

# Calculate returns for Savings Account (assuming simple interest for simplicity)
savings_return = initial_investment * (1 + savings_rate) ** investment_period

# Display the results
st.subheader('Results')
st.write(f'Initial Investment: ${initial_investment:,.2f}')
st.write(f'Treasury Bill Return after {investment_period} years: ${t_bill_return:,.2f}')
st.write(f'Savings Account Return after {investment_period} years: ${savings_return:,.2f}')

# Plotting the results
import matplotlib.pyplot as plt

years = np.arange(0, investment_period + 1, 1)
t_bill_values = initial_investment * (1 + t_bill_rate) ** years
savings_values = initial_investment * (1 + savings_rate) ** years

plt.figure(figsize=(10, 6))
plt.plot(years, t_bill_values, label='Treasury Bills', marker='o')
plt.plot(years, savings_values, label='Savings Account', marker='o')
plt.xlabel('Years')
plt.ylabel('Value ($)')
plt.title('Investment Value Over Time')
plt.legend()
plt.grid(True)

st.pyplot(plt)
