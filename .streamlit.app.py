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
    [None, "Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Style generator for table cells
def cell_style():
    return "text-align: left; padding: 10px; border: 1px solid #ddd;"

# Generate HTML table
def generate_html_table(df):
    # Start the table with styling
    html = "<table style='border-spacing: 2px; width: 100%; border: 1px solid black;'>"

    # Generate rows dynamically
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if j == 0:  # First column logic
                if i == 0:  # Merge rows 1 to 5 in the first column
                    html += f"<td rowspan='5' style='{cell_style()}'>{val}</td>"
                elif i == 5:  # Merge rows 6 to 10 in the first column
                    html += f"<td rowspan='5' style='{cell_style()}'>{val}</td>"
                elif i == 10:  # Merge rows 11 and 12 in the first column
                    html += f"<td rowspan='2' style='{cell_style()}'>{val}</td>"
            elif pd.notna(val):  # Handle other cells dynamically
                html += f"<td style='{cell_style()}'>{val}</td>"
        
        html += "</tr>"

    html += "</table>"
    return html

# Display table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
