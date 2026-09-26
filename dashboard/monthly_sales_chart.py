import streamlit as st
import plotly.express as px


def show_monthly_sales_chart(df):
    monthly_sales = (
        df.groupby(["Year", "Month"], as_index=False)["Revenue"]
        .sum()
        .sort_values(["Year", "Month"])
    )
    fig = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        color="Year",
        markers=True,
        title="Monthly Sales Trend",
        hover_data={"Year": True, "Revenue": ":,.2f"},
        labels={"Revenue": "Revenue (£)", "Month": "Month"},
    )
    fig.update_layout(
        template="plotly_white",
        xaxis=dict(tickmode="linear", dtick=1),
        margin=dict(l=10, r=10, t=55, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)
