import streamlit as st
import pandas as pd

# Data definition with variable column length
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Row 4, Col 3", "Row 4, Col 4"],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4"],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4"],
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4"],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4"],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4"],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4"],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4"],
    [None, "Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4"],
]

# Find the max column count
max_cols = max(len(row) for row in data)

# Pad shorter rows to ensure consistent column length
for row in data:
    row += [None] * (max_cols - len(row))

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Function to apply styles, including text wrapping
def cell_style(j):
    base = (
        "text-align: left; "
        "padding: 8px; "
        "border: 1px solid #ddd; "
        "word-wrap: break-word; "
        "white-space: pre-wrap; "
        "vertical-align: top;"
    )
    if j in [0, 1]:  # Apply bold styling to the first two columns
        return base + " font-weight: bold;"
    return base

# HTML table generator
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%; table-layout: fixed;'>"
    
    # Calculate the column width for columns 2 onwards (columns 2 to max_cols-1)
    col_width = 100 / max_cols
    
    for i, row in df.iterrows():
        html += "<tr>"
        
        for j, val in enumerate(row):
            style = cell_style(j) + f" width: {col_width:.2f}%;"

            # Handle merged cells for the first column
            if j == 0:
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

# Render the table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
