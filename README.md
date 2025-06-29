# 🧾 UNIQLO Sales Analysis Project

This project analyzes synthetic sales data from a fictional UNIQLO retail environment to uncover trends in product performance, channel efficiency, and customer behavior using Python, SQLite, and Tableau.

---

## 💼 Key Tools

- **Python (Pandas, SQLite3)** – Data cleaning & SQL-based KPI extraction
- **SQLite** – Lightweight database for querying KPIs
- **Tableau** – Dashboard visualizations for product and sales trends
- **Git & GitHub** – Version control and portfolio hosting

---

## 🧠 KPIs & Analyses Performed

| KPI / Insight                          | Description                                                  |
|----------------------------------------|--------------------------------------------------------------|
| 🛍️ Top Products                        | Most popular items by units sold                             |
| 💰 Revenue by Category/Subcategory     | Identified high-revenue product lines                        |
| 🎯 Channel Performance                 | Compared online vs in-store sales and sales share            |
| 🎨 Sales by Color & Size               | Customer preference insights                                 |
| 👤 Sales by Gender                     | Gender-based purchasing trends                               |
| 🕒 Seasonal Trends                     | Demand variation across seasons                              |
| 🔁 Inventory & Restocking              | Inventory turnover and restock flag detection                |
| 💸 Average Discount Rate               | Analyzed promotional impact by category                      |

---

## 📊 Tableau Dashboard

> View all KPIs and visual trends in an interactive dashboard.

🧾 File: `dashboards/uniqlo_dashboard.twbx`  
📍 Tool: Tableau Public

![Dashboard Preview](dashboards/dashboard_screenshot.png)

---

## ✨ Features

- Cleaned and transformed raw sales data for analysis
- Created a relational database using SQLite
- Generated SQL queries to extract business KPIs
- Exported query results for dashboarding
- Built a fully interactive Tableau dashboard

---

## 🚀 How to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/austin-ing/uniqlo-sales-analysis.git
    cd uniqlo-sales-analysis
    ```

2. **Create virtual environment & install requirements**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install pandas
    ```

3. **Run data pipeline**:
    ```bash
    cd src/
    python sqlite_file.py
    ```

4. **Open Tableau** and import the `.twbx` dashboard or use the exported CSVs in `queries/`.

---

## 📚 Learning Goals

- Simulate a real-world **product performance dashboard**
- Practice **end-to-end data analysis** using Python + SQL + Tableau
- Strengthen **portfolio for product management or analytics roles**

---

## 📌 Author

**Austin Ing**  
💼 Aspiring Product Manager / Data Analyst  
🔗 [LinkedIn](https://www.linkedin.com/in/austin-ing/) | [GitHub](https://github.com/austin-ing)