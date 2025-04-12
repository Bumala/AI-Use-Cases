import streamlit as st
import pandas as pd

# Defining Data (after removing the first row and first column)
data = [
    ["Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    ["Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4", None],
    ["Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4", None],
    ["Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4", None],
    ["Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4", None],
    ["Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4", None],
    ["Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4", None],
    ["Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4", None],
    ["Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4", None],
    ["Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4", None],
    ["Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4", None],
    ["Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4", None],
]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Generate styled HTML table with merged cells and bold styling for the first two columns
def generate_html_table_with_rowspans(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            if j == 0:  # Handle merged cells for the first column
                if i == 0:  # "Benefits" merged for rows 0-4
                    html += (
                        f"<td rowspan='5' style='font-weight: bold; border: 1px solid black; padding: 8px;'>"
                        f"{value}</td>"
                    )
                elif i == 5:  # "Technology (How)" merged for rows 5-9
                    html += (
                        f"<td rowspan='5' style='font-weight: bold; border: 1px solid black; padding: 8px;'>"
                        f"{value}</td>"
                    )
                elif i == 10:  # "Place (Where)" merged for rows 10-11
                    html += (
                        f"<td rowspan='2' style='font-weight: bold; border: 1px solid black; padding: 8px;'>"
                        f"{value}</td>"
                    )
                elif value is not None:
                    html += f"<td style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"
            elif j == 1:  # Second column, apply bold font
                html += f"<td style='font-weight: bold; border: 1px solid black; padding: 8px;'>{value}</td>"
            else:  # Other columns
                html += f"<td style='border: 1px solid black; padding: 8px;'>{value if value is not None else ''}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate the HTML table
html_table = generate_html_table_with_rowspans(df)

# Display the table in Streamlit
st.write(html_table, unsafe_allow_html=True)
