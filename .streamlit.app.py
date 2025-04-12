import streamlit as st
import pandas as pd

# Defining Data
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

# Remove the first row and first column
data = [row[1:] for row in data[1:]]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Generate styled HTML table with rowspan for merged cells
def generate_html_table_with_rowspans(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            if j == 0:  # Handle merged cells for the first column
                if i == 0 and value == "Benefits":
                    html += f"<td rowspan='4' style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"



```python
                elif i == 4 and value == "Row 6, Col 2":
                    html += f"<td rowspan='5' style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"
                elif i == 9 and value == "Row 11, Col 2":
                    html += f"<td rowspan='2' style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"
                elif value is not None:
                    html += f"<td style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"
            else:  # Handle other columns
                style = "font-weight: bold;" if j == 1 else ""  # Bold only for second column
                html += f"<td style='{style} border: 1px solid black; padding: 8px;'>{value if value is not None else ''}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate the HTML table
html_table = generate_html_table_with_rowspans(df)

# Display in Streamlit
st.write(html_table, unsafe_allow_html=True)
