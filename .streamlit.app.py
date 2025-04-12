import streamlit as st
import pandas as pd

# Defining Data
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", None],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4", None],
    [None, "Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4", None],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4", None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4", None],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4", None],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4", None],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4", None],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None],
    [None, "Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4", None],
]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Apply styling to bold the first and second columns
def highlight_columns(val, col_index):
    if col_index == 0 or col_index == 1:  # Bold only for first and second columns
        return "font-weight: bold;"
    return ""

# Build the styled DataFrame
def style_dataframe(df):
    styled_table = df.style.applymap(
        lambda val: "font-weight: bold;" if pd.notna(val) else "", subset=[0, 1]
    )
    return styled_table

# Generate the styled DataFrame
styled_table = style_dataframe(df)

# Display the styled table in Streamlit
st.write(styled_table.to_html(), unsafe_allow_html=True)
