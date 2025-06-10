import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Meetup Finder")

if st.button("Populate Users"):
    res = requests.post(f"{API_URL}/populate")
    st.success(res.json()["message"])

if st.button("Find Closest 100 Users"):
    res = requests.get(f"{API_URL}/closest")
    data = res.json()
    if "closest_users" in data:
        st.write("📍 Reference User:", data["reference_user"])
        df = pd.DataFrame(data["closest_users"])
        st.map(df.rename(columns={"latitude": "lat", "longitude": "lon"}))
        st.dataframe(df)
    else:
        st.warning(data["message"])
