import streamlit as st
import pandas as pd

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator ", "Customer Segments", "Value proposition ", "Value Chain", "Revenue Model"],
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

df = pd.DataFrame(data)

# Style generator for table cells
def cell_style(col_index):
    style = "text-align: left; padding: 5px; border: 1px solid #ddd;"
    if col_index in [0, 1]:
        style += " font-weight: bold;"
    return style

# Generate HTML table
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            style = cell_style(j)

            if j == 0:  # Handle merged cells
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
                html += f"<td style='{cell_style(j)}'></td>"
        html += "</tr>"
    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
