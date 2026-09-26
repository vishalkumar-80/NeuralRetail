import streamlit as st


def show_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    avg_order_value = total_revenue / total_orders if total_orders else 0

    st.subheader("📊 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Total Revenue", f"£{total_revenue:,.2f}")
    col2.metric("🛒 Total Orders", f"{total_orders:,}")
    col3.metric("👥 Total Customers", f"{total_customers:,}")
    col4.metric("📦 Avg Order Value", f"£{avg_order_value:,.2f}")
    st.markdown("---")
