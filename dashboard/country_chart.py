import streamlit as st
import plotly.express as px


def show_country_chart(df):
    country_sales = (
        df.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .head(10)
    )
    fig = px.bar(
        country_sales,
        x="Revenue",
        y="Country",
        color="Revenue",
        title="Top 10 Countries by Revenue",
        orientation="h",
        color_continuous_scale="Blues",
        labels={"Revenue": "Revenue (£)", "Country": ""},
    )
    fig.update_layout(
        template="plotly_white",
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=55, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)
