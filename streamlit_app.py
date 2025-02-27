import streamlit as st
import pandas as pd
import numpy as np

# Google Sheets Configuration
SHEET_ID = "1mB6AZurMLAqDJmou3z0IhOpz5LQAP413"
SHEET_NAME = "Sheet1"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Function to fetch real-time investment data
@st.cache_data(ttl=30)  # Refreshes every 30 sec
def fetch_data():
    df = pd.read_csv(SHEET_URL, parse_dates=["Date"])
    return df

# Function to run simplified Monte Carlo investment simulations
def run_simple_investment_simulation(data, num_simulations, num_days):
    daily_returns_mean = data["Daily Returns"].mean()
    daily_returns_std = data["Daily Returns"].std()

    # Generate random daily returns for simulations
    simulated_daily_returns = np.random.normal(daily_returns_mean, daily_returns_std, (num_days, num_simulations))

    # Calculate cumulative returns for each simulation
    cumulative_returns = np.cumprod(1 + simulated_daily_returns, axis=0)

    # Adding a row of simulated cumulative returns at the end (to simulate portfolio growth)
    initial_investment = data["Investment Amount"].iloc[0]
    simulated_portfolio_value = initial_investment * cumulative_returns
    
    return pd.DataFrame(simulated_portfolio_value)

# Streamlit UI
st.title("📈 Investment Monte Carlo Simulator")

# Load Data
df = fetch_data()

if df.empty:
    st.error("❌ No data found! Check your Google Sheets connection.")
else:
    st.success("✅ Investment Data Loaded Successfully!")

    # Show editable portfolio data
    st.subheader("💼 Edit Your Portfolio Data")
    edited_df = st.data_editor(df, num_rows="dynamic")

    # Check required columns
    required_columns = ["Date", "Investment Amount", "Daily Returns", "Cumulative Returns"]
    if not all(col in edited_df.columns for col in required_columns):
        st.error("❌ Missing required columns! Ensure 'Date', 'Investment Amount', 'Daily Returns', and 'Cumulative Returns' exist.")
    else:
        # Portfolio Summary
        total_investment = edited_df["Investment Amount"].sum()
        st.metric(label="💰 Total Investment", value=f"${total_investment:,.2f}")

        # Plot investment growth, daily returns, and cumulative returns over time
        st.subheader("📊 Investment Growth Over Time")
        combined_plot = edited_df.set_index("Date")[["Daily Returns", "Cumulative Returns", "Investment Amount"]]
        st.line_chart(combined_plot)

        # Set simulation parameters
        st.subheader("🎛️ Simulation Settings")
        st.caption("Choose the number of simulations and the investment horizon.")

        num_simulations = st.slider("Number of Simulations", min_value=50, max_value=500, value=100, step=50)
        num_days = st.slider("Investment Horizon (Days)", min_value=30, max_value=252, value=252, step=30)

        # Buttons
        col1, col2 = st.columns(2)
        run_simulation = col1.button("🚀 Run Simulation")
        reset_data = col2.button("🔄 Reset Data")

        if reset_data:
            st.cache_data.clear()
            st.experimental_rerun()

        if run_simulation:
            st.subheader(f"📊 Running {num_simulations} Simulations Over {num_days} Days")

            # Run Simulations
            simulation_results = run_simple_investment_simulation(edited_df, num_simulations, num_days)

            # Display simulation results
            st.line_chart(simulation_results)

            # Predictions - Summary Statistics for the predicted returns
            st.subheader("📈 Predictions: Summary Statistics for the Predicted Returns")

            # Calculate summary statistics for the final predicted returns
            final_returns = simulation_results.iloc[-1]
            summary_stats = final_returns.describe()

            st.write(f"Count: {len(final_returns)}")
            st.write(f"Mean: {summary_stats['mean']:.3f}")
            st.write(f"Standard Deviation: {summary_stats['std']:.3f}")
            st.write(f"Minimum: {summary_stats['min']:.3f}")
            st.write(f"25th Percentile: {summary_stats['25%']:.3f}")
            st.write(f"Median (50th Percentile): {summary_stats['50%']:.3f}")
            st.write(f"75th Percentile: {summary_stats['75%']:.3f}")
            st.write(f"Maximum: {summary_stats['max']:.3f}")

            # Download button for simulated portfolio value data
            st.download_button(
                label="📥 Download Simulated Portfolio Values",
                data=simulation_results.to_csv(index=False),
                file_name="simulated_portfolio_values.csv",
                mime="text/csv"
            )