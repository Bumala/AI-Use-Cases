import streamlit as st
import pandas as pd

# Data definition with potential for variable column counts
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", None, "Additional Col 1", "Additional Col 2"],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4", None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],
]

# Dynamically process the data to pad rows with empty strings
def process_data(data):
    # Find the maximum number of columns in any row
    max_columns = max(len(row) for row in data)
    
    # Pad each row with empty strings to match the maximum column count
    processed_data = [row + [""] * (max_columns - len(row)) for row in data]
    return processed_data

# Convert processed data to a DataFrame
processed_data = process_data(data)
df = pd.DataFrame(processed_data)

# Style generator for table cells
def cell_style(col_index):
    style = "text-align: left; padding: 5px; border: 1px solid #ddd;"
    if col_index == 0:  # First column (merged cells)
        style += " font-weight: bold; background-color: #f0f0f0;"
    elif col_index == 1:  # Second column
        style += " font-weight: bold;"
    return style

# Generate HTML table dynamically
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            style = cell_style(j)
            if j == 0:  # Handle merged cells for the first column
                if i == 0 and val == "Impact (What)":
                    html += f"<td rowspan='2' style='{style}'>{val}</td>"
                elif i == 3 and val == "Technology (How)":
                    html += f"<td rowspan='1' style='{style}'>{val}</td>"
                elif val:
                    html += f"<td style='{style}'>{val}</td>"
            else:
                html += f"<td style='{style}'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate and display the HTML table in Streamlit
html_table = generate_html_table(df)
st.write(html_table, unsafe_allow_html=True)
