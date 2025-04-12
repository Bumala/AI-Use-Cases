import streamlit as st
import pandas as pd

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", "bb", "cccccc", "ggg"],
    [None, "Row 3, Col 2", "Row 3, Col 3"],
    [None, "Row 4, Col 2"],
    [None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4"],
    [None, "Row 8, Col 2", "Row 8, Col 3"],
    [None, "Row 9, Col 2"],
    [None],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None],
    [None, "Row 12, Col 2", "Row 12, Col 3"],
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Style generator for table cells
def cell_style(col_index):
    style = "text-align: left; padding: 5px; border: 1px solid #ddd;"
    if col_index in [0, 1]:
        style += " font-weight: bold;"
    return style

# Generate HTML table
def generate_html_table(df):
    # Find the maximum number of columns in any row
    max_columns = max(len(row.dropna()) for _, row in df.iterrows())

    # Start the table with styling
    html = "<table style='border-spacing: 2px; width: 100%; border: 1px solid black;'>"

    # Generate rows dynamically
    for i, row in df.iterrows():
        html += "<tr>"
        for j in range(max_columns):  # Loop through the maximum number of columns
            val = row[j] if j < len(row) else ""  # Fill with empty string if column doesn't exist
            style = cell_style(j)

            if j == 0:  # Handle merged cells for the first column
                if i == 0 and val == "Impact (What)":
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif i == 5 and val == "Technology (How)":
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif i == 10 and val == "Place (Where)":
                    html += f"<td rowspan='2' style='{style}'>{val}</td>"
                elif val is not None:
                    html += f"<td style='{style}'>{val}</td>"
            elif val is not None:
                html += f"<td style='{style}'>{val}</td>"
            else:
                html += f"<td style='{style}'></td>"
        html += "</tr>"
    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
