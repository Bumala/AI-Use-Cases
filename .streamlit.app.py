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
df_morph = pd.read_excel(uploaded_file, sheet_name=1, header=None)

# Extract headers from Excel row 3 (index 2)
headers = df_morph.iloc[2, 1:].tolist()

# Extract morphological box data from Excel rows 4 to 15 (indices 3 to 14)
morph_display = df_morph.iloc[3:15, 1:]
morph_display.columns = headers
morph_display.reset_index(drop=True, inplace=True)

# Assign dimension labels based on row indices
dimension_labels = []
for idx in range(len(morph_display)):
    if 3 <= idx + 3 <= 8:   # Excel rows 4–8
        dimension_labels.append("Impact (What)")
    elif 9 <= idx + 3 <= 13:  # Excel rows 9–13
        dimension_labels.append("Technology (How)")
    else:  # Excel rows 14–15
        dimension_labels.append("Place (Where)")
morph_display["Dimension"] = dimension_labels

# Extract selectable impact elements
impact_elements = morph_display[morph_display["Dimension"] == "Impact (What)"]["Impact (What)"].dropna().tolist()

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
    highlight_display = morph_display.copy()
    top_index = df_use_cases["Total Score"].idxmax()
    selected_row = df_use_cases.loc[top_index]

    for i, row in highlight_display.iterrows():
        dim = row["Dimension"]
        for col in highlight_display.columns[:-1]:  # ignore Dimension column
            val = row[col]
            if pd.isna(val):
                continue
            if selected_row.get(val, 0) == 2:
                highlight_display.at[i, col] = f"<span style='background-color:#33ccff; color:black; padding:4px; border-radius:6px'>{val}</span>"
            elif selected_row.get(val, 0) == 1:
                highlight_display.at[i, col] = f"<span style='background-color:#6666ff; color:white; padding:4px; border-radius:6px'>{val}</span>"

    # Show the morphological box with HTML formatting
    st.markdown("---")
    st.markdown("### Full Morphological Box")
    st.markdown("""<div style='display: flex; justify-content: center;'>""", unsafe_allow_html=True)
    st.markdown(highlight_display.drop(columns="Dimension").to_html(escape=False, index=False), unsafe_allow_html=True)
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
