import streamlit as st
import pandas as pd

# Defining Data
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],  # Merge row 1-5
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", None],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4", None],
    [None, "Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4", None],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4", None],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],  # Merge rows 6-10
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4", None],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4", None],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4", None],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4", None],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None],  # Merge rows 11-12
    [None, "Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4", None],
]

# Dynamically generate styles
styles = []
for i in range(len(data)):  # Loop through each row
    row_styles = []
    for j in range(len(data[i])):  # Loop through each column
        if j == 0 or j == 1:  # First and second columns
            row_styles.append({"bold": True})
        else:  # All other columns
            row_styles.append({"bold": False})
    styles.append(row_styles)

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Generate styled HTML table with rowspan for merged cells
def generate_html_table_with_rowspans(df, styles):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            style = styles[i][j]
            font_weight = "font-weight: bold;" if style.get("bold") else ""
            cell_style = f"{font_weight} padding: 5px; border: 1px solid #ddd;"
            if j == 0:  # First column
                if i == 0 and value == "Impact (What)":
                    html += f"<td rowspan='5' style='{cell_style}'>{value}</td>"
                elif i == 5 and value == "Technology (How)":
                    html += f"<td rowspan='5' style='{cell_style}'>{value}</td>"
                elif i == 10 and value == "Place (Where)":
                    html += f"<td rowspan='2' style='{cell_style}'>{value}</td>"
                elif value is not None:  # Render remaining cells
                    html += f"<td style='{cell_style}'>{value}</td>"
            else:  # Other columns
                html += f"<td style='{cell_style}'>{value if value is not None else ''}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate HTML table
html_table = generate_html_table_with_rowspans(df, styles)

# Display in Streamlit
st.write(html_table, unsafe_allow_html=True)
