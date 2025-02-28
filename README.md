# 📈 Real-Time Investment Portfolio Monte Carlo Simulation

This **interactive Streamlit dashboard** provides real-time investment portfolio analysis using **Monte Carlo simulations**. It allows users to analyze potential portfolio outcomes, visualize historical performance, and estimate key statistics based on live data.

## 🚀 Features

- **Real-Time Data Integration**: Fetches live portfolio data from Google Sheets.
- **Editable Portfolio Data**: Modify investment values directly in the app.
- **Investment Growth Visualization**: View portfolio trends with interactive charts.
- **Automated Monte Carlo Simulations**: Runs simulations instantly without manual execution.
- **Predicted Returns Summary**: Provides key statistics (mean, standard deviation, percentiles).

---

## 🛠 Requirements

To run this project, ensure you have:

- Python 3.x
- Streamlit
- Pandas
- NumPy

You can install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🏗 Installation Instructions

### **Running in GitHub Codespaces**

1. **Open the repository** and click **"Open with Codespaces"**.
2. **Setup** will be handled automatically via the `devcontainer.json`.
3. **Run the app**:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Open **`http://localhost:8501`** in your browser.

---

### **Running Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MohammadBaniAbdElNabi/Dynamic_dashboard-1.git
   cd Dynamic_dashboard-1
   ```

2. **(Optional) Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows users: `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   streamlit run streamlit_app.py
   ```
   Open **`http://localhost:8501`** in your browser.

---

## 📊 How It Works

### **1. Live Data Fetching**
- The app **pulls investment data from Google Sheets** in real time.
- Users can **edit portfolio values dynamically**.

### **2. Monte Carlo Simulations**
- Runs **automatically** to project portfolio performance.
- Generates **thousands of random scenarios** based on historical data.

### **3. Investment Growth Visualization**
- **Line charts** display **portfolio value, daily returns, and cumulative returns**.
- **Predicted return summary** gives key financial statistics.

---

## 🤝 Contributions

We welcome contributions!  
To contribute:
1. **Fork the repo**
2. **Submit a pull request**
3. Open an **issue** for major feature requests.

---

## 📜 License

This project is licensed under the **Apache License**. See the [LICENSE](LICENSE) file for details.