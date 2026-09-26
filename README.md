# NeuralRetail Dashboard

Interactive retail sales analytics dashboard built with Streamlit, Pandas, and Plotly.

## Features

- Country and year filters applied across the dashboard
- Revenue, order, customer, and average order value KPIs
- Monthly revenue trend by year
- Top products and countries by revenue
- RFM customer segmentation
- Filtered dataset preview

## Run locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

The source Excel file is expected at `data/Online Retail.xlsx`.

## Deploy on Streamlit Community Cloud

Select this repository, choose the `main` branch, and set the main file path to `dashboard/app.py`.
