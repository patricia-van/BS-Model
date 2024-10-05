import numpy as np
from scipy.stats import norm

class BSModel:
    def __init__(self, current_price, strike_price, time_to_maturity, interest_rate, volatility) -> None:
        # User-input properties
        self.current_price = current_price
        self.strike_price = strike_price
        self.time_to_maturity = time_to_maturity
        self.interest_rate = interest_rate
        self.volatility = volatility

        # Derived properties
        self.d1 = (np.log(current_price / strike_price) + (interest_rate + 0.5 * volatility**2) * time_to_maturity) / \
                    (volatility * np.sqrt(time_to_maturity))
        self.d2 = self.d1 - (volatility * np.sqrt(time_to_maturity))

    def get_call_price(self):
        return self.current_price * norm.cdf(self.d1) - self.strike_price * np.exp(-self.interest_rate * self.time_to_maturity) * norm.cdf(self.d2)

    def get_put_price(self):
        return self.strike_price * np.exp(-self.interest_rate * self.time_to_maturity) * norm.cdf(-self.d2) - self.current_price * norm.cdf(-self.d1)


