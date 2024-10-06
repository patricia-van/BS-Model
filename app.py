import streamlit as st
from BSModel import BSModel

# Custom CSS to inject into Streamlit
st.markdown("""
<style>
/* Adjust the size and alignment of the CALL and PUT value containers */
.metric-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px; /* Adjust the padding to control height */
    width: auto; /* Auto width for responsiveness, or set a fixed width if necessary */
    margin: 0 auto; /* Center the container */
}

/* Custom classes for CALL and PUT values */
.metric-call {
    background-color: #90ee90; /* Light green background */
    color: black; /* Black font color */
    margin-right: 10px; /* Spacing between CALL and PUT */
    border-radius: 10px; /* Rounded corners */
}

.metric-put {
    background-color: #ffcccb; /* Light red background */
    color: black; /* Black font color */
    border-radius: 10px; /* Rounded corners */
}

/* Style for the value text */
.metric-value {
    font-size: 1.5rem; /* Adjust font size */
    font-weight: bold;
    margin: 0; /* Remove default margins */
}

/* Style for the label text */
.metric-label {
    font-size: 1rem; /* Adjust font size */
    margin-bottom: 4px; /* Spacing between label and value */
}

</style>
""", unsafe_allow_html=True)

st.title('Black-Scholes Option Pricer')
# st.header('This is a header')
# st.subheader('This is a subheader')
# st.write('Welcome to my Streamlit app!')

st.markdown('### Enter your inputs here!')

current_price = st.number_input('Enter current asset price:', 100)
strike_price = st.number_input('Enter option strike price:', 100)
time_to_maturity = st.number_input('Enter time to maturity (years):', 1)
rf_rate = st.number_input('Enter interest rate:', 0.05)
volatility = st.number_input('Enter asset volatility:', 0.2)

bsm = BSModel(current_price, strike_price, time_to_maturity, rf_rate, volatility)
call_price = bsm.get_call_price()
put_price = bsm.get_put_price()

call_block, put_block = st.columns([1,1], gap='small')

with call_block:
    st.markdown(f"""
        <div class="metric-container metric-call">
            <div>
                <div class="metric-label">CALL Value</div>
                <div class="metric-value">${call_price:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with put_block:
    st.markdown(f"""
        <div class="metric-container metric-put">
            <div>
                <div class="metric-label">PUT Value</div>
                <div class="metric-value">${put_price:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


