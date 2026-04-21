import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

st.set_page_config(layout="wide")
df_reviews = pd.read_csv("acents/customer reviews.csv")
df_top100_books = pd.read_csv("acents/Top-100 Trending Books.csv")

df_top100_books

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price=st.sidebar.slider("Price range", price_min, price_max,price_max)
df_books= df_top100_books[df_top100_books["book price"] <= max_price]

fig=px.bar(df_books["year of publication"].value_counts())
fig2=px.histogram(df_books["book price"])

fig.update_traces(
    marker_color='magenta'
)
fig2.update_traces(
    marker_color='magenta'
)

col1, col2= st.columns(2)
with col1:
    st.plotly_chart(fig)
with col2:
    st.plotly_chart(fig2)

