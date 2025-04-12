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
def generate_html_table(data):
    html = "<table style='border-collapse: collapse; width: 100%; table-layout: fixed;'>"
    
    # Iterate over each row in data
    for i, row in enumerate(data):
        # Remove None values from the first row
        if i == 0:
            row = [val for val in row if val is not None]
        
        # Calculate the column width for each row dynamically based on its length
        col_width = 100 / len(row)
        
        html += "<tr>"
        
        for j, val in enumerate(row):
            style = cell_style(j) + f" width: {col_width:.2f}%;"
            html += f"<td style='{style}'>{val}</td>"
        
        html += "</tr>"
    html += "</table>"
    return html

# Render the table in Streamlit
st.write(generate_html_table(data), unsafe_allow_html=True)
