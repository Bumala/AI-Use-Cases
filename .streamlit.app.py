import streamlit as st
import pandas as pd

# Data definition
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

# Prepare data dynamically to remove empty cells
def prepare_data(data):
    new_data = []
    for row in data:
        new_row = [cell for cell in row if cell is not None]  # Remove None values
        if new_row:  # Avoid adding empty rows
            new_data.append(new_row)
    return new_data

# Convert prepared data to a DataFrame
prepared_data = prepare_data(data)
df = pd.DataFrame(prepared_data)

# Style generator for table cells
def cell_style(col_index):
    style = "text-align: left; padding: 5px; border: 1px solid #ddd;"
    if col_index == 0:  # First column (merged cells)
        style += " font-weight: bold; background-color: #f0f0f0;"
    elif col_index == 1:  # Second column
        style += " font-weight: bold;"
    return style

# Generate HTML table with dynamic layout
def generate_html_table_dynamic(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            style = cell_style(j)

            if i == 0 and j == 0:  # Handle first column merged cells
                html += f"<td rowspan='5' style='{style}'>{val}</td>"
            elif i == 5 and j == 0:
                html += f"<td rowspan='5' style='{style}'>{val}</td>"
            elif i == 10 and j == 0:
                html += f"<td rowspan='2' style='{style}'>{val}</td>"
            else:  # Regular cells
                html += f"<td style='{style}'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate and display the table in Streamlit
html_table = generate_html_table_dynamic(df)
st.write(html_table, unsafe_allow_html=True)
