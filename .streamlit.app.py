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
    [None, "AI Concepts", "Machine Learning", Deep Learning, "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
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

# Generate HTML table
def generate_html_table(df):
    # Find the maximum number of columns in any row
    max_columns = max(len(row.dropna()) for _, row in df.iterrows())

    # Start the table with styling
    html = "<table style='border-spacing: 2px; width: 100%; border: 1px solid black;'>"

    # Generate rows dynamically
    for i, row in df.iterrows():
        html += "<tr>"
        filled_columns = 0  # Track the number of columns filled in the current row

        for j, val in enumerate(row):
            if j == 0 and i == 0:  # Merge rows 1 to 5 in the first column
                html += f"<td rowspan='5' style='{cell_style()}'>{val}</td>"
                filled_columns += 1
            elif j == 0 and i < 5:  # Skip adding cells for rows 2 to 5 in the first column
                continue
            elif j == 0 and i == 5:  # Merge rows 6 to 10 in the first column
                html += f"<td rowspan='5' style='{cell_style()}'>{val}</td>"
                filled_columns += 1
            elif j == 0 and 5 < i < 10:  # Skip adding cells for rows 7 to 10 in the first column
                continue
            elif j == 0 and i == 10:  # Merge rows 11 and 12 in the first column
                html += f"<td rowspan='2' style='{cell_style()}'>{val}</td>"
                filled_columns += 1
            elif j == 0 and i == 11:  # Skip adding the cell for row 12 in the first column
                continue
            elif pd.notna(val):  # Check if the cell is not empty (not NaN)
                html += f"<td style='{cell_style()}'>{val}</td>"
                filled_columns += 1

        # If there are fewer columns in the current row, span the remaining columns
        if filled_columns < max_columns:
            colspan = max_columns - filled_columns
            html += f"<td colspan='{colspan}' style='{cell_style()}'></td>"

        html += "</tr>"

    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
