
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
df = pd.read_csv("data/ads_switzerland_1000.csv")

lang = st.sidebar.radio("Language / Sprache", ["English", "Deutsch"])

labels = {
    "English": {
        "title": "Swiss Advertising Analysis (2019–2024)",
        "brands": "Top Brands",
        "celebs": "Top Celebrities",
        "copy": "Sample Ad Copy"
    },
    "Deutsch": {
        "title": "Werbung in der Schweiz (2019–2024)",
        "brands": "Top-Marken",
        "celebs": "Prominente in der Werbung",
        "copy": "Beispielhafte Werbetexte"
    }
}

st.title(labels[lang]["title"])
st.subheader(labels[lang]["brands"])
st.bar_chart(df["Brand"].value_counts().head(10))

st.subheader(labels[lang]["celebs"])
celeb_df = df[df["Celebrity Featured"] != ""]
st.bar_chart(celeb_df["Celebrity Featured"].value_counts().head(10))

st.subheader(labels[lang]["copy"])
st.dataframe(df[["Brand", "Ad Copy / Script"]].sample(5).reset_index(drop=True))
