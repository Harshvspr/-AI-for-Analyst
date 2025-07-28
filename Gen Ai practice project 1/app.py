# main.py

import streamlit as st
from langchain_helper import restaurant_name_dishes_generator

st.title("🍽️ Restaurant Name Generator")

# create sidebar
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Spanish", "Japanese"))

if cuisine:
    response = restaurant_name_dishes_generator(cuisine)

    # restaurant name
    st.header(f"🏠 Restaurant: {response['restaurant_name']}")

    #  menu items
    st.subheader("🍽️ Menu Items:")
    menu_items = response['menu_items'].split(',')
    for item in menu_items:
        st.write("•", item.strip())

