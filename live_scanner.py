#--- Live Market Scanner ---#
# Goal: Download real S&P 500 data and calculate the EMA 20 automatically

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

print("Connecting to live market data...")


# 1. Download Real Data (The ticker for SP500 is '^GSPC')
# We request 6 months of daily data.

sp500 = yf.download("^GSPC", period="6mo", interval="1d")

# 2. Clean the DataFrame
# We only want the "Close" price column to keep it simple

df = sp500[["Close"]].copy()

# Rename the column for better readability

df.columns = ["Close_Price"]

# 3. Calculate the EMA 20 dynamically!
# Pandas uses "ewm" (Exponential Weighted functions) to calculate moving averages instantly

df["EMA_20"] = df["Close_Price"].ewm(span=20, adjust=False).mean()


print("\n--- Last 5 days of the S&P 500 ---")
# The .tail() function shows only the bottom rows of a massive table


# --- YOUR CHALLENGE 10 ---
# 1. Apply the vectorization logic you learned in the previous phase.
# 2. Create the "Buy_Signal" column (True if Close_Price >= EMA_20).
# 3. Create the "Sell_Signal" column (True if Close_Price < EMA_20).
# 4. Change the print statement at the end to show the last 10 days instead of 5: print(df.tail(10))

df["Buy_Signal"] = df["Close_Price"] >= df["EMA_20"]

df["Sell_Signal"] = df["Close_Price"] < df["EMA_20"]


print(df.tail(10))

# Challenge 11 Data Visualization

print("\n Generating strategy chart...")

# Defining chart's size

plt.figure(figsize=(12,6))

# Plot the lines

plt.plot(df["Close_Price"], label="Close Price", color="blue", marker="o")
plt.plot(df["EMA_20"], label="EMA 20", color="red", linestyle="--")

plt.title("S&P 500: EMA 20 Crossover Strategy")
plt.xlabel("Trading Days")
plt.ylabel("Price (USD)")
plt.legend() # This shows the labels box in the corner
plt.grid(True) # Adds a background grid

plt.savefig("strategy_chart2.png")
print("Success: 'strategy_chart.png' has been saved!")

