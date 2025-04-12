import streamlit as st
import pandas as pd

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", None],
    [None, "Row 3, Col 2", "Row 3, Col 3", None],
    [None, "Row 4, Col 2"],
    [None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],
    [None, "Row 7, Col 2", "Row 7, Col 3", None],
    [None, "Row 8, Col 2"],
    [None],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None],
    [None, "Row 12, Col 2", "Row 12, Col 3"],
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Style generator for table cells
def cell_style():
    return "text-align: left; padding: 5px; border: 1px solid #ddd;"

# Generate HTML table
def generate_html_table(df):
    # Find the maximum number of columns in any row
    max_columns = max(len(row.dropna()) for _, row in df.iterrows())

    # Start the table with styling
    html = "<table style='border-spacing: 2px; width: 100%; border: 1px solid black;'>"

    # Generate rows dynamically
    for i, row in df.iterrows():
        html += "<tr>"
        filled_columns = 0
        for j in range(len(row)):  # Loop through all columns in the current row
            val = row[j]
            style = cell_style()

            if val is not None:
                html += f"<td style='{style}'>{val}</td>"
                filled_columns += 1

        # Fill remaining columns with a single cell spanning the remaining space
        if filled_columns < max_columns:
            colspan = max_columns - filled_columns
            html += f"<td colspan='{colspan}' style='{cell_style()}'></td>"

        html += "</tr>"

    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
