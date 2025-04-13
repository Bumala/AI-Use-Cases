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
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Generate HTML table
def generate_html_table(df):
    # Set universal dimensions
    cell_width = 150  # in px
    cell_height = "50px"

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed;'>"

    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):

                # Merge logic
                if j == 0 and i == 0:
                    html += f"<td rowspan='5' style='text-align: left; padding: 10px; width: {cell_width}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
                elif j == 0 and i == 5:
                    html += f"<td rowspan='5' style='text-align: left; padding: 10px; width: {cell_width}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
                elif j == 0 and i == 10:
                    html += f"<td rowspan='2' style='text-align: left; padding: 10px; width: {cell_width}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
                elif j == 0 and (i < 5 or (5 < i < 10) or i == 11):
                    continue

                # Colspan rules
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

                if (i, j) in colspan_2:
                    html += f"<td colspan='2' style='text-align: left; padding: 10px; width: {cell_width*2}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
                elif (i, j) in colspan_3:
                    html += f"<td colspan='3' style='text-align: left; padding: 10px; width: {cell_width*3}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
                else:
                    html += f"<td style='text-align: left; padding: 10px; width: {cell_width}px; height: {cell_height}; border: 1px solid #ccc;'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# Display in Streamlit
st.markdown("### Morphological Box with Fixed Cell Size")
st.markdown(generate_html_table(df), unsafe_allow_html=True)
