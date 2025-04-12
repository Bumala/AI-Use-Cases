# Web app using Streamlit to display a morphological box from an Excel file
import streamlit as st
import pandas as pd

# Load data from the Excel file
uploaded_file = "Use Cases.xlsx"

# Load the second sheet (morphological box)
df_morph = pd.read_excel(uploaded_file, sheet_name=1, header=None)

# Streamlit page configuration
st.set_page_config(layout="wide", page_title="Morphological Box Viewer")
st.title("Morphological Box Viewer")

# Display the morphological box exactly as it appears in the Excel file
st.markdown("### Morphological Box")
st.dataframe(df_morph, height=600)

st.markdown("---")
st.info("This morphological box is displayed exactly as it appears in the Excel file.")
