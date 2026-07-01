# Marketing Funnel & Conversion Performance Analysis

An end-to-end Data Analytics project that analyzes marketing campaign performance and customer conversion using Python, Streamlit, and Plotly. This project helps businesses understand customer behavior, identify conversion bottlenecks, and optimize marketing strategies through interactive visualizations and actionable insights.

---

## Project Overview

Marketing campaigns generate thousands of customer interactions, but not every customer converts. Understanding where customers convert, which marketing channels perform best, and which customer segments respond positively is essential for improving business growth.

This project analyzes a real-world marketing dataset to:

- Measure overall conversion performance
- Analyze customer demographics
- Evaluate campaign effectiveness
- Compare conversion rates across customer segments
- Generate business recommendations
- Present insights through an interactive Streamlit dashboard

---

## Business Problem

Businesses often struggle to answer questions such as:

- What is the overall conversion rate?
- Which customer segments convert the most?
- Which months perform better?
- Which contact method is more effective?
- Where should marketing efforts be focused?

This project provides data-driven answers to these questions.

---

## Dataset

**Dataset:** Bank Marketing Dataset

The dataset contains customer information collected during direct marketing campaigns conducted by a banking institution.

### Features

- Age
- Job
- Marital Status
- Education
- Account Balance
- Housing Loan
- Personal Loan
- Contact Method
- Campaign Month
- Campaign Duration
- Previous Marketing Outcome
- Deposit Subscription (Target Variable)

Target Variable:

- **Yes** → Customer subscribed to the term deposit
- **No** → Customer did not subscribe

---

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Jupyter Notebook
- Git
- GitHub

---

## Project Workflow

### 1. Data Collection

- Imported marketing campaign dataset
- Loaded data into Pandas DataFrame

### 2. Data Cleaning

- Removed duplicate records
- Checked missing values
- Verified data types
- Prepared dataset for analysis

### 3. Exploratory Data Analysis

Performed analysis on:

- Customer Age Distribution
- Job Categories
- Education Levels
- Contact Methods
- Monthly Campaign Performance
- Account Balance Distribution

### 4. Marketing Funnel Analysis

Calculated:

- Total Customers Contacted
- Total Converted Customers
- Overall Conversion Rate
- Non-Converting Customers

### 5. Interactive Dashboard

Built a Streamlit dashboard including:

- KPI Cards
- Funnel Chart
- Monthly Conversion Analysis
- Job-wise Conversion
- Education Analysis
- Contact Method Analysis
- Download Filtered Dataset

---

## Dashboard Features

- 📊 Interactive KPI Cards
- 📉 Marketing Funnel Visualization
- 📅 Monthly Conversion Analysis
- 💼 Job-wise Conversion Analysis
- 🎓 Education-wise Performance
- 📞 Contact Method Analysis
- 📥 Download Filtered Dataset
- 🎯 Business Recommendations

---

##  Key Insights

- Calculated the overall customer conversion rate.
- Identified high-performing customer segments.
- Compared conversion across contact methods.
- Evaluated monthly campaign performance.
- Recommended strategies for improving marketing effectiveness.

---

##  Business Recommendations

- Focus campaigns on customer segments with the highest conversion rates.
- Prioritize high-performing communication channels.
- Schedule campaigns during high-conversion months.
- Personalize marketing for low-converting customer groups.
- Improve follow-up strategies for non-converted customers.

---

## Project Structure

```
marketing-funnel-analysis/
│
├── app.py
├── cleaned_marketing_funnel.csv
├── requirements.txt
├── README.md
│
├── notebook/
│   └── marketing_funnel_analysis.ipynb
│
└── assets/
    └── dashboard.png
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/marketing-funnel-analysis.git
```

Navigate to the project:

```bash
cd marketing-funnel-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Dashboard URL

```
https://srisakthipanchanathi-del-future-ds-03-app-qjtoqj.streamlit.app/
```

---

##  Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Marketing Analytics
- Funnel Analysis
- KPI Reporting
- Data Visualization
- Dashboard Development
- Business Intelligence
- Python Programming
- Streamlit Deployment

---

##  Future Enhancements

- Customer Segmentation using Machine Learning
- Conversion Prediction Model
- Marketing Campaign ROI Analysis
- Time-Series Forecasting
- Interactive Executive Dashboard
- Power BI Dashboard Version

---

##  Author

**Sri Sakthi Panchanathi**


---

##  If you found this project useful, consider giving it a star on GitHub!
