import streamlit as st
import pandas as pd

# Cleaned up data
data = [
    # Skip the first cell in the first row
    ["Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost", "Revenue Model"],
    ["Impact (What)", "Focus within Business Model Navigator", "Customer Segments", "Value proposition", "Value Chain", None],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4", None, None],
    [None, "Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4", None, None],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4", None, None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None, None],
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4", None, None],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4", None, None],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4", None, None],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4", None, None],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None, None],
    [None, "Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4", None, None],
]

df = pd.DataFrame(data)

# Bold style for first and second columns
def cell_style(j):
    base = "text-align: left; padding: 8px; border: 1px solid #ddd;"
    if j == 0 or j == 1:
        return base + " font-weight: bold;"
    return base

# Generate HTML table
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%; table-layout: fixed;'>"
    
    for i, row in df.iterrows():
        html += "<tr>"
        
        # Custom header row
        if i == 0:
            col_width = 100 // len(row)
            for j, val in enumerate(row):
                style = cell_style(j) + f" width: {col_width}%; background-color: #f0f0f0;"
                html += f"<th style='{style}'>{val}</th>"
            html += "</tr>"
            continue
        
        for j, val in enumerate(row):
            style = cell_style(j)
            if j == 0:
                if i == 1 and val == "Impact (What)":
                    html += f"<td rowspan='4' style='{style}'>{val}</td>"
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

# Display in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
