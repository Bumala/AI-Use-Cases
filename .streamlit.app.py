import streamlit as st

# Define the table data
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

# Start building the HTML table
html = """
<style>
    table {
        border-collapse: collapse;
        width: 100%;
        table-layout: fixed;
    }
    td, th {
        border: 1px solid #ddd;
        text-align: left;
        padding: 10px;
    }
    th {
        background-color: #f4f4f4;
    }
    td[rowspan] {
        background-color: #e8f4f8;
        font-weight: bold;
    }
    .variable-width {
        width: auto;
    }
    .fixed-width {
        width: 20%;
    }
</style>
<table>
"""

# Loop through the data to populate rows
for i, row in enumerate(data):
    html += "<tr>"
    for j, cell in enumerate(row):
        if j == 0:  # Handle the first column with row spans
            if i == 0:
                html += f"<td rowspan='5'>{cell}</td>"
            elif i == 5:
                html += f"<td rowspan='5'>{cell}</td>"
            elif i == 10:
                html += f"<td rowspan='2'>{cell}</td>"
        elif cell is not None:
            # Add alternating widths for other columns
            if j > 1:  # From the third column onward
                html += f"<td class='variable-width'>{cell}</td>"
            else:  # Second column
                html += f"<td class='fixed-width'>{cell}</td>"
    html += "</tr>"

html += "</table>"

# Render the HTML in Streamlit
st.write(html, unsafe_allow_html=True)
