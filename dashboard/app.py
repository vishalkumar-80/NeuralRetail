import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering
from dashboard.sidebar import show_sidebar
from dashboard.kpi import show_kpis
from dashboard.monthly_sales_chart import show_monthly_sales_chart
from dashboard.top_products_chart import show_top_products_chart
from dashboard.country_chart import show_country_chart
from dashboard.customer_segment_chart import show_customer_segmentation_chart

st.set_page_config(page_title="NeuralRetail Dashboard", page_icon="🛍️", layout="wide")
st.title("🛍️ NeuralRetail Dashboard")
st.caption("Online retail sales, customer behavior, and market performance")

file_path = Path(__file__).resolve().parent.parent / "data" / "Online Retail.xlsx"

@st.cache_data(show_spinner="Loading and preparing retail data…")
def load_dashboard_data(path):
    return feature_engineering(clean_data(path))

df = load_dashboard_data(str(file_path))
selected_country, selected_year = show_sidebar(df)
filtered_df = df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == selected_year]

st.caption(f"Showing {len(filtered_df):,} transactions")
if filtered_df.empty:
    st.info("No transactions match these filters. Choose another country or year.")
    st.stop()

show_kpis(filtered_df)
col1, col2 = st.columns(2)
with col1:
    show_monthly_sales_chart(filtered_df)
with col2:
    show_top_products_chart(filtered_df)
col3, col4 = st.columns(2)
with col3:
    show_customer_segmentation_chart(filtered_df)
with col4:
    show_country_chart(filtered_df)
with st.expander("📄 Dataset Preview"):
    st.dataframe(filtered_df.head(100), use_container_width=True)
