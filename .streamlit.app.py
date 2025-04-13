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

# Style generator for table cells
def cell_style():
    return "text-align: left; padding: 10px; border: 1px solid #ddd;"

# Generate HTML table with dynamic colspan logic
def generate_html_table(df):
    max_columns = max(len(row.dropna()) for _, row in df.iterrows())
    html = "<table style='border-spacing: 2px; width: 100%; border: 1px solid black;'>"

    for i, row in df.iterrows():
        html += "<tr>"
        cells = row.dropna().tolist()

        # Determine if the first cell is a merged vertical label
        first_cell_merged = False
        if i == 0:
            html += f"<td rowspan='5' style='{cell_style()}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif i == 5:
            html += f"<td rowspan='5' style='{cell_style()}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif i == 10:
            html += f"<td rowspan='2' style='{cell_style()}'>{cells[0]}</td>"
            cells = cells[1:]
            first_cell_merged = True
        elif (i < 5 or (5 < i < 10) or i == 11):
            # These are skipped rows for merged cells
            continue

        # Calculate how many columns are available for the remaining cells
        num_cells = len(cells)
        span = max_columns - (1 if first_cell_merged else 0)
        base_colspan = span // num_cells if num_cells > 0 else 1
        extra_cols = span % num_cells

        for idx, val in enumerate(cells):
            colspan = base_colspan + (1 if idx < extra_cols else 0)
            html += f"<td colspan='{colspan}' style='{cell_style()}'>{val}</td>"

        html += "</tr>"

    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
