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

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Function to apply styles for bolding only the first and second columns
def style_table(val, column_index):
    if column_index == 0 or column_index == 1:
        return f"font-weight: bold; text-align: left; padding: 5px; border: 1px solid #ddd;"
    else:
        return f"text-align: left; padding: 5px; border: 1px solid #ddd;"

# Generate HTML table
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for row_index, row in df.iterrows():
        html += "<tr>"
        for col_index, val in enumerate(row):
            style = style_table(val, col_index)
            if col_index == 0:  # Handle merged cells for the first column
                if row_index == 0 and val == "Impact (What)":
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif row_index == 5 and val == "Technology (How)":
                    html += f"<td rowspan='5' style='{style}'>{val}</td>"
                elif row_index == 10 and val == "Place (Where)":
                    html += f"<td rowspan='2' style='{style}'>{val}</td>"
                elif val is not None:
                    html += f"<td style='{style}'>{val}</td>"
            elif val is not None:
                html += f"<td style='{style}'>{val}</td>"
            else:
                html += "<td style='padding: 5px; border: 1px solid #ddd;'></td>"
        html += "</tr>"
    html += "</table>"
    return html

# Generate the HTML table
html_table = generate_html_table(df)

# Display in Streamlit
st.write(html_table, unsafe_allow_html=True)
