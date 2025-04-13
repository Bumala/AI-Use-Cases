import streamlit as st
import pandas as pd

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive" ],
    [None,"Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None,"Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Table cell style
def cell_style(width_percent=None):
    base = "text-align: left; padding: 10px; border: 1px solid #ddd;"
    if width_percent:
        base += f"width: {width_percent}%;"
    return base

# Generate the HTML table with fixed layout
def generate_html_table(df):
    max_columns = max(len(row.dropna()) for _, row in df.iterrows())

    html = "<table style='border-spacing: 0; width: 100%; border: 1px solid black; table-layout: fixed;'>"

    for i, row in df.iterrows():
        html += "<tr>"
        cells = row.dropna().tolist()

        first_cell_merged = False
        if i == 0:
            html += f"<td rowspan='5' style='{cell_style(width_percent=10)}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif i == 5:
            html += f"<td rowspan='5' style='{cell_style(width_percent=10)}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif i == 10:
            html += f"<td rowspan='2' style='{cell_style(width_percent=10)}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif (i < 5 or (5 < i < 10) or i == 11):
            continue

        # How many columns to fill across (excluding merged label cell)
        remaining_columns = max_columns - (1 if first_cell_merged else 0)
        num_cells = len(cells)

        if num_cells > 0:
            base_colspan = remaining_columns // num_cells
            extra = remaining_columns % num_cells
            for idx, val in enumerate(cells):
                colspan = base_colspan + (1 if idx < extra else 0)
                width_percent = round(90 / remaining_columns * colspan, 2)  # 90% is distributed beyond first column
                html += f"<td colspan='{colspan}' style='{cell_style(width_percent=width_percent)}'>{val}</td>"

        html += "</tr>"

    html += "</table>"
    return html

# Show in Streamlit
st.markdown("### Morphological Box")
st.write(generate_html_table(df), unsafe_allow_html=True)
