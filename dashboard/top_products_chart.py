import streamlit as st
import plotly.express as px


def show_top_products_chart(df):
    top_products = (
        df.dropna(subset=["Description"])
        .groupby("Description", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .head(10)
    )
    fig = px.bar(
        top_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 Products by Revenue",
        color="Revenue",
        color_continuous_scale="Teal",
        labels={"Revenue": "Revenue (£)", "Description": ""},
    )
    fig.update_layout(
        template="plotly_white",
        yaxis=dict(categoryorder="total ascending"),
        margin=dict(l=10, r=10, t=55, b=10),
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig, use_container_width=True)
