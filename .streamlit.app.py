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

# Cell style function
def cell_style():
    return "padding: 10px; border: 1px solid #ccc; text-align: left;"

# Generate the HTML table
def generate_html_table(df):
    html = "<table style='width: 100%; border-collapse: collapse;'>"
    
    for i, row in df.iterrows():
        html += "<tr>"

        # Handle merged left-column labels
        if i == 0:
            html += f"<td rowspan='5' style='{cell_style()} width: 10%; background-color: #e6f0ff; font-weight: bold;'>{row[0]}</td>"
            cells = row[1:]
        elif i == 5:
            html += f"<td rowspan='5' style='{cell_style()} width: 10%; background-color: #e6f0ff; font-weight: bold;'>{row[0]}</td>"
            cells = row[1:]
        elif i == 10:
            html += f"<td rowspan='2' style='{cell_style()} width: 10%; background-color: #e6f0ff; font-weight: bold;'>{row[0]}</td>"
            cells = row[1:]
        elif row[0] is None:
            cells = row[1:]
        else:
            cells = row

        # Count how many actual content cells (non-None)
        content_cells = [c for c in cells if pd.notna(c)]

        # Compute colspan so that cells stretch across the rest of the row
        colspan = int(90 / len(content_cells))  # 90% of width split evenly

        for val in content_cells:
            html += f"<td style='{cell_style()} width: {colspan}%;'>{val}</td>"

        html += "</tr>"

    html += "</table>"
    return html

# Render in Streamlit
st.markdown("### Morphological Box", unsafe_allow_html=True)
st.write(generate_html_table(df), unsafe_allow_html=True)
