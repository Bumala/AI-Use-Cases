import streamlit as st
import pandas as pd

# Define your morphological box data
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Configuration for fixed sizes
first_col_width = 160
second_col_width = 220
base_cell_width = 150
cell_height = "60px"

# Colspan map
colspan_2 = {
    (0, 2), (0, 3), (0, 4),
    (1, 4), (1, 5),
    (2, 4), (2, 5),
    (3, 2), (3, 3), (3, 4),
    (5, 2), (5, 3), (5, 4),
    (7, 4), (7, 5),
    (8, 6),
    (10, 2), (10, 3), (10, 4),
    (11, 2), (11, 3), (11, 4)
}

colspan_3 = {
    (4, 2), (4, 3)
}

# Generate the HTML table
def generate_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"

    for i, row in df.iterrows():
        html += "<tr>"

        for j, val in enumerate(row):
            if pd.isna(val):
                continue

            style = f"padding: 10px; border: 1px solid #ccc; height: {cell_height}; vertical-align: top;"

            if j == 0:
                # First column with merged rows
                if i == 0:
                    html += f"<td rowspan='5' style='width: {first_col_width}px; {style}'>{val}</td>"
                elif i == 5:
                    html += f"<td rowspan='5' style='width: {first_col_width}px; {style}'>{val}</td>"
                elif i == 10:
                    html += f"<td rowspan='2' style='width: {first_col_width}px; {style}'>{val}</td>"
                else:
                    continue
            elif j == 1:
                # Second column
                html += f"<td style='width: {second_col_width}px; {style}'>{val}</td>"
            else:
                # Third column and onward
                if (i, j) in colspan_3:
                    width = base_cell_width * 3
                    html += f"<td colspan='3' style='width: {width}px; {style}'>{val}</td>"
                elif (i, j) in colspan_2:
                    width = base_cell_width * 2
                    html += f"<td colspan='2' style='width: {width}px; {style}'>{val}</td>"
                else:
                    html += f"<td style='width: {base_cell_width}px; {style}'>{val}</td>"

        html += "</tr>"

    html += "</table>"
    return html

# Render in Streamlit
st.markdown("## Morphological Box", unsafe_allow_html=True)
st.markdown(generate_html_table(df), unsafe_allow_html=True)
