import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
df_reviews = pd.read_csv("acents/customer reviews.csv")
df_top100_books = pd.read_csv("acents/Top-100 Trending Books.csv")

book= df_top100_books["book title"].unique()
book= st.sidebar.selectbox("books", book)

df_book = df_top100_books[df_top100_books["book title"]== book]
df_reviews_book = df_reviews[df_reviews["book name"]== book]


book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]



st.title(book_title)
st.subheader(book_genre)

col1,col2,col3=st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

for row in df_reviews.values:
    message= st.chat_message(f"{row[4]}")
    st.write(f"**{row[2]}**")
    st.write(row[5])




