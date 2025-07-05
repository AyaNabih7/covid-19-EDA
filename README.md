
# 📊 COVID‑19 EDA App (Streamlit)

An interactive web app for **Exploratory Data Analysis (EDA)** of COVID‑19 data, built using **Python**, **Pandas**, and **Streamlit**.

---

## 🚀 Features

- 🌍 View **global** and **country-level** COVID‑19 statistics
- 🗓️ Filter by **date range** and **region**
- 📈 Interactive visualizations:
  - Time-series line charts
  - Country comparisons (bar charts)
  - Pie charts of active vs recovered vs deaths
- 🎛️ Clean and simple user interface using Streamlit widgets

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – data manipulation
- **Streamlit** – building the interactive web app
- **Plotly / Matplotlib / Seaborn** – data visualization

---

## 📦 Project Structure

```

covid-19-EDA/
├── Main.py              # Main Streamlit application
├── Helper.py            # Functions
├── data/                # COVID-19 dataset(s)
├── pages/               # Optional Streamlit multi-page structure
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

````

---

## 📥 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/AyaNabih7/covid-19-EDA.git
cd covid-19-EDA
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## 📊 Visualizations

* Total and daily confirmed/death/recovered cases
* Country-wise bar charts
* Active vs recovered vs deaths (pie charts)
* Region-specific time series

---

## ✅ Requirements

* Python 3.7+
* Streamlit
* Pandas
* Plotly or Matplotlib or Seaborn

(See `requirements.txt` for the full list of dependencies.)

