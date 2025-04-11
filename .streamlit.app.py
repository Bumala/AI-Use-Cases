# Web app using Streamlit to display a morphological box and analyze data from Excel
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import base64

# Load data from Excel file
uploaded_file = "Use Cases.xlsx"

# Load both sheets
df_use_cases = pd.read_excel(uploaded_file, sheet_name="IBM SPSS Statistics")
df_morph_raw = pd.read_excel(uploaded_file, sheet_name=1)

# Fix headers and extract morphological box
df_morph_raw.columns = df_morph_raw.iloc[1]  # Set row 1 as header (Impact, Technology, Place)
df_morph = df_morph_raw[2:].reset_index(drop=True)  # Skip first 2 rows

morph_display = df_morph.copy()

# Get list of Impact elements (non-NaN from Impact column)
impact_elements = morph_display['Impact'].dropna().tolist()

# Configure page aesthetics
st.set_page_config(layout="wide", page_title="AI Use Case Morphological Box")
st.markdown("""
    <style>
        body {
            background-color: #0f1116;
            color: white;
        }
        .block-container {
            background-image: url('https://i.imgur.com/vjPGJbi.jpeg');
            background-size: cover;
            background-position: center;
            padding: 2rem;
        }
        .stDataFrame thead tr th {
            background-color: #2c2f35 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("\U0001F4BB AI Use Case Morphological Box")
st.markdown("Select impact factors to explore the most relevant AI use case.")

# Create selection boxes under Impact
st.markdown("### Dimension: Impact")
selected_impacts = st.multiselect("Select relevant impact elements:", impact_elements)

# Filter only the first dimension's selected criteria
if selected_impacts:
    scores = df_use_cases[selected_impacts]
    df_use_cases["Total Score"] = scores.sum(axis=1)
    top_use_case = df_use_cases.loc[df_use_cases["Total Score"].idxmax()]

    st.markdown("---")
    st.markdown("### \U0001F3C6 Most Relevant AI Use Case")
    st.success(f"**{top_use_case.iloc[0]}** with a total relevance score of **{top_use_case['Total Score']}**")

    # Highlight Technology and Place dimensions
    tech_place_data = morph_display.copy()
    top_index = df_use_cases["Total Score"].idxmax()
    selected_row = df_use_cases.loc[top_index]

    for col in ["Technology", "Place"]:
        for idx, val in tech_place_data[col].items():
            if pd.isna(val):
                continue
            if selected_row.get(val, 0) == 2:
                tech_place_data.at[idx, col] = f"<span style='background-color:#33ccff; color:black; padding:4px; border-radius:6px'>{val}</span>"
            elif selected_row.get(val, 0) == 1:
                tech_place_data.at[idx, col] = f"<span style='background-color:#6666ff; color:white; padding:4px; border-radius:6px'>{val}</span>"

    # Show the morphological box with HTML formatting
    st.markdown("---")
    st.markdown("### Full Morphological Box")
    st.markdown("""<div style='display: flex; justify-content: center;'>""", unsafe_allow_html=True)
    st.markdown(tech_place_data.to_html(escape=False, index=False), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### \U0001F91D Similar Use Cases")
    # PLACEHOLDER: Insert cluster logic here to identify use cases in the same cluster as `top_use_case`
    # Example:
    # cluster_map = { 'Use Case Name': [other_use_cases_in_same_cluster] }
    # similar_cases = cluster_map.get(top_use_case.iloc[0], [])
    # for case in similar_cases:
    #     st.write(f"- {case}")
    st.info("[Insert similar use cases from the same cluster here]")
else:
    st.info("Please select one or more impact elements above to see the top AI use case.")
