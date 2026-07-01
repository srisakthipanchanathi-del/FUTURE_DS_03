import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Marketing Funnel Dashboard",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_marketing_funnel.csv")

df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Dashboard Filters")

jobs = st.sidebar.multiselect(
    "Job",
    sorted(df["job"].unique()),
    default=sorted(df["job"].unique())
)

months = st.sidebar.multiselect(
    "Month",
    ["jan","feb","mar","apr","may","jun",
     "jul","aug","sep","oct","nov","dec"],
    default=["jan","feb","mar","apr","may","jun",
             "jul","aug","sep","oct","nov","dec"]
)

education = st.sidebar.multiselect(
    "Education",
    sorted(df["education"].unique()),
    default=sorted(df["education"].unique())
)

filtered = df[
    (df["job"].isin(jobs)) &
    (df["month"].isin(months)) &
    (df["education"].isin(education))
]

# -----------------------------
# TITLE
# -----------------------------
st.title("📈 Marketing Funnel & Conversion Performance Dashboard")

st.markdown("""
This dashboard analyzes marketing campaign performance and customer conversions.
""")

# -----------------------------
# KPI CARDS
# -----------------------------
total = len(filtered)
converted = (filtered["deposit"] == "yes").sum()
not_converted = (filtered["deposit"] == "no").sum()

conversion_rate = (converted / total) * 100 if total > 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers Contacted", total)
col2.metric("Converted", converted)
col3.metric("Not Converted", not_converted)
col4.metric("Conversion Rate", f"{conversion_rate:.2f}%")

st.divider()

# -----------------------------
# FUNNEL CHART
# -----------------------------
st.subheader("Marketing Funnel")

fig = go.Figure(go.Funnel(
    y=[
        "Customers Contacted",
        "Converted"
    ],
    x=[
        total,
        converted
    ]
))

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# MONTHLY CONVERSION
# -----------------------------
st.subheader("Monthly Conversion Rate")

month_conversion = (
    filtered.groupby("month")["deposit"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .reset_index(name="Conversion")
)

month_order = [
    "jan","feb","mar","apr","may","jun",
    "jul","aug","sep","oct","nov","dec"
]

month_conversion["month"] = pd.Categorical(
    month_conversion["month"],
    categories=month_order,
    ordered=True
)

month_conversion = month_conversion.sort_values("month")

fig = px.bar(
    month_conversion,
    x="month",
    y="Conversion",
    color="Conversion",
    title="Monthly Conversion Rate"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# JOB ANALYSIS
# -----------------------------
st.subheader("Conversion by Job")

job_conversion = (
    filtered.groupby("job")["deposit"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .reset_index(name="Conversion")
)

job_conversion = job_conversion.sort_values(
    by="Conversion",
    ascending=False
)

fig = px.bar(
    job_conversion,
    x="job",
    y="Conversion",
    color="Conversion"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# EDUCATION
# -----------------------------
st.subheader("Education Analysis")

education_conversion = (
    filtered.groupby("education")["deposit"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .reset_index(name="Conversion")
)

fig = px.bar(
    education_conversion,
    x="education",
    y="Conversion",
    color="Conversion"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# CONTACT METHOD
# -----------------------------
st.subheader("Contact Method Performance")

contact = (
    filtered.groupby("contact")["deposit"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .reset_index(name="Conversion")
)

fig = px.pie(
    contact,
    names="contact",
    values="Conversion",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# AGE DISTRIBUTION
# -----------------------------
st.subheader("Customer Age Distribution")

fig = px.histogram(
    filtered,
    x="age",
    nbins=30,
    title="Age Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# BALANCE DISTRIBUTION
# -----------------------------
st.subheader("Account Balance Distribution")

fig = px.box(
    filtered,
    y="balance",
    title="Customer Balance"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# DOWNLOAD
# -----------------------------
st.subheader("Download Filtered Data")

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_marketing_data.csv",
    mime="text/csv"
)

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------
st.subheader("Business Recommendations")

st.success("""
• Focus marketing on customer segments with the highest conversion rates.

• Prioritize the best-performing contact methods.

• Schedule campaigns during high-converting months.

• Personalize offers for customer groups with lower conversion rates.

• Improve follow-up strategies for customers who did not convert.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Created by Sri Sakthi Panchanathi | Marketing Funnel & Conversion Analysis")