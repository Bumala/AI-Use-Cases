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

# Dynamically process the data to remove empty cells and adjust layout
def process_data(data):
    processed_data = []
    for row in data:
        # Remove `None` values and append only rows with content
        processed_row = [cell for cell in row if cell is not None]
        if processed_row:
            processed_data.append(processed_row)
    return processed_data

# Convert processed data to DataFrame
processed_data = process_data(data)
df = pd.DataFrame(processed_data)

# Style generator for table cells
def cell_style(col_index):
    style = "text-align: left; padding: 5px; border: 1px solid #ddd;"
    if col_index == 0:  # For the first column
        style += " font-weight: bold; background-color: #f0f0f0;"
    elif col_index == 1:  # For the second column
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
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif i == 5 and val == "Technology (How)":
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif i == 10 and val == "Place (Where)":
                    html += f"<td rowspan='2' style='{style}'>{val}</td>"
                else:
                    html += f"<td style='{style}'>{val}</td>"
            else:
                html += f"<td style='{style}'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate and display the HTML table in Streamlit
html_table = generate_html_table(df)
st.write(html_table, unsafe_allow_html=True)
