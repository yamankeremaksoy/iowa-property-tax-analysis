# 🏛️ Iowa Property Tax Levy Rates Analysis (FY 2017)

This repository contains an Exploratory Data Analysis (EDA) performed on the **Iowa Property Tax Levy Rates dataset for Fiscal Year 2017**. The project analyzes municipal tax distributions, identifies primary financial cost drivers (such as Employee Benefits and Debt Service obligations), and highlights tax rate disparities across various Iowa cities.

---

## 📌 Dataset Summary & Scope

* **Dataset Title:** Iowa Property Tax Levy Rates (FY 2017)
* **Fiscal Period:** FY 2017 (Ended June 30, 2017)
* **Key Fields Analyzed:** `city_code`, `city_name`, `levy_category`, `levy_component`, `levy_rate`

---

## 📊 Key Analytical Takeaways

1. **Tax Rate Disparities:** 
   * **Audubon (05G027)** recorded the highest total levy rate in the dataset at **21.36320**, driven significantly by employee benefit expenses.
   * **Harpers Ferry (03G010)** maintained the lowest total tax rate at **7.98888**.
2. **Standardized Base Levies:**
   * **Regular General Levy** is fixed/capped at **8.10000** for almost all reporting municipalities (except Harpers Ferry at ~7.05).
   * **Ag Land Levy** is applied at a uniform rate of **3.00375** across recorded entries.
3. **Primary Cost Drivers:** Variations in total tax rates across top municipalities are primarily dictated by **Employee Benefits Levies** (e.g., Audubon at 7.59478) and **Debt Service Obligations** (e.g., Corning).
4. **Data Completeness Note:** Total levy rate entries were unrecorded/blank for 15 municipalities (e.g., Orient, Postville, Waukon, Moravia).

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Pandas** (Data Aggregation & Structural Analysis)
* **Matplotlib** (Data Visualization)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/yamankeremaksoy/iowa-property-tax-analysis.git](https://github.com/yamankeremaksoy/iowa-property-tax-analysis.git)
   cd iowa-property-tax-analysis
pip install pandas matplotlib
python iowa_tax_analysis.py

📈 Visual Output
Running iowa_tax_analysis.py generates a visualization (tax_rates_chart.png) comparing total property tax levy rates across the analyzed Iowa cities.