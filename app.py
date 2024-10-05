import streamlit as st
from BSModel import BSModel

st.title('Black-Scholes Option Pricer')
st.write('Welcome to my Streamlit app!')

current_price = st.number_input('Enter current asset price:', 100)
strike_price = st.number_input('Enter option strike price:', 100)
time_to_maturity = st.number_input('Enter time to maturity (years):', 1)
rf_rate = st.number_input('Enter interest rate:', 0.05)
volatility = st.number_input('Enter asset volatility:', 0.2)

bsm = BSModel(current_price, strike_price, time_to_maturity, rf_rate, volatility)
call_price = bsm.get_call_price()
put_price = bsm.get_put_price()

st.write('Your call price is ', round(call_price, 2))
st.write('Your put price is ', round(put_price, 2))